nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7.0:
    print("O aluno está aprovado.")
elif 4 < media < 7.9:
    print("O aluno deve realizar a prova de segunda chamada.")
else:
    print("O aluno está reprovado.")