multa = 0
pesagem = float(input("Informe quantos quilos de peixes devem ser considerados: "))

if pesagem > 50:
    excesso = pesagem - 50
    multa = excesso * 4
    print(f"O excesso de peso foi de {excesso} quilos. Por isso, você deverá pagar uma multa de R${multa} reais.")

else:
    print("Sua pesagem está livre de multas.")