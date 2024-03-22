arquivo = 'dataset.csv'
arquivo = open(arquivo, 'r')
dados = arquivo.readlines()
pula = 0
somatorio = 0
velho = 0
for i in range(len(dados)):
    if i == 0:
        continue
    idade = dados[i].split(',')[1].replace('\n', '').replace(' ', '')
    if int(idade) > velho:
        velho = int(idade)
        index_velho = i
    somatorio = int(somatorio) + int(idade)
  
media = somatorio / (len(dados) - 1)
nome_velho = dados[index_velho].split(',')[0].replace('\n', '').replace(' ', '') 
idade_velho = dados[index_velho].split(',')[1].replace('\n', '').replace(' ', '') 

print("Média de idade", media)
print("Maior idade", nome_velho, idade_velho)

    