count = 0
fo = open("foo.txt", "w")
for i in range(0, 100000):
    list = []
    a, b, c, d, e = 0, 0, 0, 0, 0
    e = i % 10
    i = i // 10
    d = i % 10
    i = i // 10
    c = i % 10
    i = i // 10
    b = i % 10
    i = i // 10
    a = i % 10
    i = i // 10
    list.append(a)
    list.append(b)
    list.append(c)
    list.append(d)
    list.append(e)
    list.sort()
    summ = sum(list)
    maxx = max(list)
    minn = min(list)
   
    if (abs(maxx - minn) >= 7):
        count = count + 1
        res = e + 10*d + 100*c + 1000*b + 10000*a
        ss = str(res)
        ans = ""
        l = len(ss);
        if (l == 1):
            ans = "0000" + ss
        if (l == 2):
            ans = "000" + ss
        if (l == 3):
            ans = "00" + ss
        if (l == 4):
            ans = "0" + ss
        if (l == 5):
            ans = ss   
        ans = ans + ','  
        fo.write(ans)

print(count)