while True:
    menu = int(input('1.Olá\n2.Oi\n3.Sair --> '))

    if menu == 1:
        print('Olá')
    elif menu == 2:
        print('Oi')
    elif menu == 3:
        print('Sair')
        break
    else:
        print('Opção Inválida')