n1,n2,n3,n4 = line1 = input().split(" ")
media = (float(n1)*2+float(n2)*3+float(n3)*4+float(n4))/10
print("Media: %.1f"%media)
if media >= 7.0 :
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
    print("Aluno em exame.")
    nEx = float(input())
    MediaF = (media+nEx)/2
    print("Nota do exame: {}".format(nEx))
    if MediaF >= 5.0:
        print("Aluno aprovado.")
    elif MediaF < 5.0:
        print("Aluno reprovado.")
    print("Media final: %.1f"%MediaF)
