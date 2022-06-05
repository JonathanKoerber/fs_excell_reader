from ast import arg
import os
import argparse
import openpyxl
import pandas as pd

'''
parses the args and 
'''
def parse(arg):
    location = arg.parse[0]
    #workbook =  openpyxl.load_workbook(location)
    excel_data = pd.read_excel(location, sheet_name='Dinner 5.23')
    print(excel_data)
    for sheet in excel_data:
        print(sheet)
    # sheet = workbook.active
    # for i in range(0, sheet.max_row):
    #     for col in sheet.iter_col(1, sheet.max_column):
    #         print(col[i].value, end='\t')
    #     print(' ')

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
