line1 = input().split(" ")

A, B, C = line1
A = int(A)
B = int(B)
C = int(C)

maior = A
if B > maior:
    maior = B
if C > maior:
    maior = C

print("%d eh o maior"%maior)