numero = int(input("Digite um número: "))

fibonacci = [0, 1]  # Inicia a sequência de Fibonacci com 0 e 1

# Gera a sequência de Fibonacci até o último número ser menor ou igual ao número informado pelo usuário
while fibonacci[-1] < numero:
  proximo = fibonacci[-1] + fibonacci[
    -2]  # Calcula o próximo número da sequência
  fibonacci.append(proximo)  # Adiciona o próximo número à sequência

if numero in fibonacci:
  print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
  print(f"O número {numero} não pertence à sequência de Fibonacci.")
