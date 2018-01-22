import sys

def solution(N , mHp , pJoy):

    hp = 100
    joy = 0

    for i in range(N):
        dp = []
        if i == 0:
            dp.append(pJoy[i])
        elif i == 1 & hp[i] + hp[i-1] < 100:
            dp.append(pJoy[i] + pJoy[i-1])
        elif hp[i]:
            dp.append(ma)


        if(hp - mHp[i] >= 0):
            hp = hp - mHp[i]
            joy = joy + pJoy[i]
        else :
            break

    return joy;

def getmax(capacity, index):
    ret = 0
    if index == n :
        return 0
    unselected = getmax(capacity,index+1)
    selected = 0
    if capacity >= weight[index]:
        select = getmax(capacity-weight[index],index+1) + value[index]
    return max


def sol(N , mHp , pJoy):
    dp = []
    for i in range(N):
        for j in range(100):
            dp[j] = max(dp[j],dp[j-1])




n = 3
weight = map(int,input().split())
value = map(int,input().split())
capacity = 99
index = 0

print(solution(3,[1,21,79],[20,30,25]))