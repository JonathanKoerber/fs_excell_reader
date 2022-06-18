from ast import arg
import os
import argparse
import openpyxl
import pandas as pd
from datetime import datetime

'''
Take consume excel doc.
add data frame dictionary keyed by day broken by day and meal
'''
meal_key = ['']
def parse(arg):
    location = arg.parse[0]
    #workbook =  openpyxl.load_workbook(location)
    excel_data = pd.read_excel(location, sheet_name='Dinner 5.23')
    #print(excel_data.iloc[0:32])
    
    for i in range(0, len(excel_data), 32):
        print('*************************')
        data = excel_data.iloc[i:i+32]
        col_0 = data.iloc[:,0]
        
        prep_serve = list(filter(lambda x: type(x) == datetime, col_0))
        print(prep_serve)
                
    print('*******************')
    

'''
main arg 
'''
 
def main():
    print('hello arg')
    parser = argparse.ArgumentParser(description='Value for files')
    parser.add_argument('-p', '--parse', type=str, nargs=1,
        metavar=('file'), help='''Add workbook''')
    arg = parser.parse_args()
    print(arg)
    if arg.parse != None:
        parse(arg)
    
if __name__ == '__main__':
    main()    
