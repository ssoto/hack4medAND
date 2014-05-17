# -*- coding: UTF-8 -*-
from lisa_modules.csv_reader import CSV
from lisa_models.table import Table_Model
from lisa_models.key import Key_Model

def persist_csv(csv_object, key_list=None):
    
    extended_keys = []
    for title in csv_object.titles:
        key_object = Key_Model(name=title)
        extended_keys.append(key_object)
    if key_list:
        for key in key_list:
            key_object = Key_Model(name=key)
            extended_keys.append(key_object)

    #TODO: REVISAR SI METER TITLES POR DEFECTO
    csv_table = Table_Model.objects.create(
        name = csv_object.name,
        description = csv_object.description,
        titles = csv_object.titles,
        rows = csv_object.rows,
        keys = extended_keys
        )
    csv_table.save()

def get_suggested_keys(csv_table):
    pass

def add_keys(name, key_list):
    table = Table_Model.objects(name=name).first()
    keys = table.keys
    for key in key_list:
        key = Key_Model(name=key).save()
        keys.append(key)
    table.keys = keys
    table.save()