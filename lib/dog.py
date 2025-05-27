from models import Dog

def create_table(base, engine):
    # Create tables in the database using the base metadata and engine
    base.metadata.create_all(engine)

def save(session, dog):
    # Add the dog instance to session and commit to save it
    session.add(dog)
    session.commit()

def get_all(session):
    # Return all Dog records
    return session.query(Dog).all()

def find_by_name(session, name):
    # Return the first Dog record matching the name
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    # Return the Dog record with the given id
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    # Return Dog record matching both name and breed
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    # Update the breed of the given Dog instance and commit
    dog.breed = breed
    session.commit()
