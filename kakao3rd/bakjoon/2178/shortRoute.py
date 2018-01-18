#넓이우선탐색
#다시 풀어볼 것


cnt = 0
x=list(range(100))
y=list(range(100))
ll=list(range(100))

def start(xpos, ypos, count):
    global cnt
    global x
    global y
    global ll
    x[cnt] = xpos
    y[cnt] = ypos
    ll[cnt] = count
    cnt = cnt + 1

def solution(n, m ,orires):
   idx = 0
   xIndex = 0
   yIndex = 0
   res = [[0 for col in range(m)] for row in range(n)]
   for i in orires:
       for j in str(i):
           res[xIndex][yIndex] = int(j)
           yIndex += 1
       xIndex += 1
       yIndex = 0
   print("res", res)
   start(0, 0, 1)
   while (idx < cnt and ( x[idx] != m-1  or y[idx] != n-1 )):
       res[y[idx]][x[idx]] = 0
       if y[idx] > 0 and res[y[idx] -1 ][x[idx]] == 1:
           start(x[idx], y[idx] -1, ll[idx]+1)
       if y[idx] < n-1 and res[y[idx] + 1][x[idx]] == 1:
           start(x[idx], y[idx] + 1, ll[idx] + 1)
       if x[idx] > 0 and res[y[idx]][x[idx]-1] == 1:
           start(x[idx] -1, y[idx], ll[idx] + 1)
       if x[idx] < m-1 and res[y[idx]][x[idx]+1] == 1:
           start(x[idx] +1 , y[idx], ll[idx] + 1)

       idx += 1
       print("res",res)

   if idx < cnt :
       print(x)
       print(y)
       print(ll)
       print(ll[idx])



map = [101111,101010,101011,111011]
solution(4,6, orires)