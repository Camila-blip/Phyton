#espaco \n
x = 0
decisao = 0

while x < 10:
    print(x)
    x = x + 1
while decisao != 3:
    decisao = int(input('digite 1 para logar 2 para cadastrar e 3 para sair'))
    if decisao == 1:
        print('logando')
    if decisao == 3:
        break
    elif decisao == 2:
        print('cadastrando')
print('Você saiu')
