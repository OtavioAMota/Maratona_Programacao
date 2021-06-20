N = int(input())
time = [0,0,0]

while N != 0:
    if N >= 365:
        time[0]+=1
        N-=365
    elif N >= 30:
        time[1]+=1
        N-=30
    elif  N >= 1:
        time[2]+=1
        N-=1
    
print("{0} ano(s)".format(time[0]))
print("{0} mes(es)".format(time[1]))
print("{0} dia(s)".format(time[2]))