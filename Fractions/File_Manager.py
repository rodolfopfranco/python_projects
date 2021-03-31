from Fracao import Fracao

class FractionsFile:

    def __init__(self):
        self.fractions = []

    def scanFile(self,filename):
        """proccess the file and generates fractions array"""
        f = open(filename)
        for s in f:
            fracao = s.split(" ")
            fracao = Fracao(int(fracao[0]),int(fracao[1]))
            self.fractions.append(fracao)

    def openFile(self):
        """opens the file"""
        return none

    def fileScreen(self):
        """Dialog screen for path info"""
        path=input("qual o diretório do arquivo?")
        self.scanFile(path)
        self.showResults()

    def showResults(self):
        """Shows sum and product of fractions array"""
        print("Soma: "+str(self.sumF()))
        print("Produto: "+str(self.multiplyF()))

    def multiplyF(self):
        """multiplies every array's fraction"""
        result = self.fractions[0]
        i = 0
        for f in self.fractions:
            if i == 0:
                i += 1
                continue
            else:
                result *= f
        return result

    def sumF(self):
        """sums every array's fraction"""
        result = Fracao(0,1)
        for f in self.fractions:
            result=result + f
        return result