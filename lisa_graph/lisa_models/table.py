# -*- coding: UTF-8 -*-
from mongoengine import *
from lisa_models.key import Key_Model

class Table_Model (Document):
    name = StringField()
    description = StringField()
    titles = ListField()
    rows = ListField()
    keys = ListField(EmbeddedDocumentField(Key_Model))


