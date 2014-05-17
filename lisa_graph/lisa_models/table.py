# -*- coding: UTF-8 -*-
from mongoengine import *
from lisa_models.key import Key_Model
import datetime

class Table_Model (Document):
    name = StringField(required=True)
    description = StringField()
    titles = ListField()
    rows = ListField()
    keys = ListField(ReferenceField(Key_Model))
    creation_date = DateTimeField(default=datetime.datetime.now)