class CalculadoraCoprimo:

  def mdc(self, x, y):
    if (x > y):
      return self.mdc(y, x)
    if (x == 0):
      return y
    return self.mdc(x, y % x)

  def QuantosCoprimos(self, numero_analisado):
    quantos = 0
    i = 1
    while (i < numero_analisado):
      if (self.mdc(i, numero_analisado) == 1):
        quantos += 1
      i += 1
    return quantos

