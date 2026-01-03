estados_centro_oeste = ['Goiás', 'Mato Grosso', 'Mato Grosso do Sul']

print(estados_centro_oeste[0])
print(estados_centro_oeste[2])
print(estados_centro_oeste[-1])

#Append acrescenta dados no final
estados_centro_oeste.append('DF')
print(estados_centro_oeste)

#Acrescenta uma lista de dados no final
estados_centro_oeste.extend(['Espirito Santo', 'Rio de Janeiro'])


#Listas aninhadas
frutas = ['pera', 'maçã', 'uva', 'banana']
vegetais = ['cenoura', 'batata', 'tomate']

alimentos_saudaveis = [frutas, vegetais]
print(alimentos_saudaveis)
