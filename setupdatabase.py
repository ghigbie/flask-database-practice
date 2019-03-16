from app import db, Puppy

db.create_all() #creates all tables, transforms model class to table
sam = Puppy('Sammy', 3, 'blue', 'male')
frank = Puppy('Frankie', 1, 'red', 'male')
cutie = Puppy('Cutie', 1, 'light brown', 'female')

print(sam.id)
print(frank.id)
print(cutie.id)

db.sesssion.add([sam, frank, cutie])
db.session.commit()

print(sam.id)
print(frank.id)
print(cutie.id)