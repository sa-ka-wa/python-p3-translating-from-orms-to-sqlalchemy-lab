from models import Dog

def create_table(base,engine):
    """
    Create the Dog table in the database.
    """
    sql = """
    CREATE TABLE IF NOT EXISTS dogs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        breed TEXT NOT NULL,
        age INTEGER NOT NULL
    );
    """
    base.metadata.create_all(engine)
    return base
    pass

def save(session, dog):
    """
    Save a Dog object to the database.
    """
    sql = """
    INSERT INTO dogs (name, breed, age)
    VALUES (:name, :breed, :age);
    """
    session.add(dog)
    session.commit()
    pass

def get_all(session):
    return session.query(Dog).all()
    pass

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()
    pass

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()
    pass

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()
    pass

def update_breed(session, dog, breed):
    dog.breed = breed; session.commit()
    pass