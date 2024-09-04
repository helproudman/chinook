from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instrucitons from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
# class Programmer(base):
#     __tablename__ = "Programmer"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     gender = Column(String)
#     nationality = Column(String)
#     famous_for = Column(String)

# create class based model for the "Places" table    
class Places(base):
    __tablename__ = "Places"
    id = Column(Integer, primary_key=True)
    country_name = Column(String)
    capital_city = Column(String)
    population = Column(Integer)
    language = Column(String)
    currency = Column(String)



# instead of connection to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# create records oon the "Places" table
united_kingdom = Places(
    country_name = "United Kingdom",
    capital_city = "London",
    population = 50000,
    language = "English",
    currency = "Pound"

)

# create records on our Programmer table
# ada_lovelace = Programmer(
#     first_name="Ada",
#     last_name="Lovelace",
#     gender="f",
#     nationality="British",
#     famous_for="First Programmer"
# )

# alan_turing = Programmer(
#     first_name="Alan",
#     last_name="Turing",
#     gender="m",
#     nationality="British",
#     famous_for="Modern computing"
# )

# grace_hopper = Programmer(
#     first_name="Grace",
#     last_name="Hopper",
#     gender="f",
#     nationality="American",
#     famous_for="COBOL language"
# )

# alan_turing = Programmer(
#     first_name="Alan",
#     last_name="Turing",
#     gender="m",
#     nationality="British",
#     famous_for="Modern computing"
# )

# margaret_hamilton = Programmer(
#     first_name="Margaret",
#     last_name="Hamilton",
#     gender="f",
#     nationality="American",
#     famous_for="Apollo 11"
# )

# bill_gates = Programmer(
#     first_name="Bill",
#     last_name="Gates",
#     gender="m",
#     nationality="American",
#     famous_for="Microsoft"
# )

# tim_berners_lee = Programmer(
#     first_name="Tim",
#     last_name="Berners-Lee",
#     gender="m",
#     nationality="British",
#     famous_for="World Wide Web"
# )

# helen_proudman = Programmer(
#     first_name="Helen",
#     last_name="Proudman",
#     gender="f",
#     nationality="British",
#     famous_for="Drinking tea"
# )
session.add(united_kingdom)
session.commit()


# query the database to find all programmers
places = session.query(Places)
for place in places:
    print(
        place.id,
        place.country_name,
        place.capital_city,
        place.population,
        place.language,
        place.currency,
        sep = " | "        
    )

# add records to the table
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(helen_proudman)

# commit session to the database
# session.commit()

# undating a single record
# programmer = session.query(Programmer).filter_by(id=8).first()
# programmer.famous_for = "World President"

# commit the session to the database
# session.commit()

# updating multiple records
# people = session.query(Programmer)

# for person in people:
#     if person.gender == "f":
#         person.gender = "Female"
#     elif person.gender == "m":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()     

# deleting a single record

# fname = input("Enter a firstname: ")
# lname = input("Enter a last name: ")

# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()

# # defensive programming....double checking
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this programmer?  y/n ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No record found")            


# query the database to find all programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep = " | "        
#     )

