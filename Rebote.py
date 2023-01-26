class Bouncy:

  def is_bouncy(self, N):
      '''Esta función determina si el numero iterado es rebotante.'''
      number = list(str(N))
      increasing = list(str(N))
      decreasing = list(str(N))
      increasing.sort()
      decreasing.sort(reverse=True)
      if (number != increasing and number != decreasing):
          return True
      else:
          return False

  def __init__(self):
      '''Esta función itera los números de forma ascendente para asi poder evaluar la secuencia de cada cifra. '''
      start = 1
      total = 0
      bou = 0 
      while True:
          total += 1
          if self.is_bouncy(start):
              bou += 1
          if bou/total >= 0.99:
              break
          start += 1
      return print(start)

test = Bouncy()
