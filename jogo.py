from random import choice
print('''Regras do pedra, papel e tesoura:
    pedra vs papel -> vitória do papel
    pedra vs tesoura -> vitória da pedra
    papel vs tesoura-> vitória da tesoura.''')
print('-='*20)
while True:
    lista = ['tesoura','papel','pedra']
    computador = choice(lista)
    vc = input('digite sua escolha (pedra, papel ou tesoura): ')
    print('-=' * 20)
    print(f'           Computador escolheu {computador}')
    print('-=' * 20)
    print('resultado:'.upper())
    print('*'*10)
    if vc == computador:
        print('Deu empate'.upper())
    elif vc == 'tesoura':
        print('vc perdeu, boa sorte na próxima') if computador == 'pedra' else print('vc venceu')
    elif vc == 'pedra':
        print('vc perdeu, boa sorte na próxima') if computador == 'papel' else print('vc venceu')
    elif vc == 'papel':
        print('vc perdeu, boa sorte na próxima') if computador == 'tesoura' else print('vc venceu')
    if input('vc quer continuar? [s/n] ').lower() == 'n':
        print('Muito obrigada por jogar, esperamos que tenha gostado!!')
