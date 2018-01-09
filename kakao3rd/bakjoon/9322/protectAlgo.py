

def solution(case,test):
    result = []
    for i in range(case):
        dic = {}
        list = []
        iter = test[i][0]
        fst = test[i][1].split(" ")
        snd = test[i][2].split(" ")
        pw = test[i][3].split(" ")
        print(fst,snd,pw)
        for i in range(iter):
            temp = fst.index(snd[i])
            dic[temp] =  pw[i]
        for k,v in sorted(dic.items()):
            list.append(v)
        result.append(' '.join(list))
    return result



case = 2
test = [[4,"A B C D","D A B C","C B A P"],[3,"SECURITY THROUGH OBSCURITY","OBSCURITY THROUGH SECURITY","TOMORROW ATTACK WE"]]
print(solution(2,test))

"""
n = 4
F = "A B C D"
S = "D A B C"
PW = "C B A P"
3
SECURITY THROUGH OBSCURITY
OBSCURITY THROUGH SECURITY
TOMORROW ATTACK WE

"""
