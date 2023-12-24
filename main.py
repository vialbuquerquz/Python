import pandas as pd

df = pd.read_excel("data/VendaCarros.xlsx")

#nova tabela com colunas específicas
data = df[["Fabricante", "ValorVenda", "Ano"]]
print(data)

#geração da nova tabela(pivô)
pivot_table = data.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)

print(pivot_table)

#Exportando tabela em arquivo excel

pivot_table.to_excel("data/pivotable.xlsx", "Relatório")