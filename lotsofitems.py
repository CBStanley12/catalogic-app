# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Collection, Item

engine = create_engine('sqlite:///catalogic_data.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

# Create users
User1 = User(name="Garth Tatum", email="garth.tatum@fake.com", picture="https://unsplash.com/photos/wKOKidNT14w")
User2 = User(name="Russell Elliot", email="relliot@fake.com", picture="https://unsplash.com/photos/tAvpDE7fXgY")
User3 = User(name="Randolph Harrelson", email="randolph@fake.com", picture="https://unsplash.com/photos/sibVwORYqs0")
User4 = User(name="Minnie Rennell", email="minnie@fake.com", picture="https://unsplash.com/photos/rDEOVtE7vOs")
User5 = User(name="Jaye Maddison", email="jaye.mad@fake.com", picture="https://unsplash.com/photos/Ugpcxb0jG4Q")
User6 = User(name="Anabella Danell", email="adanell@fake.com", picture="https://unsplash.com/photos/IPETsB4dcCs")

session.add_all([User1, User2, User3, User4, User5, User6])
session.commit()

# Create categories
category1 = Category(name="Clothing")
category2 = Category(name="Shoes")
category3 = Category(name="Electronics")
category4 = Category(name="Books")
category5 = Category(name="Movies")
category6 = Category(name="Music")
category7 = Category(name="Video Games")
category8 = Category(name="Cosmetics")
category9 = Category(name="Sports")
category10 = Category(name="Outdoors")
category11 = Category(name="Toys & Games")
category12 = Category(name="Industrial & Scientific")
category13 = Category(name="Luggage & Travel")
category14 = Category(name="Watches")
category15 = Category(name="Historical")
category16 = Category(name="Currency")

session.add_all([category1, category2, category3, category4, category5, category6, category7, category8, category9, category10, category11, category12, category13, category14])
session.commit()

# Create collections
collection1 = Collection(user_id=2, name="Beanie Babies", description="A collection of beanie babies", category=category11)
collection2 = Collection(user_id=3, name="Luxury Watches", description="A collection of luxury watches", category=category14)
collection3 = Collection(user_id=4, name="Baseball Cards", description="A collection of baseball cards", category=category9)

session.add_all([collection1, collection2, collection3])
session.commit()

# Create items for collection1
collection1_item1 = Item(name="Employee Bear (Green Ribbon)", description="", collection=collection1, user_id=2)
collection1_item2 = Item(name="Mystic (Unicorn)", description="", collection=collection1, user_id=2)
collection1_item3 = Item(name="Chef Robuchon", description="Introduced in August 2006 for the opening of the L'Atelier de Joel Robuchon restaurant at the Four Seasons Hotel in New York (only about 200 were produced)", collection=collection1, user_id=2)
collection1_item4 = Item(name="#1 the Bear", description="Gifts for Ty sales representatives (only about 250 were produced)", collection=collection1, user_id=2)
collection1_item5 = Item(name="Hong Kong Toy Fair 2010 (Bear)", description="Special Beanie Baby made for the Hong Kong toy show", collection=collection1, user_id=2)
collection1_item6 = Item(name="Patti (Platypus)", description="One of the original nine Beanie Babies", collection=collection1, user_id=2)
collection1_item7 = Item(name="M.C. Beanie", description="Produced for MasterCard applicants from 2001 to 2002", collection=collection1, user_id=2)
collection1_item8 = Item(name="Humphrey", description="One of the first Beanies, and one of the first to be retired", collection=collection1, user_id=2)
collection1_item9 = Item(name="Spot", description="One of the original nine Beanie Babies", collection=collection1, user_id=2)

session.add_all([collection1_item1, collection1_item2, collection1_item3, collection1_item4, collection1_item5, collection1_item6, collection1_item7, collection1_item8, collection1_item9])
session.commit()

# Create items for collection2
collection2_item1 = Item(name="Patek Philippe Grand Complications 41MM, 18K Rose Gold and Alligator", description="", collection=collection2, user_id=3)
collection2_item2 = Item(name="Jaeger-Lecoultre Master Ultra Thin Moon 39MM, Stainless Steel and Alligator", description="", collection=collection2, user_id=3)
collection2_item3 = Item(name="Omega Speedmaster Racing Automatic Chronograph 40MM, Stainless Steel", description="", collection=collection2, user_id=3)
collection2_item4 = Item(name="Blancpain Fifty Fathoms Meteor Automatic 43MM", description="", collection=collection2, user_id=3)
collection2_item5 = Item(name="Chanel Monsieur Watch 40MM", description="", collection=collection2, user_id=3)

session.add_all([collection2_item1, collection2_item2, collection2_item3, collection2_item4, collection2_item5])
session.commit()

# Create items for collection3
collection3_item1 = Item(name="1909-11 T206 White Border Honus Wagner", description="", collection=collection3, user_id=4)
collection3_item2 = Item(name="1952 Topps #311 Mickey Mantle", description="", collection=collection3, user_id=4)
collection3_item3 = Item(name="1916 (M101-5) Sporting News Babe Ruth Rookie Card", description="", collection=collection3, user_id=4)
collection3_item4 = Item(name="1909-11 Ty Cobb Tobacco (Ty Cobb Back)", description="", collection=collection3, user_id=4)
collection3_item5 = Item(name="1914 Baltimore News #9 Babe Ruth", description="", collection=collection3, user_id=4)

session.add_all([collection3_item1, collection3_item2, collection3_item3, collection3_item4, collection3_item5])

print("Items sucessfully added to database!")