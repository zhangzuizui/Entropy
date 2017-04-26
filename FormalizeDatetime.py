import pandas as pd
import os
import math
import datetime

def FormalizedDatetime(aStr, time_interval=3):
    
    if type(aStr) != str:
        raise ValueError('the first argument is a str')
    if type(time_interval) != int:
        raise ValueError('the second argument is an int')
    
    temp = aStr.replace('-', '').replace(' ', '')
    tl = list(temp)
    if tl[3].encode('gbk') != b'\xd4\xc2':
        raise ValueError('month error')
    DD = int(tl[0] + tl[1])
    MM = int('0' + tl[2])
    YY = int('20' + tl[4] + tl[5])
    HH = tl[-4] + tl[-3]
    if tl[-2].encode('gbk') == b'\xcf\xc2':
        HH = math.floor((int(HH)+12)/time_interval) * time_interval
        if HH == 24:
            HH = 0
    else:
        HH = math.floor(int(HH)/time_interval) * time_interval
    time_window = datetime.datetime(year=YY, month=MM, day=DD, hour=HH, minute=0, second=0)
    
    return time_window

def GetTimeWindow(aDatetime, time_interval=3):
    
    try:
        op_time = datetime.datetime.strptime(aDatetime, '%Y/%m/%d %H:%M:%S')
    except:
        return 0
        
    op_time_hour = math.floor(op_time.hour / time_interval) * time_interval
    op_time = datetime.datetime(year=op_time.year, month=op_time.month, day=op_time.day,
                                hour=op_time_hour, minute=0, second=0)
    
    return op_time
    
    
    

path = os.getcwd() + '/' + 'time_preference'
#filename = 'against_like.csv'
#against_like = pd.read_csv(path+'/'+filename, encoding='gbk', dtype=str)
#against_like['OP_TIME'] = against_like['OP_TIME'].apply(FormalizedDatetime)
#against_like.to_csv(path+'/'+filename)

filename = 'resource.csv'
login_visit = pd.read_csv(path+'/'+filename, dtype=str)
login_visit['OP_TIME'] = login_visit['OP_TIME'].apply(GetTimeWindow)
login_visit = login_visit[login_visit['OP_TIME']!=0]
login_visit.reindex(index=list(range(len(login_visit))))
login_visit.to_csv(path+'/'+filename)

