# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///item_catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

# Create fake users
User1 = User(name="Garth Tatum", email="garth.tatum@fake.com", picture="https://unsplash.com/photos/wKOKidNT14w")
session.add(User1)
session.commit()

User2 = User(name="Russell Elliot", email="relliot@fake.com", picture="https://unsplash.com/photos/tAvpDE7fXgY")
session.add(User2)
session.commit()

User3 = User(name="Randolph Harrelson", email="randolph@fake.com", picture="https://unsplash.com/photos/sibVwORYqs0")
session.add(User3)
session.commit()

User4 = User(name="Minnie Rennell", email="minnie@fake.com", picture="https://unsplash.com/photos/rDEOVtE7vOs")
session.add(User4)
session.commit()

User5 = User(name="Jaye Maddison", email="jaye.mad@fake.com", picture="https://unsplash.com/photos/Ugpcxb0jG4Q")
session.add(User5)
session.commit()

User6 = User(name="Anabella Danell", email="adanell@fake.com", picture="https://unsplash.com/photos/IPETsB4dcCs")
session.add(User6)
session.commit()

# Create categories of animal types
category1 = Category(user_id=1, name="Reptiles")
session.add(category1)
session.commit()

category2 = Category(user_id=2, name="Amphibians")
session.add(category2)
session.commit()

category3 = Category(user_id=3, name="Birds")
session.add(category3)
session.commit()

category4 = Category(user_id=4, name="Mammals")
session.add(category4)
session.commit()

category5 = Category(user_id=5, name="Fish")
session.add(category5)
session.commit()

category6 = Category(user_id=6, name="Insects")
session.add(category6)
session.commit()

# Create animals in respective categories
reptile1 = Item(user_id=1, name="American Alligator", description="American alligators, or simply, gators, are common crocodilians that are native to the southeastern United States. These alligators are an amazing conservation success story, and were once driven to the brink of extinction. Nowadays these large reptiles have thriving populations. Read on to learn about the American alligator.", category=category1)
session.add(reptile1)
session.commit()

reptile2 = Item(user_id=1, name="Green Anaconda", description="Would you be surprised if you were told that green anacondas are, green? While they are not neon green or anything of the sort, they are a muddy green that blends in to the turbid waters of the Amazon and other South American rivers. Their scales are also blotched with black spots that help them camouflage themselves. They are the largest snakes in the Americas, but their maximum size is highly debated.", category=category1)
session.add(reptile2)
session.commit()

reptile3 = Item(user_id=1, name="Chameleon", description="These famously colorful lizards are a diverse group of color-changing creatures. They use their ability to change their skin pigmentation as a form of camouflage and communication. These reptiles have a number of identifying traits. Read on to learn about the chameleon.", category=category1)
session.add(reptile3)
session.commit()

amphibian1 = Item(user_id=2, name="Bullfrog", description='Bullfrogs, also known as "American bullfrogs," are large semi-aquatic amphibians. They are considered to be "true frogs," and truly are the archetype for what most people imagine when they think of a frog. These large amphibians are interesting creatures, and are used in a number of different ways. Read on to learn about the bullfrog.', category=category2)
session.add(amphibian1)
session.commit()

amphibian2 = Item(user_id=2, name="Salamander", description="Frogs are cute, sure, but salamanders definitely hold the title for cutest amphibian. These often colorful, unique little animals are long and slender, with short legs and a rounded head. With over 500 different species, there's something for everyone to love! Read on to learn about the salamander.", category=category2)
session.add(amphibian2)
session.commit()

amphibian3 = Item(user_id=2, name="Cane Toad", description='The cane toad is a large amphibian native to South and Central America. They are also known as "marine toads," and "giant neotropical toads." These creatures have voracious appetites, which poses a problem in the areas into which they have been introduced. Cane toads are a problematic invasive species in the southeastern United States, Australia, and a number of islands. Read on to learn about the cane toad.', category=category2)
session.add(amphibian3)
session.commit()

bird1 = Item(user_id=3, name="Bald Eagle", description="As the United States' national bird, most people realize this but... the bald eagle isn't bald at all! These white-headed birds are majestic predators found across the entirety of the United States, and most of North America. Read on to learn about the bald eagle.", category=category3)
session.add(bird1)
session.commit()

