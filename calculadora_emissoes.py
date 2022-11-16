import math

print("========================================================================")
print("Quantas árvores precisa plantar por ano de acordo com sua emissão de CO2")
print("========================================================================")
distancia = int(input("Distância do percurso por dia (Km): "))
semana = int(input("Número de dias por semana que o percurso é feito: "))
combustivel = int(input("Digite 1 para gasolina e 2 para diesel: "))
while combustivel != 1 and combustivel != 2:
    combustivel = int(input("Digite 1 para gasolina e 2 para diesel: "))
consumo = int(input("Taxa de consumo (Km/L): "))
print("------------------------------------------------------------------------")
diario = distancia / consumo
anual = diario * 53
if combustivel == 1:
    emissoes = ((distancia * semana * 53) / consumo) * (0.82 * 0.75 * 3.7)
elif combustivel == 2:
    emissoes = ((distancia * semana * 53) / consumo) * (0.83 * 3.7)
else:
    emissoes = 0

print("Consumo diário (L): %.2f" % diario)
print("Consumo anual (L): %.2f" % anual)
print("Emissões totais (Kg CO2-eq): %.2f" % (emissoes))
print("Nº de árvores a plantar na Mata Atlântica: %d" % (int(math.ceil(emissoes / 130))))
print("Nº de árvores a plantar na Amazônia: %d" % (int(math.ceil(emissoes / 222))))
print("========================================================================")
