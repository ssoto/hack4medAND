# -*- coding: UTF-8 -*-
from lisa_modules.csv_reader import CSV
from lisa_models.table import Table_Model
from lisa_modules.db_middleware import persist_csv
from lisa_modules.key_middleware import add_keys, get_all_keys,get_suggested_keys

if __name__ == "__main__":
    from mongoengine import connect
    connect('project1')
    csv_object = CSV()
    csv_object.initialize('/home/alicia/hack4medAND/lisa_graph/resources/file.csv', 
    					'andalucia temperatura',
     					'Tabla con las temperaturas por provincia')
    persist_csv(csv_object,
                 ['key', 'andalucia'])
    for key in get_suggested_keys('andalucia temperatura'):
    	print key.name
    #add_keys('NOMBRE_CSV',['HOLA', 'MUNDO'])