bird2 = Item(user_id=3, name="Ostrich", description="Ostriches are large, flightless birds with long legs, long necks, and light airy feathers. They are simply massive birds, both in height and in weight. To make up for their inability to fly, ostriches are capable of running and kicking with their powerful legs. Read on to learn about the ostrich.", category=category3)
session.add(bird2)
session.commit()

bird3 = Item(user_id=3, name="Peregrine Falcon", description="Peregrine falcons are incredibly impressive hunters, and are one of the most unique species on the planet. This is because they are the fastest animals on earth! These skilled flyers are both impressive and adaptable to a number of different environments. Read on to learn about the peregrine falcon.", category=category3)
session.add(bird3)
session.commit()

mammal1 = Item(user_id=4, name="African Lion", description="These famous cats are frequently portrayed in cartoons, movies, and television. Lions are imposing cats that exhibit unrivaled teamwork among felines. These magnificent predators are world renowned, and for good reason! Read on to learn about the African lion.", category=category4)
session.add(mammal1)
session.commit()

mammal2 = Item(user_id=4, name="Spider Monkey", description="Spider monkeys are a group of primates native to Central and South America. They are all members of the genus Ateles, and have long limbs and long, prehensile tails. Scientists have identified seven different species of spider monkey, all of which may face extinction. Two species, the black-headed and brown spider monkey, are Critically Endangered. Read on to learn about the spider monkey.", category=category4)
session.add(mammal2)
session.commit()

mammal3 = Item(user_id=4, name="Brown Bear", description="Brown bears are a large species of bear that ranges throughout much of the Northern Hemisphere. They are massive animals, and the only bear species larger than brown bears is polar bears. In fact, brown bears are closely related to polar bears, and share some of the same habitat. Hybrids of these two species are rare, but do occur, especially because many polar bears must roam farther south due to climate change. Read on to learn about the brown bear.", category=category4)
session.add(mammal3)
session.commit()

fish1 = Item(user_id=5, name="Great White Shark", description="The great white shark is the very picture of ferocity and shark attacks. Great whites are not mindless killers in search of human flesh. These apex predators are horribly misunderstood, and deserve our respect. Read on to learn about the great white shark.", category=category5)
session.add(fish1)
session.commit()

fish2 = Item(user_id=5, name="Stingray", description="Stingrays are a family of fish, primarily composed of cartilage, that are closely related to sharks. They are characterized by their flattened bodies and long tails, which are sometimes equipped with a defensive spine. There are eight different families of stingrays: sixgill, deepwater, stingarees, round rays, whiptail, river, butterfly, and eagle rays. Read on to learn about the stingray.", category=category5)
session.add(fish2)
session.commit()

fish3 = Item(user_id=5, name="Piranha", description="Piranhas are freshwater fish native to South American rivers, streams, lakes, and floodplains. Scientists believe there may be anywhere between 40 and 60 different species. These fish are notorious for their dangerous swarming behavior. In reality, most of the time these fish are harmless to humans, and attacks result in minor injuries. Read on to learn about the piranha.", category=category5)
session.add(fish3)
session.commit()

insect1 = Item(user_id=6, name="Ant", description="This impressively diverse group of animals has developed hundreds of different adaptations to survive in many different habitats. Scientists estimate that we have discovered only slightly more than half of the ant species in the world. The species that we have discovered are simply fascinating. Read on to learn about the ant.", category=category6)
session.add(insect1)
session.commit()

insect2 = Item(user_id=6, name="Ladybug", description='Ladybugs are a large group of insects in the Coccinellidae taxonomic family. They are small beetles, and depending on the region the ladybug is also referred to as "ladybirds," "lady beetles," or "ladybird beetles." There are a huge variety of species in the Coccinellidae family, possibly 5,000 or more! The vast majority of species feed on pest species, making them beneficial for farmers. Read on to learn about the ladybug.', category=category6)
session.add(insect2)
session.commit()

insect3 = Item(user_id=6, name="Monarch Butterfly", description="Monarch butterflies are possibly the most widely known butterfly species in North America. Depending on the region, they are also referred to as monarch, black veined brown, milkweed, wanderer, and common tiger. It has an easily-recognizable pattern, and makes a stunning appearance during its lengthy migration across North America. Read on to learn about the monarch butterfly.", category=category6)
session.add(insect3)
session.commit()


print("Items added to database!")