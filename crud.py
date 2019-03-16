from app import db, Puppy

#Create
my_puppy = Puppy('Rufus', 5, 'brown', 'male')
db.session.add(my_puppy)
db.session.commit()

#Read
all_puppies = Puppy.query.all()
print(all_puppies)

#select by id
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

#filters - will produce sql code
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie)
print(puppy_frankie.all())

#update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

rufus = Puppy.query.filter_by(name='Rufus')
rufus.fur = 'orange'
db.session.commit()

#delete
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

#show results
all_puppies = Puppy.query.all()
print('AFTER everything: ', all_puppies)