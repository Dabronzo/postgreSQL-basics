from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# Create a class base model for the "Programmer"

class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)
#C of CRUD
#Creating new records for our table(class) Programmer

ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "Female",
    nationality = "English",
    famous_for = "First Programmer Ever",
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

ayrton_dabronzo = Programmer(
    first_name="Ayrton",
    last_name="D'Abronzo",
    gender="M",
    nationality="Brazilian",
    famous_for="Game Developer"
)

# add each instance on our databse
# session.add(ada_lovelace)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(ayrton_dabronzo)



# Updating a record from the database
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "Creator of GamOne"

# Updating multiple records

# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     #commiting the session
#     session.commit()

# Deleting a record

# fname = input("Enter the first name: ")
# lname = input("Enter the last name: ")

# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming

# if programmer is not None:
#     print("Programmer Found: " + programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Do you want to delete this record? (y/n)")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer have been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("Programmer not found")

    

# Commit the session
# session.commit()

# query testing the new record on the database

programmers = session.query(Programmer)
for programmer in programmers:
    print (
        programmer.id,
        programmer.first_name,
        programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep = " | "
    )