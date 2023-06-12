arquivo = open('criandoarqtext.txt', 'w')

arquivo.write("Curso python \n")
arquivo.write("Aula prática")
arquivo.close()

#leitura de arquivo de texto

leitura = open('criandoarqtext.txt', 'r')
print(leitura.read())
leitura.close()