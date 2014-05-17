# -*- coding: UTF-8 -*-
#CSV_Reader for LISA

from time import strptime

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

    def __get_row_types(self, titles, example_row):
        result = {}
        for index in range(0,len(titles)):
            result[index] = _get_type(example_row[index])
        return result

    def _get_type(self, str_to_parse):
        try:
            result = strptime(str_to_parse,'%d/%m/%Y')
        except ValueError:
            try:
                result = int(str_to_parse)
            except ValueError:
                try:
                    result = float(str_to_parse)
                except ValueError:
                    result = str_to_parse
        return (type(result), result)




if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        sys.exit(1)
    path_to_file=sys.argv[1]
    name = sys.argv[2]
    description=sys.argv[3]

    my_csv = CSV()
    my_csv.initialize(  path_to_file,
                        name,
                        description)

    print my_csv.name, my_csv.titles, len(my_csv.rows)

