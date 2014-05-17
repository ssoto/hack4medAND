# -*- coding: UTF-8 -*-
from lisa_modules.csv_reader import CSV
from lisa_models.table import Table_Model


def persist_csv(csv_object, key_list=None):
    extended_keys = csv_object.titles
    if key_list:
        extended_keys += key_list
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

def add_keys(key_list):
    # nombre 
    pass

