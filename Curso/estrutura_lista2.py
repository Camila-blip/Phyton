x = []
for i in range(1,101):
    x.append(i)

#outra forma de fazer
x = list(range(1,101))
a = [1,2,3,4,5]
y = int(input('digite um numero'))

if y in x:
    x.remove(y)
    print('o valor foi removido com sucesso')

#criando outra lista e acessando as posicoes
x= [['camila',20],['jhenifer',24]]
print(x[0][1])
