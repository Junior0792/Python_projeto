# Vetor que guarda o valor de faturamento diário de uma distribuidora 

faturamento = [ 22174.1664, 24537.6698,  26139.6134, 0.0, 0.0,  26742.6612, 0.0, 42889.2258, 46251.174,  11191.4722, 0.0, 0.0,  3847.4823, 
               373.7838, 2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 
               25681.8318, 1718.1221, 13220.495, 8414.61 ];

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

