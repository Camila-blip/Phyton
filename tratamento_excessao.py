#erro sintatico  se digitar algo errado
#erro semantico logica
#comando finally e executado mesmo se houver erro
#else so e executado se der sucesso
try:
    x = int(input('digite sua idade'))
except:
    print('Você não digitou sua idade correta')
else:
    print(f'sua idade é {x}')
finally:
    print('muito obrigado por acessar')
