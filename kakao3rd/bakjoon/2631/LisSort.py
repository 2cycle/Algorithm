
def solution(n,value) :

    mlist = []

    for i in range(n):
        if len(mlist) == 0 or value[i] > mlist[len(mlist) -1] :
            mlist.append(value[i])
            print("mlist",mlist)
        else :
            m = 0
            print(len(mlist)-1)
            idx = len(mlist)-1
            while(m < idx):
                mid = (m + idx) // 2
                print("mid",mid)
                if mlist[mid] < value[i]:
                    m = mid + 1
                else :
                    idx = mid

            mlist[idx] = value[i]

        print(mlist)


    return print(n - len(mlist))



num = 7
value = [3,7,5,2,6,1,4]

solution(num , value)
