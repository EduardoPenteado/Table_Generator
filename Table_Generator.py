#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import random
from os import path

class Table_Generator:
    col_name = []
    
    def __init__(self):
        self.rows = int(input('Insert the number of rows on the table:'))
        self.cols = int(input('Insert the number of cols on the table: '))
        self.df = pd.DataFrame()
        
    def columns(self):
        for i in range(0, self.cols):
            col_name = [str(input('Insert the column name: '))]
            resp = str(input('The Data is numeric? [Y/N]')).upper()
            if resp == 'YES' or resp == 'Y':
                col_value_lower = int(input('Insert the lower value: '))
                col_value_higher = int(input('Insert the higher value: '))
                values = [random.randrange(col_value_lower, col_value_higher+1) for _ in range(0, self.rows)]
                self.DataFrame(values, col_name, i)
            else:
                print('Insert the values in the value\n'+'Insert quit to leave!')
                col_value = input()
                col_list = []
                while col_value != 'quit':
                    col_list.append(col_value)
                    print(col_value+' added.')
                    col_value = input()
                values = [col_list[random.randrange(0, len(col_list))] for _ in range(0, self.rows)]
                self.DataFrame(values, col_name, i)  
        
    def DataFrame(self, values, col_name, index):
        try:
            self.df = pd.concat([self.df, pd.DataFrame(values, columns = col_name)], axis=1, sort=False)
        except UnboundLocalError:
            self.df = pd.DataFrame(data=values, columns = col_name)
        if index == self.cols-1:
            print(self.df)
            self.Save_to_excel()
    
    def Save_to_excel(self):
        print('Saving Table_generator ...')
        self.df.to_excel('Table_generator.xlsx')
        dir_path = path.dirname(path.realpath("Table_generator.xlsx"))
        print('Table_generator as been saved in '+dir_path)
        
if __name__ == '__main__':
    table = Table_Generator()
    table.columns()

