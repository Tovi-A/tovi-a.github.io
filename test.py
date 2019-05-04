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
    m1 = list[0] + list[1]
    m2 = list[0] + list[2]
    m3 = list[0] + list[3]
    m4 = list[0] + list[4]
    m5 = list[1] + list[2]
    m6 = list[1] + list[3]
    m7 = list[1] + list[4]
    m8 = list[2] + list[3]
    m9 = list[2] + list[4]
    m10 = list[3] + list[4]
    left = 3
    right = 4
    if (not((m1 >= left and m1 <= right) or (m2 >= left and m2 <= right) or (m3 >= left and m3 <= right) or \
        (m4 >= left and m4 <= right) or(m5 >= left and m5 <= right) or (m6 >= left and m6 <= right) or \
            (m7 >= left and m7 <= right) or (m8 >= left and m8 <= right) or (m9 >= left and m9 <= right) or \
                (m10 >= left and m10 <= right))):
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