import json

# Lê o arquivo JSON com o faturamento diário
with open('faturamento.json') as file:
    faturamento = json.load(file)

# Remove os dias sem faturamento (valor 0)
faturamento = [valor for valor in faturamento if valor != 0]

# Calcula o menor e o maior valor de faturamento
menor = min(faturamento)
maior = max(faturamento)

# Calcula a média mensal de faturamento
media = sum(faturamento) / len(faturamento)

# Conta o número de dias em que o faturamento foi superior à média mensal
dias_acima_media = sum(valor > media for valor in faturamento)

# Imprime os resultados
print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")

