import pandas as pd

def getNumericData(URL):
    dataFrameList = pd.read_html(URL, encoding='CP1251')
    header = dataFrameList[6].drop(12).T
    data = dataFrameList[7].drop(12).T
    header[0]='Номер УИК'
    data.columns=header.iloc[1]
    data.reset_index()
    for f in range(1,12):
        newint=[]
        for i in data.iloc[:,f]:
            newint.append(int(i))
        data.iloc[:,f]=newint
    for j in range(12,15):
        count=[]
        pro=[]
        for i in data.iloc[:,j]:
            i = i.replace("%","")
            i = i.replace("'","")
            i = i.split()
            count.append(int(i[0]))
            pro.append(float(i[1]))
        data.iloc[:,j]=count
        data['% '+ str(data.columns.values[j])] = pro
    n = []
    ni = []
    for i in range(data.shape[0]):
        n.append(int(data.iloc[i,3]+data.iloc[i,4]))
    data['Явка'] = n
    for i in range(data.shape[0]):
        ni.append(float(round(data.iloc[i,18]/data.iloc[i,1]*100, 2)))
    data['% Явка'] = ni
    return data
