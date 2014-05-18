# -*- coding: UTF-8 -*-

import datetime
from mongoengine import *
import time
import sys
from time import strptime
import traceback

from lisa_models.table import Table_Model
from lisa_models.dynamicTable import DynamicTable

def create_value(string_value, string_type):
    try:
        strptime(string_value,'%d/%m/%Y')
        result = datetime.datetime.strptime(string_value, "%d/%m/%Y")
    except ValueError:
        try:
            result = int(string_value)
        except ValueError:
            try:
                result = float(string_value)
            except ValueError:
                try:
                    result = float(string_value.replace(",", "."))
                except ValueError:
                    result = string_value
    return result

def persist_table(table):
    rows = []
    for row in table.rows:
        result = {}
        for index in range(len(table.titles)):
            row_title = table.titles[index]
            
            string_value = row[index]
            truth_value = create_value(string_value,
                                      table.row_types[row_title])
            result[row_title] = truth_value
        rows.append(result)
        result = {}
    doc = DynamicTable.objects.create(rows=rows)
    doc.save()


def save_table(table_name):
    query_set = Table_Model.objects(name=table_name)
    if len(query_set) != 0:
        return None
    else:
        persist_table(query_set.first())

def get_table(table_name):
    query_set = Table_Model.objects(name=table_name)
    if len(query_set) == 0:
        return None
    else:
        return query_set.first()