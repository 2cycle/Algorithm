




def solution(E,S,M):
    e = s = m = 1
    cnt = 0
    while (not(e == E & s == S & m == M)):

       if e == E:
            e = 1
       if s == S:
            s = 1
       if m == M:
            m = 1


    #        if (e == E & s == S & m == M):
    #        break





ESMList = [[1,16,16],[1,1,1],[1,2,3],[15,28,19]]
for i in range(len(ESMList)):
    print(solution(ESMList[i][0],ESMList[i][1],ESMList[i][2]))