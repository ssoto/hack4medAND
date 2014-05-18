# -*- coding: UTF-8 -*-
from lisa_modules.csv_reader import CSV
from lisa_models.table import Table_Model
from lisa_modules.db_middleware import persist_csv, get_last_created_tables, filter_tables
from lisa_modules.key_middleware import add_keys, get_all_keys,get_suggested_keys
from mongoengine import connect

def main():
    connect('project1')
    csv_object = CSV()
    csv_object.initialize('/home/alicia/hack4medAND/lisa_graph/resources/file.csv', 
                        "tabla2",
                        'Tabla con las temperaturas por provincia')
    persist_csv(csv_object,
                 ['key', 'Andalucia', 'erdogan'])

    #add_keys('NOMBRE_CSV',['HOLA', 'MUNDO'])

    for table in get_last_created_tables():
        print table.name

    print "Filtered tables:"
    for table in filter_tables(['rota']):
       print table.name

if __name__ == "__main__":
    main()