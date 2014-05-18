# -*- coding: UTF-8 -*-

from mongoengine import *

class DynamicTable(Document):
    name = StringField()
    rows = ListField(DictField())
