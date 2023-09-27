altura = float(input("Informe a sua altura: "))
genero = input("Informe o seu gênero para realizar um cálculo mais preciso: ")

if genero == "feminino":
    imcfinal = round((62.1*altura) - 44.7, 2)
elif genero == "masculino":
    imcfinal = round((72.7 * altura) - 58, 2)
else:
    print("Gênero inválido. Por favor, informe feminino ou masculino.")
    imcfinal = None

if imcfinal is not None: 
    print(f"O seu peso ideal é de {imcfinal} kg.")