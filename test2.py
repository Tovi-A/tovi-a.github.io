count = 0
fo = open("foo.txt", "w")
for i in range(0, 100):
    list = []
    a, b, c, d, e = 0, 0, 0, 0, 0
    e = i % 10
    i = i // 10
    d = i % 10
    
    
    
    list.append(e)
    list.append(d)
    
    list.sort()
    flag = 0
    maxx = max(list)
    minn = min(list)
    
    if ((maxx - minn <= 5) and (maxx - minn > 1)):
        count = count + 1
        res = e + 10*d
        ss = str(res)
        ans = ""
        l = len(ss);
        if (l == 1):
            ans = "0" + ss
        if (l == 2):
            ans = ss
        
          
        ans = ans + ','  
        fo.write(ans)

print(count)