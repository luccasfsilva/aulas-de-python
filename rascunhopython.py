# exercicios (deixa as letras em maiúsculas)
def processar_frase():
    frase = input("Digite uma frase: ") 
    # frase ao usuário
    frase_processada = frase.replace(" ", "").upper() 
    # Remove espaços/converte para maiúsculas
    print("Frase processada:", frase_processada)
    # Executa a função
processar_frase()

# exercicios (salario do funcionario/ indice em % e o saraio atual)
def calcular_novo_salario():
    salario = float(input("Digite o salário do funcionário: ")) 
    # Recebe o salário
    reajuste = int(input("Digite o índice de reajuste (em %): ")) 
    # Recebe o índice de reajuste
    novo_salario = salario + (salario * reajuste / 100)  
    # Calcula o novo salário
    print(f"O novo salário será: R$ {novo_salario:.2f}")
# Executa a função
calcular_novo_salario()

# calcula o CR de cada diciplina de pela media delas 
n = int(input('Digite a quantidade de disciplinas cursadas: '))
total = 0  # Variável para acumular as notas

for i in range(n):
    media = float(input(f'Média da disciplina {i + 1}: '))  # Recebe a média de cada disciplina
    total += media  # Soma a média ao total

cr = total / n  # Calcula a média geral (CR)
print(f'O coeficiente de rendimento (CR) é: {cr}')
