x = 10
y = 20

def soma(a, b):
  resultado = a + b
  return resultado
  
def divisao(a, b):
  if b == 0:
    print("Erro: Divisão por zero.")
  return a / b

def mensagem():
    print("Esta função não faz nada importante.")

soma(x, y)
divisao(10, 0)
