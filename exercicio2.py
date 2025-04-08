class Domino():
    def _init_(self,faceA=0,faceB=0):
        self.Faces = (faceA,faceB)
    def getMostrarPontos(self):
        return print('Lado A: ',self.Faces[0], 'lado B: ',self.Faces[1])
    def Valor(self):
        return self.Faces[0] + self.Faces[1]
domino1 = Domino(2,6)
domino2 = Domino(4,3)
domino1.getMostrarPontos()
domino2.getMostrarPontos()
print("total de pontos: ", domino1.Valor() + domino2.Valor())