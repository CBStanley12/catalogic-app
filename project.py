from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item
from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from oauth2client.client import AccessTokenCredentials
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Animal Catalog Application"

engine = create_engine('sqlite:///item_catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Render login page and reate anti-forgery state token for user login
@app.route('/login/')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE = state)

# Login with Google OAuth
@app.route('/gconnect', methods = ['POST'])
def gconnect():
    # Validate the state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain the authorization code
    code = request.data
    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Check that the access token is valid
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    # Create a JSON GET request
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Verify that the access token is used for the intended user
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Check to see if the user is already logged in
    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
    # Store the access token in the session for later use
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id
    # Get the user's info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token' : credentials.access_token, 'alt' : 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = json.loads(answer.text)

    login_session['provider'] = 'google'
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # Check to see if it is an existing user, and create the user if not
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += "<div class='col-12'><h1>Welcome, %s!</h1></div>" % login_session['username']
    output += "<div class='col-12 text-center'><img src='%s' style='width: 300px; height: 300px; border-radius: 150px; -webkit-border-radius: 150px; -moz-border-radius: 150px;'></div>" % login_session['picture']
    return output

# Disconnect user's logged in with Google OAuth
@app.route('/gdisconnect')
def gdisconnect():
    # DISCONNECT - Revoke a current user's token and reset their login_session
    # Only disconnect a connected user
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Execute HTTP GET request to revoke current token
    access_token = credentials
    url = "https://accounts.google.com/o/oauth2/revoke?token=%s" % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        # Reset the user's session
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        # For whatever reason, the given token was invalid
        response = make_response(json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response

# Disconnect and log out the user
@app.route('/disconnect')
def disconnect():
    # Disconnect a user from the login_session if they are logged in
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['credentials']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        return redirect(url_for('showCategories'))
    # Redirect to showCategories if the user is not logged in
    else:
        redirect(url_for('showCategories'))

# Display all categories
@app.route('/')
@app.route('/categories/')
def showCategories():
    categories = session.query(Category).order_by(Category.name)
    if 'username' not in login_session:
        return render_template('publiccategories.html', categories = categories)
    else:
        user = getUserInfo(login_session['user_id'])
        return render_template('categories.html', categories = categories, user = user)

# Add new categories
@app.route('/categories/new/', methods=['GET', 'POST'])
def newCategory():
    if 'username' not in login_session:
        return redirect('/login/')
    if request.method == 'POST':
        newCategory = Category(name = request.form['name'], user_id = login_session['user_id'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        user = getUserInfo(login_session['user_id'])
        return render_template('newcategory.html', user = user)

# Edit category
@app.route('/categories/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedCategory = session.query(Category).filter_by(id = category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
        session.add(editedCategory)
        session.commit()
        flash("New category has been created!")
        return redirect(url_for('showItems', category_id = category_id))
    else:
        return render_template('editcategory.html', category_id = category_id, i = editedCategory)

# Delete category
@app.route('/categories/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    if 'username' not in login_session:
        return redirect('/login')
    categoryToDelete = session.query(Category).filter_by(id = category_id).one()
    if categoryToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to delete this category.');}</script><body onload='myFunction()'>"
    elif request.method == 'POST':
        session.delete(categoryToDelete)
        session.commit()
        flash("Category has been deleted")
        return redirect(url_for('showCategories'))
    else:
        return render_template('deletecategory.html', category_id = category_id, i = categoryToDelete)

# Display items in a category
@app.route('/categories/<int:category_id>/items')
def showItems(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    creator = getUserInfo(category.user_id)
    items = session.query(Item).filter_by(category_id = category_id)
    if 'username' not in login_session or creator.id != login_session['user_id']:
        if 'username' in login_session:
            user = getUserInfo(login_session['user_id'])
            return render_template('publicitems.html', items = items, category = category, creator = creator, user = user)
        else:
            return render_template('publicitems.html', items = items, category = category, creator = creator)
    else:
        user = getUserInfo(login_session['user_id'])
        return render_template('items.html', items = items, category = category, creator = creator, user = user)

# Add new item
@app.route('/categories/<int:category_id>/items/new/', methods=['GET', 'POST'])
def newItem(category_id):
    if 'username' not in login_session:
        return redirect('/login')
    elif request.method == 'POST':
        newItem = Item(name = request.form['name'], description = request.form['desc'], category_id = category_id, user_id = login_session['user_id'])
        session.add(newItem)
        session.commit()
        flash("Item has been created!")
        return redirect(url_for('showItems', category_id = category_id))
    else:
        return render_template('newitem.html', category_id = category_id)

# Helpful methods for user login and user information
def getUserID(email):
    try:
        user = session.query(User).filter_by(email = email).one()
        return user.id
    except:
        return None

def getUserInfo(user_id):
    user = session.query(User).filter_by(id = user_id).one()
    return user

def createUser(login_session):
    newUser = User(name = login_session['username'], email = login_session['email'], picture = login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email = login_session['email']).one()
    return user.id

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
