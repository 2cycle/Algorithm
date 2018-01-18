import sys

def solution (nm , mvOrder):

    maxV=int(nm[0])
    mList = list(range(1,maxV+1))
    res = ''

    for i in range(nm[1]):
        res = res + str(mList.index(mvOrder[i])) + ' '
        mList.insert(0,mList.pop(mList.index(mvOrder[i])))

    return print(res);




#
# times = int(input("times : "))
# nm = input("nm : ")
# mvOrder = input("Movie order : ")


times = 1
nm = "5 3"
mvOrder = "4 4 5"

for i in range (times):
    solution(list(map(int, nm.split())),list(map(int, mvOrder.split())))