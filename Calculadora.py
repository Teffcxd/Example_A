class calculadora:
  def __init__(self):
    self.n1=float(input('Ingrese un primer valor: '))
    self.n2=float(input('Ingrese un segundo valor: '))
  def mostrar(self):
    print('valor 1 ', self.n1)
    print('valor 2 ', self.n2)
  def suma(self):
    suma=self.n1+self.n2
    print('la suma de:',self.n1 ,"y" , self.n2, "es", suma)
  def resta(self):
    resta=self.n1-self.n2
    print('la resta de:',self.n1 ,"y" , self.n2, "es", resta)
  def mul(self):
    mul=self.n1*self.n2
    print('la multiplicación de:',self.n1 ,"y",  self.n2, "es", mul)
  def div(self):

   if self.n2==0:
    print('ERROR MATH')
   else:
    div=self.n1/self.n2
    print('la división de:',self.n1 ,"y", self.n2, "es", div)
  def pot(self):
    pot=pow(self.n1,self.n2)
    print('La Potencia de', self.n1, 'a', self.n2, 'es: ', pot)
  
  def imprimir(self):
    print('Los numeros son: ')
    print('Numero 1: ', self.n1)
    print('Numero 2: ', self.n2)
 