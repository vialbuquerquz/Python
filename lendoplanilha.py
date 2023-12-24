from openpyxl import load_workbook

#lendo pasta de trabalho
wb = load_workbook("data/pivotable.xlsx")

sheet = wb["Relatório"]

for i in range(2, 6):
    ano = sheet["A%s" %i].value
    am  = sheet["B%s" %i].value
    bt = sheet["C%s" %i].value
    print("{0} o Aston Martin vendeu {1} e o Bentley vendeu {2}.".format(ano, am, bt))

