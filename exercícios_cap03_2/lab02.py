# Calculadora em Python

print("***** CALCULADORA EM PYTHON *****")
pn = 0
sn = 0
total = 0

def opcoes():
    while True:
        try:
            print(" 1 - Soma \n", "2 - Subtração \n", "3 - Multiplicação \n", "4 - Divisão \n")
            o = int(input("Selecione o número da opção desejada: "))

            if o == 1:
                pn = float(input("Digite o primeiro número: "))
                sn = float(input("Digite o segundo número : "))

                total = pn + sn

                print("------------------------------------------------")
                print("Seu resultado: ", "%d + %d = %d" %(pn, sn, total))

            if o == 2:
                pn = float(input("Digite o primeiro número: "))
                sn = float(input("Digite o segundo número : "))

                total = pn - sn

                print("------------------------------------------------")
                print("Seu resultado: ", "%d - %d = %d" %(pn, sn, total))

            if o == 3:
                pn = float(input("Digite o primeiro número: "))
                sn = float(input("Digite o segundo número : "))

                total = pn * sn

                print("------------------------------------------------")
                print("Seu resultado: ", "%d * %d = %d" %(pn, sn, total))

            if o == 4:
                pn = float(input("Digite o primeiro número: "))
                sn = float(input("Digite o segundo número : \n"))

                total = pn / sn

                print("------------------------------------------------")
                print("Seu resultado: ", "%d / %d = %d" %(pn, sn, total))
        except:
            print("ERRO")
            print("Deseja rodar novamente?")
            c = int(input("1 - SIM   2-NÃO\n"))

            if c == 1:
                continue
            if c == 2:
                break


opcoes()
