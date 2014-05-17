# -*- coding: UTF-8 -*-
#CSV_Reader for LISA

import csv as ecsv

class CSV:
    def __init__(self):
        pass

    def initialize(self, path_to_file, name, description):
        #TO-DO: check that the file exists
        ifile = open(path_to_file, "rb")
        reader = ecsv.reader(ifile)
        rows_list= []
        for row in reader:
            rows_list.append(row)        
        ifile.close()
        self.name = name
        self.description = description
        self.titles = rows_list[0]
        self.rows = rows_list[1:]



