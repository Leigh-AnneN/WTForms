from models import Pet, db
from app import app

#Create all tables

db.drop_all()
db.create_all()

p1 = Pet(name="Sandy", species="dog", photo_url="https://www.akc.org/wp-content/uploads/2019/10/ottherhound-outdoors.jpeg", age="5", notes="Great with kids", available=True)
p2 = Pet(name="Sandman", species="cat", photo_url="https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg", age="8", notes="Very friendly", available=False)
p3 = Pet(name="Carrots", species="bunny", photo_url="https://media.newyorker.com/photos/59096937019dfc3494ea1169/master/w_2560%2Cc_limit/Frazier-Bunny-Rabbits.jpg", age="1", notes="Cute", available=True)


db.session.add(p1)
db.session.add(p2)
db.session.add(p3)

db.session.commit()
