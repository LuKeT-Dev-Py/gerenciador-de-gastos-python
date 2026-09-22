"""Versão original do desafio, preservada para demonstrar a evolução do projeto."""

Gastos = []
menu = (
    '1: Adicionar',
    '2: Listar',
    '3: Maior gasto',
    '4: Total',
    '5: Filtrar',
    '6: Descrições',
    '7: Ordenar',
    '8: Sair'
)


def soma(*x):
    return sum(*x)


categorias = ('Alimento', 'Lazer', 'Transporte', 'Estudos')

while True:
    print(menu)
    try:
        escolha = int(input('Escolha o NUMERO que deseja do menu: '))
    except ValueError:
        print('Digite um valor valido!')
        continue

    if escolha not in range(1, 9):
        print('Escolha um numero valido!!')
        continue

    if escolha == 1:
        try:
            nome = input('No que foi gasto?: ')
            valor = float(input('Qual foi o valor do gasto?: '))
            categoria = input(
                'Alimento, Lazer, Transporte ou Estudos. '
                'Qual categoria do gasto?: '
            )
            if categoria not in categorias:
                print('Selecione uma categoria valida.')
                continue
        except ValueError:
            print('Digite apenas valores e caracteres validos!!')
            continue

        if not nome or not valor or not categoria:
            print('Digite todos os pedidos')
            continue
        if valor <= 0:
            print('Digite valor maior que 0!')
            continue

        dicta = {}
        dicta['Gasto'] = nome
        dicta['Valor'] = valor
        dicta['Categoria'] = categoria
        Gastos.append(dicta)
        continue

    if escolha == 2:
        if Gastos == []:
            print('Não tem nada para listar')
            continue
        for n in enumerate(Gastos):
            print(n)
        continue

    if escolha == 3:
        if Gastos == []:
            print('Não tem nenhum gasto')
            continue
        mais_caro = max(Gastos, key=lambda produto: produto['Valor'])
        print(mais_caro)

    elif escolha == 4:
        if Gastos == []:
            print('Não tem nada para somar')
            continue
        total = []
        for n in Gastos:
            total.append(n['Valor'])
        print(f'Total = {soma(total)}')

    elif escolha == 5:
        ver = input('Deseja ver qual categoria: ').strip().title()
        filtrados = [
            gasto
            for gasto in Gastos
            if gasto['Categoria'] == ver
        ]
        if filtrados:
            for gasto in filtrados:
                print(gasto['Gasto'])
        else:
            print('Nada encontrado!')

    elif escolha == 6:
        if Gastos == []:
            print('Não tem nada para descrever')
            continue
        lista = [gasto['Gasto'] for gasto in Gastos]
        print(lista)

    elif escolha == 7:
        if Gastos == []:
            print('Não tem nada para ordenar')
            continue
        ordem = sorted(Gastos, key=lambda produto: produto['Valor'])
        print(ordem)

    elif escolha == 8:
        break
