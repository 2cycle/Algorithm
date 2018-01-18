#넓이우선탐색
#다시 풀어볼 것


cnt = 0
x=[0 for x in range(100)]
y=[0 for y in range(100)]
ll=[0 for l in range(100)]

def start(nn, mm, qq):
    global cnt
    global x
    global y
    global ll
    x[cnt] = nn
    y[cnt] = mm
    ll[cnt] = qq
    cnt += 1

def dfs(n, m ,orimap):
   pos = 0
   xx = 0
   yy = 0
   map = [[0 for col in range(m)] for row in range(n)]
   for i in orimap:
       for j in str(i):
           map[xx][yy] = int(j)
           yy += 1
       xx += 1
       yy = 0

   print("map", map)
   start(0, 0, 1)

   while (pos < cnt and ( x[pos] != m-1  or y[pos] != n-1 )):
       map[y[pos]][x[pos]] = 0

       if y[pos] > 0 and map[y[pos] -1 ][x[pos]] == 1:
           start(x[pos], y[pos] -1, ll[pos]+1)
           print("up")

       if y[pos] < n-1 and map[y[pos] + 1][x[pos]] == 1:
           start(x[pos], y[pos] + 1, ll[pos] + 1)
           print("down")

       if x[pos] > 0 and map[y[pos]][x[pos]-1] == 1:
           start(x[pos] -1, y[pos], ll[pos] + 1)
           print("left")

       if x[pos] < m-1 and map[y[pos]][x[pos]+1] == 1:
           start(x[pos] +1 , y[pos], ll[pos] + 1)
           print("right")

       pos += 1
       print("map",map)

   if pos < cnt :
       print(x)
       print(y)
       print(ll)
       print(ll[pos])



orimap = [101111,101010,101011,111011]
dfs(4,6, orimap)