from tortoise import Model
from tortoise import fields

class Model(Model):
    name = fields.CharField(max_length=50)
    age = fields.IntField()
