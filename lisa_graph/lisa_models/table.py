# -*- coding: UTF-8 -*-
from mongoengine import *

class Table_Model (Document):
    name = StringField()
    description = StringField()
    titles = ListField()
    rows = ListField()
    keys = ListField()


