两个csv文件(1.csv 2.csv)，第一个有 100万行数据左右，第二个30万行数据，它们有两个相同的列标，我想同时匹配这两列字符串，如果1的这两个字符串和2的内容相同，则把1中这一行数据筛选下来。有什么高效的算法吗？怎么做？ 谢谢！
import pandas as pd
df1 = pd.read_csv('1.csv')
df2 = pd.read_csv('2.csv')

idx_for_df1 = df1['列标'].isin(df2['列标']) # 使用DataFrame.isin 筛选列标字符一样的行
df_final = df1[idx_for_df1] # df_final 是你想要的结果



#-*- coding:utf-8 -*-
import csv
DIR = 'data/'
fname = 'AwardsManagers.csv'
fpath = DIR+fname

## 用 with open() as filename 的结构非常优美, 而且不需要写代码来关文件
## 省去了fileobj.close(), 省去写try-finally的麻烦来出来exception

with open(fpath, 'rb') as csvfile: 
    ## delimiter是csv文件每行中数据间隔开的符号，常用是comma逗号，
    ## quotechar之间包括特殊字符
    mreader = csv.reader(csvfile, delimiter=',', quotechar='|') 

    ## 读出每一行都是一个list
    first_row = mreader.next()
    print first_row
    print type(first_row)
    ## 目前的行数
    print mreader.line_num
    for row in mreader:  
        print ', '.join(row) 

## 另外一个读取数据的方法是用DictReader
names = ['playerID','awardID','yearID','lgID','tie','notes']
with open(fpath) as csvfile: 
    ## fieldnames指明了csv文件的列名称   
    reader = csv.DictReader(csvfile, fieldnames=names, 
        delimiter=',', quotechar='|')     
    for row in reader:   
        ## 每一行都是一个dict对象
        print row[names[0]], row[names[1], row[names[2]
        
        
        
#-*- coding:utf-8 -*-
import xlrd

DIR = 'C:/Users/Lucas/Downloads/'
fname = '33010do001_2009.xls'

# 首先建立workbook
mworkbook = xlrd.open_workbook(DIR+fname)

# 打印出所有sheetnames
sheet_names = mworkbook.sheet_names()
print('Sheet Names', sheet_names)

# 选取第二个sheet
msheet = mworkbook.sheet_by_name(sheet_names[1])

# 或者通过index得到sheet
nsheet = mworkbook.sheet_by_index(1)
print ('Sheet name: %s' % nsheet.name)

# Pull the first row by index
row = msheet.row(0)  

# Pull the first row by index
row = msheet.row(4) 
# Print 1st row values and types
for cell in row:
    print cell.value

# Print all values, iterating through rows and columns
#
num_cols = msheet.ncols   # Number of columns
num_rows = msheet.nrows   # Number of rows
for row_idx in range(0, num_rows):    # Iterate through rows
    row_values = []
    for col_idx in range(0, num_cols):  # Iterate through columns
        row_values.append([msheet.cell(row_idx, col_idx).value])

    ## 输出每行数据
    print row_values

## 用col_slice得到某一列的数据
col_cells = msheet.col_slice(2, 4, num_rows)
for cell in col_cells:
    print("-"*6)
    print cell.value
        
## 用col_valeus得到某一列的数据
col_values = msheet.col_values(2, 4, num_rows)
print col_values        