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

# calcula o CR de cada diciplina de pela media delas,
#  (programa desemvolvido para receber a quantidade de disciplinas cursadas,
#    ler a media de cada diciplina e ao final calcular o coeficiente de rendimento)

n = int(input('Digite a quantidade de disciplinas cursadas: '))
total = 0  # Variável para acumular as notas

for i in range(n):
    media = float(input(f'Média da disciplina {i + 1}: '))  # Recebe a média de cada disciplina
    total += media  # Soma a média ao total

cr = total / n  # Calcula a média geral (CR)
print(f'O coeficiente de rendimento (CR) é: {cr}')

# codigo que mostra numero 1 e vai continuando ate o numero que o usuario escolheu e onde esteiver os multiplos de 5(foo) e 7 (bar)

n = int(input('Digite um número: '))

for i in range(1, n + 1):
    if i % 5 == 0 and i % 7 == 0:
        print('foo bar')  # Múltiplos de 5 e 7
    elif i % 5 == 0:
        print('foo')  # Múltiplos de 5
    elif i % 7 == 0:
        print('bar')  # Múltiplos de 7
    else:
        print(i)  # Outros números
