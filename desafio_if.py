#Indentificação do nome e idade da pessoa
nome = input("Digite seu nome: ")
idade= int(input("Digite sua idade: "))
if idade <18:
    print("Por ser menor de idade não poderá completar a inscrição.")
else:
    print("Sua idade está aprovada para continuar o processo.")

#CPF do inscrito
cpf= int(input("Digite seu cpf: "))
if cpf !=11:
    print("CPF inválido.")
#Escolaridade do inscrito
print("1 - Ensino Médio" )
print("2 - Ensino Superior")
print("3 - Pós-graduação")

escola= input("Digite seu nível de escola")
if escola ==1:
    nível_de_ensino= "Ensino Médio completo"
elif escola ==2:
    nível_de_ensino= "Ensino de Superior completo"
elif escola ==3:
    nível_de_ensino= "Ensino de Pós-Graduação completo"
else:
    nível_de_ensino= "Nível de ensino não encontrado"

#Escolha do sexo do inscrito
sexo =("Masculino" or "Feminino")
sexo = input("Qual é o seu sexo?").upper()

if sexo == "Masculino":
    documento="Apresente a sua reservista."
elif sexo == "Feminino":
    documento="Não é nescessário apresentar a reservista."
else:
    documento= "Sexo inválido"

#Escolha da área que deseja atuar
print("\nEcolha a área desejada:")
print("1 - Administração")
print("2 - Tecnologia da Informação")
print("3 - Educação")

area = int(input("Área: "))

if area == 1:
    cargo = "Administração"
elif area ==2:
    cargo = "Analista de Sistema"
elif area ==3: 
    cargo = "Educacional"
else:
    cargo = "área Inválida"

#Final
print("\n"+ "+"*40)
print("INSCRIÇÃO DO CANDIDATO")
print("="*40)

print(f"Nome do candidato: {nome}")
print(f"Idade do candidato: {idade} anos")
print(f" CPF do candidato: {cpf}")
print(f"Nível de escolaridade do candidato: {escola}")
print(f"Cargo escolhido: {cargo}")
print(f"Sexo: {documento}")

if idade >= 18 and escola>0 and sexo in ["Masculino", "Feminino"]:
    print("\n INSCRIÇÃO FEITA COM SUCESSO!")
else:
    print("\n INSCRIÇÃO INVÁLIDA!")



