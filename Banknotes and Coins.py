value_in = round(float(input()),2)
notas = [0,0,0,0,0,0]
moeda = [0,0,0,0,0,0]

while value_in != 0.00:
    value_in = round(value_in,2)
    if value_in >= 100.00:
        notas[0]+=1
        value_in -= 100.00

    elif value_in >= 50.00:
        notas[1]+=1
        value_in -= 50.00

    elif value_in >= 20.00:
        notas[2]+=1
        value_in -= 20.00

    elif value_in >= 10.00:
        notas[3]+=1
        value_in -= 10.00

    elif value_in >= 5.00:
        notas[4]+=1
        value_in -= 5.00

    elif value_in >= 2.00:
        notas[5]+=1
        value_in -= 2.00

    elif value_in >= 1.00:
        moeda[0]+=1
        value_in -= 1.00

    elif value_in >= 0.50:
        moeda[1]+=1
        value_in -= 0.50

    elif value_in >= 0.25:
        moeda[2]+=1
        value_in -= 0.25

    elif value_in >= 0.10:
        moeda[3]+=1
        value_in -= 0.10

    elif value_in >= 0.05:
        moeda[4]+=1
        value_in -= 0.05

    elif value_in >= 0.01:
        moeda[5]+=1
        value_in -= 0.01
    else:
        value_in = 0.00

print("NOTAS:")
print("{0} nota(s) de R$ 100.00".format(notas[0]))
print("{0} nota(s) de R$ 50.00".format(notas[1]))
print("{0} nota(s) de R$ 20.00".format(notas[2]))
print("{0} nota(s) de R$ 10.00".format(notas[3]))
print("{0} nota(s) de R$ 5.00".format(notas[4]))
print("{0} nota(s) de R$ 2.00".format(notas[5]))
print("MOEDAS:")
print("{0} moeda(s) de R$ 1.00".format(moeda[0]))
print("{0} moeda(s) de R$ 0.50".format(moeda[1]))
print("{0} moeda(s) de R$ 0.25".format(moeda[2]))
print("{0} moeda(s) de R$ 0.10".format(moeda[3]))
print("{0} moeda(s) de R$ 0.05".format(moeda[4]))
print("{0} moeda(s) de R$ 0.01".format(moeda[5]))