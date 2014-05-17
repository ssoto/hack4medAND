# -*- coding: UTF-8 -*-
from lisa_modules.csv_reader import CSV
from lisa_models.table import Table_Model
from lisa_models.key import Key_Model

def persist_csv(csv_object, key_list=None):
    
    extended_keys = []
    key_list+=csv_object.titles
    for title in key_list:
        key_object = Key_Model.objects(name=title).first()
        if not key_object:
            key_object = Key_Model(name=title).save()
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
