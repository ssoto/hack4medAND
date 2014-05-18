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
                        "meteorologia_cordoba",
                        'Datos meteorológicos de Córdoba')
    persist_csv(csv_object,
                 ['cordoba', 'Andalucia', 'temperatura', 'humedad', 'meteorologia', 'estaciones'])

    csv_object.initialize('/home/alicia/hack4medAND/lisa_graph/resources/estaciones.csv',
                        "estaciones_meteorologicas",
                        'Localización de las estaciones meteorologicas de Andalucia')
    persist_csv(csv_object,
                ['cordoba', 'cadiz', 'sevilla', 'huelva', 'almeria', 'meteorologia', 'estaciones' ])

    csv_object.initialize('/home/alicia/hack4medAND/lisa_graph/resources/datos_estaciones_almeria.csv',
                        "meteorologia_almeria",
                        "Datos metorologicos de Almería")
    persist_csv(csv_object,
                ["almeria", "andalucia", "temperatura", "humedad", "meteorologia", "estaciones"])
    #add_keys('NOMBRE_CSV',['HOLA', 'MUNDO'])

    for table in get_last_created_tables():
        print table.name

    print "Filtered tables:"
    for table in filter_tables(['cadiz']):
       print table.name

if __name__ == "__main__":
    main()