import csv
import os

DIR = 'data/'
fname = 'AwardsManagers.csv'
fpath = DIR+fname


## 另外一个读取数据的方法是用DictReader
names = ['messageID','userID','user','screen','turnID','message','URL','sorce','imageURL','voiceURL','videoURL','gps','turntimes','comments','agree','time']
with open(fpath) as csvfile: 
    ## fieldnames指明了csv文件的列名称   
    reader = csv.DictReader(csvfile, fieldnames=names, 
        delimiter=',', quotechar='|')     
    for row in reader: 
        row = (row[0],row[5],row[13],row[14],row[15],row[16])
    return row

def __init__(self):
    self.current_dir = os.getcwd()
    
def process_row(self,startmp,endtmp,row):
    endtmp = 1481295600
    startmp = 1480690800
    dir_path = self.current_dir + '/result/' 
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    result_file_path = dir_path + '/' + startmp + '.txt'
    
    if os.path.exists(result_file_path) and os.path.isfile(result_file_path):
        print'-------------------'
        print startmp + '.txt exists, not overriden'
        print '-----------------------'
        return startmp



    
    if (endtmp >= row[16] > startmp):
        f=open(startmp +'.txt','a')
        f.write(row)
        f.close()
        endtmp = startmp 
        startmp-= 604800
            
        ## 每一行都是一个dict对象
       