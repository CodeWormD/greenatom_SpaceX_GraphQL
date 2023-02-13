from get_query_data import rockets_data, launches_data
from models import Rocket, Launch
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1@localhost/spacex"


engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)


Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)


def insert_rockets(db: Session):

    data = rockets_data().json()['data']['rockets']

    for i in range(len(data)):
        rocket = Rocket(
            name=data[i]['name'],
            first_flight=data[i]['first_flight'],
            description=data[i]['description']
        )

        db.add(rocket)
        db.commit()
        db.refresh(rocket)



def insert_launches(db: Session):

    data = launches_data().json()['data']['launches']
    for i in range(len(data)):
        rocket = Launch(
            mission_name=data[i]['mission_name']
        )

        db.add(rocket)
        db.commit()
        db.refresh(rocket)



def count_rockets(db: Session):
    return db.query(Rocket).count()


def count_launches(db: Session):
    return db.query(Launch).count()


def check_db(db: Session):
    if count_rockets(Session()) == 0 and count_launches(Session()) == 0:
        insert_rockets(Session())
        insert_launches(Session())

    print(f'\nTotal rockets: {count_rockets(Session())}\n'
          f'Total launches: {count_launches(Session())}\n')


if __name__ == '__main__':
    check_db(Session())
