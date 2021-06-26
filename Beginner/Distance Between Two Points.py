line1 = input().split(" ")
line2 = input().split(" ")

x1, y1 = line1
x2, y2 = line2
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
Distance = ((x2-x1)**2+(y2-y1)**2)**(1/2)

print("%.4f"%Distance)