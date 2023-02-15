from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from get_query_data import launches_data, rockets_data
from models import Launch, Rocket
from data_crud import Data_post

# for docker
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1@postgres:5432/spacex"

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1@localhost:5432/spacex"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)


def insert_rockets(db: Session):
    """Добавляем спарсенные данные в бд(ракеты)"""

    data = rockets_data().json()['data']['rockets']
    object = Data_post(db, Rocket)

    for i in range(len(data)):
        object.add_to_base(
            name=data[i]['name'],
            first_flight=data[i]['first_flight'],
            description=data[i]['description']
        )


def insert_launches(db: Session):
    """Добавляем спарсенные данные в бд(запуски)"""

    data = launches_data().json()['data']['launches']
    object = Data_post(db, Launch)

    for i in range(len(data)):
        object.add_to_base(
            mission_name=data[i]['mission_name']
        )


def count_rockets(db: Session):
    """Считаем кол-во ракет"""

    return db.query(Rocket).count()


def count_launches(db: Session):
    """Считаем кол-во запусков"""

    return db.query(Launch).count()


def check_db(db: Session):
    """Если база пустая - вызываем скрипт добавления объектов в базу,
    если объекты в базе есть - выводим их кол-во"""

    if count_rockets(db) == 0 and count_launches(db) == 0:
        insert_rockets(db)
        insert_launches(db)

    print(f'\nTotal rockets: {count_rockets(db)}\n'
          f'Total launches: {count_launches(db)}\n')


if __name__ == '__main__':
    check_db(Session())
