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

