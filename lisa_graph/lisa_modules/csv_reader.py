# -*- coding: UTF-8 -*-
#CSV_Reader for LISA

from time import strptime

import csv as ecsv

class CSV:
    def __init__(self):
        pass

    def initialize(self, path_to_file, name, description):
        #TO-DO: check that the file exists
        all_rows = self.__get_all_rows(path_to_file)
        titles = all_rows[0]
        data_rows = all_rows[1:]
        # get types
        self.row_types =    self.__get_row_types(titles,data_rows[1])
        print self.row_types
        self.name =         name
        self.description =  description
        self.titles =       titles
        self.rows =         data_rows

    def __get_all_rows(self, path_to_file):
        ifile = open(path_to_file, "rb")
        reader = ecsv.reader(ifile)
        rows_list= []
        for row in reader:
            rows_list.append(row)
        ifile.close()
        return rows_list

    ## Return a dictionary with:
    #   colum name => type
    def __get_row_types(self, titles, example_row):
        result = {}
        for index in range(0,len(titles)):
            row_name = titles[index]
            result[row_name] = self.__get_type(example_row[index])
        return result

    def __get_type(self, str_to_parse):
        try:
            result = strptime(str_to_parse,'%d/%m/%Y')
        except ValueError:
            try:
                result = int(str_to_parse)
            except ValueError:
                try:
                    result = float(str_to_parse)
                except ValueError:
                    try:
                        result = float(str_to_parse.replace(",", "."))
                    except ValueError:
                        result = str_to_parse
        return str(type(result))