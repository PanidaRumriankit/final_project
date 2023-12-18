# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import copy
import csv
import secrets



# add in code for a Database class
class DB:
    def __init__(self):
        self.database = []

    def insert(self, table):
        self.database.append(table)

    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None



    # def entry(self):
    #     for table in self.database:
    #         if table.table_name == table_name:
    #             return table
    #     return None


# add in code for a Table class


class Table:
    def __init__(self, table=[], table_name=''):
        self.table_name = table_name
        self.table = table
        self.key = {}

    def join(self, other_table, common_key):
        joined_table = Table(self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def filter(self, condition):
        filtered_table = Table(self.table_name + '_filtered', [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def aggregate(self, function, aggregation_key):
        temps = []
        for item1 in self.table:
            temps.append(float(item1[aggregation_key]))
        return function(temps)

    def select(self, attributes_list):
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps

    def add(self, ins):
        self.table.append(ins)
        safe = secrets.token_urlsafe(16)
        self.key[safe] = len(self.table) - 1
        # if len(key) != 0:
        #     self.key[key] = len(self.table) - 1

    def update(self, new, key):
        self.table[self.key[key]] = new

    def insert_by_csv(self, file, name):
        f = open(file, 'r')
        reader = csv.DictReader(f)
        saving = []
        for num, dic in enumerate(reader):
            # store = list()
            # store.append(dic)
            saving.append(dic)
            safe = secrets.token_urlsafe(16)
            self.key[safe] = num
            # print(self.key)
        self.table = saving
        self.table_name = name
        return self

    def __str__(self):
        return self.table_name + ':' + str(self.table)


# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary


# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated
#
# my_DB = DB
# table = Table()
# table.insert_by_csv('persons.csv', 'persons')
# print('name ', table.table_name)
# print('table ', table.table)
# print('key ', table.key)


