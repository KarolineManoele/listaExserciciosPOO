class Circle:
     def __init__(self, centro, r):
          self.centro = centro
          self.r = r 

     def calcularArea(self):
        area = 3.14 * (self.r ** 2)
        return area
     
     def calcularPerimetro(self):
        perimetro = 2 * 3.14 * self.r
        return perimetro
     
     def pertenceCircle(self, x, y):
        cx, cy = self.centro
        distancia =  (((x - cx)**2 + (y - cy)**2)) ** 0.5
        return distancia <= self.r
     
c1 = Circle((2, 2), 3)

print("Área:", c1.calcularArea())
print("Perímetro:", c1.calcularPerimetro())

print("Ponto (0, 0) pertence?", c1.pertenceCircle(0, 0))
print("Ponto (0, -1) pertence?", c1.pertenceCircle(0, -1))