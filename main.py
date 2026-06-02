#01
votos = [0,0,0,0,0,0]

print("1 - Windows Server")
print("2 - Unix")
print("3 - Linux")
print("4 - Netware")
print("5 - Mac OS")
print("6 - Outro")

voto = int(input("Escolha uma opção: "))

if voto == 1:
  votos[0] += 1
elif voto == 2:
  votos[1] += 1
elif voto == 3:
  votos[2] += 1
elif voto == 4:
  votos[3] += 1
elif voto == 5:
  votos[4] += 1
elif voto == 6:
  votos[5] += 1
else:
  print("Valor inválido")

while voto != 0:
  print("1 - Windows Server")
  print("2 - Unix")
  print("3 - Linux")
  print("4 - Netware")
  print("5 - Mac OS")
  print("6 - Outro")

  voto = int(input("Escolha uma opção: "))

  if voto == 1:
    votos[0] += 1
  elif voto == 2:
    votos[1] += 1
  elif voto == 3:
    votos[2] += 1
  elif voto == 4:
    votos[3] += 1
  elif voto == 5:
    votos[4] += 1
  elif voto == 6:
    votos[5] += 1
  else:
    print("Valor inválido")

totalVotos = votos[0] + votos[1] + votos[2] + votos[3] + votos[4] + votos[5]
print(totalVotos)

percentuais = []
for i in range(6):
  percentuais.append((votos[i] / totalVotos) * 100)

maiorVotos = max(votos)
indiceVencedor = votos.index(maiorVotos)

print(percentuais)
print(maiorVotos)

#02
salarios = []

def solicitaSalario():
    salario = float(input("Digite o salário do funcionário: "))
    if salario != 0:
        salarios.append(salario)
    return salario

def calcularAbono(salario_funcionario):
    abono = salario_funcionario * 0.20
    if abono < 100:
        abono = 100
    return abono


print("Projeção de Gastos com Abono")
print("============================")

while True:
    salario_atual = solicitaSalario()
    if salario_atual == 0:
        break

print("\nSalário - Abono")

total_gastos = 0
minimo_pago = 0
maior_abono = 0
total_colaboradores = 0

for s in salarios:
    total_colaboradores = total_colaboradores + 1
    valor_do_abono = calcularAbono(s)

    if valor_do_abono == 100:
        minimo_pago = minimo_pago + 1
    if valor_do_abono > maior_abono:
        maior_abono = valor_do_abono
    total_gastos = total_gastos + valor_do_abono

    print("R$", s, "-", "R$", valor_do_abono)

print("\nForam processados", total_colaboradores, "colaboradores")
print("Total gasto com abonos: R$", total_gastos)
print("Valor mínimo pago a", minimo_pago, "colaboradores")
print("Maior valor de abono pago: R$", maior_abono)


#03
carros = {}

print("Comparativo de Consumo de Combustível")
print("=" * 40)

for i in range(5):
    print(f"\nVeículo {i + 1}")
    nome = input("Nome: ")
    consumo = float(input("Km por litro: "))

    carros[nome] = consumo

mais_economico = max(carros, key=carros.get)

print("\nRelatório Final")

for i, (nome, consumo) in enumerate(carros.items(), start=1):
    litros = 1000 / consumo
    custo = litros * 2.25

    print(
        f"{i} - {nome} - {consumo:.1f} - "
        f"{litros:.1f} litros - R$ {custo:.2f}"
    )

print(f"\nO menor consumo é do {mais_economico}.")  


#04
def principal():

    relatorio = {
        1: {"situacao": "necessita da esfera", "quantidade": 0},
        2: {"situacao": "necessita de limpeza", "quantidade": 0},
        3: {"situacao": "necessita troca do cabo ou conector", "quantidade": 0},
        4: {"situacao": "quebrado ou inutilizado", "quantidade": 0}
    }

    total_mouses = 0

    print("--- Levantamento de Mouses no Suporte de Informática ---")
    print("Categorias de defeitos:")
    for codigo, dados in relatorio.items():
        print(f"{codigo} - {dados['situacao'].capitalize()}")
    print("0 - Encerrar o programa e emitir relatório\n")

    while True:
        try:
            voto = int(input("Informe o tipo de defeito (0 a 4): "))

            if voto == 0:
                break


            if voto in relatorio:
                relatorio[voto]["quantidade"] += 1
                total_mouses += 1
            else:
                print("Opção inválida! Digite um número entre 1 e 4 (ou 0 para sair).")

        except ValueError:
            print("Entrada inválida. Por favor, insira apenas números inteiros.")


    if total_mouses == 0:
        print("\nNenhum mouse foi registrado.")
        return


    print("\n" + "="*55)
    print(f"Quantidade de mouses testados: {total_mouses}")
    print("="*55)
    print(f"{'Situação':<40} {'Quantidade':<12} {'Percentual'}")
    print("-"*65)

    for codigo, dados in relatorio.items():
        qtd = dados["quantidade"]
        percentual = (qtd / total_mouses) * 100

        print(f"{codigo}- {dados['situacao']:<37} {qtd:<12} {percentual:>3.0f}%")

    print("-"*65)

if __name__ == "__main__":
    principal()