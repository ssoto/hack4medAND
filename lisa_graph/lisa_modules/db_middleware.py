# -*- coding: UTF-8 -*-
from lisa_modules.csv_reader import CSV
from lisa_models.table import Table_Model


def persist_csv(csv_object, key_list=None):
	csv_table = Table_Model.objects.create(
		name = csv_object.name,
		description = csv_object.description,
		titles = csv_object.titles,
		rows = csv_object.rows,
		keys = key_list
		)
	csv_table.save()

def get_suggested_keys(csv_table):
	pass

