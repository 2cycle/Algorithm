

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






print(solution(3,[1,21,79],[20,30,25]))