# -*- coding: UTF-8 -*-
from lisa_modules.csv_reader import CSV
from lisa_models.table import Table_Model
from lisa_modules.db_middleware import persist_csv

if __name__ == "__main__":
	from mongoengine import connect
	connect('project1')
	csv_object = CSV()
	csv_object.initialize('/home/alicia/hack4medAND/lisa_graph/resources/file.csv', 'NOMBRE_CSV', 'CSV MOLÓN!')
	persist_csv(csv_object)
