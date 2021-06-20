value_in = int(input())
value = value_in
notas = [0,0,0,0,0,0,0]

while value_in != 0:
    if value_in >= 100:
        notas[0]+=1
        value_in -= 100

    elif value_in >= 50:
        notas[1]+=1
        value_in -= 50

    elif value_in >= 20:
        notas[2]+=1
        value_in -= 20

    elif value_in >= 10:
        notas[3]+=1
        value_in -= 10

    elif value_in >= 5:
        notas[4]+=1
        value_in -= 5

    elif value_in >= 2:
        notas[5]+=1
        value_in -= 2

    elif value_in >= 1:
        notas[6]+=1
        value_in -= 1

print("{0}".format(value))
print("{0} nota(s) de R$ 100,00".format(notas[0]))
print("{0} nota(s) de R$ 50,00".format(notas[1]))
print("{0} nota(s) de R$ 20,00".format(notas[2]))
print("{0} nota(s) de R$ 10,00".format(notas[3]))
print("{0} nota(s) de R$ 5,00".format(notas[4]))
print("{0} nota(s) de R$ 2,00".format(notas[5]))
print("{0} nota(s) de R$ 1,00".format(notas[6]))