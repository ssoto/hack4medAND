# -*- coding: UTF-8 -*-
from mongoengine import *
import datetime

from lisa_models.key import Key_Model

class Table_Model (Document):
    name = StringField(required=True, unique=True)
    description = StringField()
    titles = ListField()
    rows = ListField()
    keys = ListField(ReferenceField(Key_Model))
    row_types = DictField()
    creation_date = DateTimeField(default=datetime.datetime.now)