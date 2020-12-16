nf = int(input("Qual o número do funcionário? "))
nh = int(input("Número de horas trabalhadas? "))
vph = float(input("Salário recebido por hora: "))

x = vph*nh

print("NUMBER = ", nf)
print("SALARY = U$ ", "%.2f" % x)