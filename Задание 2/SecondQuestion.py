import re
from datetime import datetime

def judge(a,b):
    if a==b:
        return int(1)
    elif a!=b:
        return int(0)

DIR = "file2.csv"
file = open(DIR, 'r')
arr = []
i=0
x=0
y=0
for line in file:
    print(x)
    x+=1
    SpLine = re.split(r'\t+', line.rstrip('\t|\n'))
    logIn = SpLine[0]
    Id = SpLine[1]
    docId = SpLine[2]
    jud = SpLine[3]
    cjud = SpLine[4]
    if arr == []:
        arr.append(SpLine)
    else:
        for i in range(len(arr)):

            if SpLine[0] in arr[i][0]:
                arr[i][2] = arr[i][2]+judge(jud,cjud)
                arr[i][3]= arr[i][3]+1
                Counter = 0
                # arr.append([logIn, Id, str(judgment), arr[i][3]+1])
                Check = True
                break
            else:
                Check = False
        if Check==False:
            arr.append([logIn,Id,judge(jud,cjud),0])
for s in range(len(arr)):
    if s != 0:
        ProcOfTrue = (int(arr[s][2])/int(arr[s][3]))*100
        arr[s].append(ProcOfTrue)
del arr[0]
arr.sort(key = lambda x:x[4], reverse=True)
f = open('result1.csv', 'w')
for i in range(len(arr)):
    f.write(f'Логин: {arr[i][0]} |Id:{arr[i][1]} |Количество корректно выполненных заданий:{arr[i][2]} |Количество заданий: {arr[i][3]} |Процент выполнения : {arr[i][4]} \n')
f.close()
print(arr)
file.close()



