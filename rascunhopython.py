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
