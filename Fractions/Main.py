from Fracao import Fracao
from Maths import Maths
from Manual import Manual
from File_Manager import FractionsFile

def demo():
    print("Demo de resultados com estas 2 frações:")
    f = Fracao(15,45)
    g = Fracao(50,75)
    print("f = "+str(f.num)+"/"+str(f.den))
    print("g = "+str(g.num)+"/"+str(g.den)+"\n")
    print("f = 15/45 = %s" %f)
    print("g= 50/75 = %s" % g)
    print("f+g = %s" % (f + g))
    h = Fracao(10, 28)
    print("h = 10/28 = %s" % h)
    print("f * h = %s" % (f * h))
    print("f + g + h = %s" % (f + g + h))
    print("f * g * h = %s" % (f * g * h))
    print("f + g * h = %s" % (f + g * h))
    print("g - f - f = %s" % (g - f - f))
    print("f * 2 = %s" % (f * 2))
    print("f + 2 = %s" % (f + 2))
    print("f/g = %5s" % (f / g))
    f += g * 2
    print("f += g*2 = %s" % f)
    f -= g * 2
    print("f -= g*2 = %s" % f)

def menu():
    f = FractionsFile()
    print("Escolha uma opção:")
    print("1 - Manual")
    print("2 - Arquivo")
    print("3 - Demo")
    choice=int(input('digite um número'))
    if(choice==3):
        demo()
    elif(choice==2):
        f.fileScreen()
    elif(choice==1):
        Manual.tela()

def main():
    menu()

main()