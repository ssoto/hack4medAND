# -*- coding: UTF-8 -*-
from lisa_modules.csv_reader import CSV
from lisa_models.table import Table_Model
from lisa_models.key import Key_Model

def get_suggested_keys(table_name):
    suggested_keys = []
    table = Table_Model.objects(name=table_name).first()
    for key in get_all_keys():
        key_name = key.name
        table_description = table.description
        if key_name in (table_name+table_description):
            suggested_keys.append(key)
    return suggested_keys


def add_keys(name, key_list):
    table = Table_Model.objects(name=name).first()
    keys = table.keys
    for key in key_list:
        key = Key_Model.objects(name=key).first()
        if not key_object:
            key_object = Key_Model(name=title).save()
        keys.append(key)
    table.keys = keys
    table.save()

def get_all_keys():
    return Key_Model.objects()