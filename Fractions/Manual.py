from Maths import Maths
from Fracao import Fracao

class Manual:

    def tela():
        """manages manual input screen"""
        recomecar="s"
        while recomecar == "s":
            fracao1 = input("informe a fração 1 no formato x/y:").split("/")
            fracao1 = Fracao(int(fracao1[0]), int(fracao1[1]))
            fracao2 = input("informe a fração 2 no formato x/y:").split("/")
            fracao2 = Fracao(int(fracao2[0]), int(fracao2[1]))
            continuar = "s"
            while continuar == "s":
                op=input("informe o operador: + - * /")
                print(Maths.controlador(op,fracao1,fracao2))
                print("Deseja fazer outra conta com as frações abaixo? s/n")
                print(str(fracao1)+'\n'+str(fracao2))
                continuar=input().lower()
            recomecar=input("Deseja novas contas com novas frações? s/n").lower()