line1 = input().split(" ")
line2 = input().split(" ")

cod_prod1, unit_prod1, value_prod1 = line1
cod_prod2, unit_prod2, value_prod2 = line2

Value_to_pay = (int(unit_prod1) * float(value_prod1))+(int(unit_prod2) * float(value_prod2))

print("VALOR A PAGAR: R$ %.2f" % Value_to_pay)