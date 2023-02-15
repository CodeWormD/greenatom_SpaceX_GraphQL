class Data_post:
    """Универсальный класс для добавления объектов в базу данных"""

    def __init__(self, db, model):
        self.db = db
        self.model = model

    def add_to_base(self, *args, **kwargs):
        object = self.model(*args, **kwargs)
        self.db.add(object)
        self.db.commit()
        self.db.refresh(object)