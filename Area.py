line1 = input().split(" ")
pi = 3.14159
A, B, C = line1
A = float(A)
B = float(B)
C = float(C)

TRIANGULO = (A * C)/2
print("TRIANGULO: %.3f"%TRIANGULO)
CIRCULO = pi*C**2
print("CIRCULO: %.3f"%CIRCULO)
TRAPEZIO = ((A+B)*C)/2
print("TRAPEZIO: %.3f"%TRAPEZIO)
QUADRADO = B**2
print("QUADRADO: %.3f"%QUADRADO)
RETANGULO = A*B
print("RETANGULO: %.3f"%RETANGULO)