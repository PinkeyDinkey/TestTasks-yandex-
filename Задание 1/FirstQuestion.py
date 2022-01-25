import re
from datetime import datetime

DIR = "File1.txt"
file = open(DIR, 'r')
arr = []
anoArray = []
i=0
x=0
for line in file:
    print(x)
    x+=1
    SpLine = re.split(r'\t+', line.rstrip('\t|\n'))
    if arr == []:
        arr.append(SpLine)
        anoArray.append(SpLine)
    else:
        for i in range(len(arr)):
            if SpLine[0] in arr[i][0]:
                microtasks = arr[i][2]
                oldAssignedTime = datetime.strptime(arr[i][3], '%Y-%m-%d %H:%M:%S')
                newAssignedTime = datetime.strptime(SpLine[3], '%Y-%m-%d %H:%M:%S')
                oldTclosetTime = datetime.strptime(arr[i][4], '%Y-%m-%d %H:%M:%S')
                newTclosetTime = datetime.strptime(SpLine[4], '%Y-%m-%d %H:%M:%S')
                hours_difference = abs(newAssignedTime - newTclosetTime).total_seconds() / 3600.0
                anoArray.append([SpLine[0],SpLine[2],hours_difference, float(SpLine[2])/hours_difference])
                if newAssignedTime<oldAssignedTime:
                    arr[i][3]=str(newAssignedTime)
                if newTclosetTime>oldTclosetTime:
                    arr[i][4]=str(newTclosetTime)
                arr[i][2]=str(float(arr[i][2])+float(SpLine[2]))
                Check = True
                break
            else:
                Check = False
        if Check==False:
            arr.append(SpLine)
file.close()
f = open('result1.txt', 'w')
for i in range(len(arr)-1):
    hours_difference = abs(datetime.strptime(arr[i+1][3], '%Y-%m-%d %H:%M:%S') - datetime.strptime(arr[i+1][4], '%Y-%m-%d %H:%M:%S')).total_seconds() / 3600.0
    f.write(f'Логин: {arr[i+1][0]} |Количество выполненных микрозаданий:{arr[i+1][2]} |В период с:{arr[i+1][3]} по {arr[i+1][4]} , время в часах: {hours_difference} \n')
f.close()
f = open('result2.txt', 'w')
for i in range(len(anoArray)-1):
    f.write(f'Логин: {anoArray[i+1][0]}|Количество выполненных микрозаданий:{anoArray[i+1][1]} |Время выполнения(в часах): {anoArray[i+1][2]} |Скорость выполнения(микрозадание в час):{anoArray[i+1][3]} \n')
f.close()