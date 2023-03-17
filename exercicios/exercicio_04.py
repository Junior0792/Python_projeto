# Define a string
string = "Busco emprego"

# Converte a string para uma lista de caracteres
caracteres = list(string)

# Inverte a ordem dos caracteres na lista
for i in range(len(caracteres)//2):
    temp = caracteres[i]
    caracteres[i] = caracteres[len(caracteres)-i-1]
    caracteres[len(caracteres)-i-1] = temp

# Converte a lista de caracteres de volta para uma string
string_invertida = ''.join(caracteres)

# Imprime a string invertida
print(string_invertida)

