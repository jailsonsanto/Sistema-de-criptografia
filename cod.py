s = input("diga uma palavra:" )
v = int (ord(s))
n = 0
n2 = 0
if v <= 127:
    n = v - 47
    print("%s =  %d"%(chr(n),n))

    
s1 = input("diga uma palavra:" )
v1 = int (ord(s))
n1 = 0

if v1 >= 127:
    n1 = v1 + 47
    print("%s =  %d"%(chr(n1),n1))


    
'''
for c in range(33,127):
    print("%s =  %d"%(chr(c),c))
'''
