from random import choice
print('''Regras do pedra, papel e tesoura:
    pedra vs papel -> vitória do papel
    pedra vs tesoura -> vitória da pedra
    papel vs tesoura-> vitória da tesoura.''')
print('-='*20)
VC = VE = 0
while True:
    lista = ['tesoura','papel','pedra']
    computador = choice(lista)
    vc = input('digite sua escolha (pedra, papel ou tesoura): ')
    print('-=' * 20)
    print(f'      Computador escolheu {computador}')
    print('-=' * 20)
    print('resultado:'.upper())
    print('*'*15)
    if vc == computador:
        print('Deu empate'.upper())
    elif vc == 'tesoura':
        if computador == 'pedra':
            VC += 1
            print('vc perdeu, boa sorte na próxima')
        else:
            VE +=1
            print('vc venceu')
    elif vc == 'pedra':
        if computador == 'papel':
            VC += 1
            print('vc perdeu, boa sorte na próxima')
        else:
            VE += 1
            print('vc venceu')
    elif vc == 'papel':
        if computador == 'tesoura':
            VC += 1
            print('vc perdeu, boa sorte na próxima')
        else:
            VE += 1
            print('vc venceu')
    print(f' O computador já ganhou {VC} vez(es) e você já ganhou {VE} vez(es)')
    print('0-0-'*8)
    if input('vc quer continuar? [s/n] ').lower() == 'n':
        print('Muito obrigada por jogar, esperamos que tenha gostado!!')
        break
