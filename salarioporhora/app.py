salarioporhora = float(input("Quanto você recebe por hora trabalhada?"))
horatrabalhada = int(input("Quantas horas por dia você trabalha?"))
salariomensal = (horatrabalhada * salarioporhora) * 30

print(f"O seu salário mensal é de R${salariomensal} reais.")