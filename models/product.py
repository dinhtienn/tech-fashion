from mongoengine import *

class Product(Document):
    image = StringField()
    name = StringField()
    product_type = StringField()
    description = StringField()
    price = IntField()
    status = StringField()
    place = StringField()