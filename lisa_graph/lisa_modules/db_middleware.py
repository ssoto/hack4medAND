# -*- coding: UTF-8 -*-
from lisa_modules.csv_reader import CSV
from lisa_models.table import Table_Model
from lisa_models.key import Key_Model
from django.template.defaultfilters import slugify
from mongoengine import connect

from lisa_modules.real_table_middleware import save_table

connect('lisa_project_db')

def persist_csv(csv_object, key_list=[]):
    extended_keys = []
    if key_list:
        key_list += csv_object.titles
    else:
        key_list  = csv_object.titles

    for title in key_list:
        title = slugify(title)
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
        keys = extended_keys,
        row_types = csv_object.row_types
    )
    csv_table.save()
    # y guardamos las tablas con datos
    save_table(csv_table.name)


def get_last_created_tables():
    return Table_Model.objects.order_by('-creation_date').limit(5)
 
def filter_tables(key_list):
    key_tables = []
    for key in key_list:
        key_object = Key_Model.objects(name=slugify(key)).first()
        key_tables.append(Table_Model.objects.filter(keys__contains=key_object))
    iterating_tables = key_tables[0]
    filtered_table = []
    for table in iterating_tables:
        is_in_all=True
        for tables_array in key_tables:
            if not table in tables_array:
                is_in_all = False
                break
        if is_in_all:
            filtered_table.append(table)
    return filtered_table
