line1 = input().split(" ")
y,x = line1
y,x = int(y), int(x)
price = [0,4.00 ,4.50 ,5.00 ,2.00 ,1.50]

total = price[y]*x


print("Total: R$ %.2f"%total)