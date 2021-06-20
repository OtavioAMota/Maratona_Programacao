N = int(input())
time = [0,0,0]

while N != 0:
    if N >= 3600:
        time[0]+=1
        N -= 3600

    elif N >= 60:
        time[1]+=1
        N -= 60

    elif N >= 1:
        time[2]+=1
        N -= 1


print("{0}:{1}:{2}".format(time[0],time[1],time[2]))