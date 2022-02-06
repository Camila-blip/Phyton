'''
append
insert(0, 'x')
pop(1)
remove(x)
len()
sort()
reverse
max()
min()
sum()
'''
# as variaveis compostas podem armazerar um ou mais valores
idade = [18,20,30,40,15]
idade1 = []
#append adiciona valores
idade.append(18)
#insere uma posicao se nao tem, insere
idade.insert(3, 'camila')
#comando pop remove a ultima posicao se nao passar parametro
idade.pop(2)
#se eu quiser remover pelo valor
idade.remove(2)
#len retorna a quantidade de elementos que tem na lista
#print(len(idade))
#metodo sort() ordena a lista
idade.sort()
#se eu quiser ordenar de forma decrescente, e no phyton T sempre tem que ser maiusculo
idade.sort(reverse = True)
idade.reverse()
#pega valor maximo
print(max(idade))
#pega valor minimo
print(min(idade))
#sum pega a soma de toda a lista
print(sum(idade))


