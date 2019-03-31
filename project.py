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

# CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Animal Catalog Application"

engine = create_engine('sqlite:///item_catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Display categories
@app.route('/')
@app.route('/categories/')
def showCategories():
    categories = session.query(Category).order_by(Category.name)
    return render_template('categories.html', categories = categories)

# Display items in category
@app.route('/categories/<int:category_id>/')
def showAnimals(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    animals = session.query(Item).filter_by(category_id = category_id)
    return render_template('animals.html', animals = animals, category = category)

if __name__ == '__main__':
    # app.secret.key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)

