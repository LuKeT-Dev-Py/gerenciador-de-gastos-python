"""Gerenciador de gastos executado pelo terminal."""

from datetime import datetime


CATEGORIAS = ('Alimento', 'Lazer', 'Transporte', 'Estudos')
LARGURA = 72


def exibir_titulo(titulo):
    """Exibe um título com separadores para organizar a interface."""
    print(f'\n{"=" * LARGURA}')
    print(titulo.center(LARGURA))
    print('=' * LARGURA)


def formatar_moeda(valor):
    """Converte um número para o formato monetário brasileiro."""
    numero_formatado = f'{valor:,.2f}'
    numero_formatado = numero_formatado.replace(',', 'X')
    numero_formatado = numero_formatado.replace('.', ',')
    numero_formatado = numero_formatado.replace('X', '.')
    return f'R$ {numero_formatado}'


def data_valida(texto):
    """Verifica se uma data existe e está no formato DD/MM/AAAA."""
    try:
        datetime.strptime(texto, '%d/%m/%Y')
        return True
    except ValueError:
        return False


def ler_descricao(descricao_atual=None):
    """Solicita uma descrição não vazia ou mantém o valor atual."""
    while True:
        texto_atual = f' [{descricao_atual}]' if descricao_atual else ''
        descricao = input(f'Descrição do gasto{texto_atual}: ').strip()

        if descricao:
            return descricao
        if descricao_atual is not None:
            return descricao_atual

        print('A descrição não pode ficar vazia.')


def ler_valor(valor_atual=None):
    """Solicita um valor positivo ou mantém o valor atual."""
    while True:
        texto_atual = f' [{formatar_moeda(valor_atual)}]' if valor_atual else ''
        entrada = input(f'Valor do gasto{texto_atual}: ').strip().replace(',', '.')

        if not entrada and valor_atual is not None:
            return valor_atual

        try:
            valor = float(entrada)
        except ValueError:
            print('Digite um número válido. Exemplo: 25,90')
            continue

        if valor <= 0:
            print('O valor precisa ser maior que zero.')
            continue

        return valor


def ler_categoria(categoria_atual=None):
    """Mostra as categorias numeradas e devolve a categoria escolhida."""
    while True:
        print('\nCategorias:')
        for numero, categoria in enumerate(CATEGORIAS, start=1):
            print(f'  {numero}. {categoria}')

        texto_atual = f' [{categoria_atual}]' if categoria_atual else ''
        entrada = input(f'Escolha uma categoria{texto_atual}: ').strip()

        if not entrada and categoria_atual is not None:
            return categoria_atual

        try:
            indice = int(entrada) - 1
            if 0 <= indice < len(CATEGORIAS):
                return CATEGORIAS[indice]
        except (ValueError, IndexError):
            pass

        print('Escolha uma categoria entre 1 e 4.')


def ler_data(data_atual=None):
    """Solicita e valida uma data; no cadastro, vazio significa hoje."""
    while True:
        if data_atual is None:
            hoje = datetime.now().strftime('%d/%m/%Y')
            entrada = input(f'Data (DD/MM/AAAA) [{hoje}]: ').strip()
            data = entrada or hoje
        else:
            entrada = input(f'Data (DD/MM/AAAA) [{data_atual}]: ').strip()
            data = entrada or data_atual

        if data_valida(data):
            return data

        print('Digite uma data existente no formato DD/MM/AAAA.')


def exibir_tabela(gastos, titulo='GASTOS CADASTRADOS'):
    """Exibe os gastos em colunas e informa se havia dados para mostrar."""
    exibir_titulo(titulo)
    if not gastos:
        print('Nenhum gasto encontrado.')
        return False

    print(f'{"Nº":<4}{"Data":<12}{"Descrição":<22}{"Categoria":<16}{"Valor":>18}')
    print('-' * LARGURA)

    for numero, gasto in enumerate(gastos, start=1):
        descricao = gasto['descricao'][:20]
        print(
            f'{numero:<4}'
            f'{gasto["data"]:<12}'
            f'{descricao:<22}'
            f'{gasto["categoria"]:<16}'
            f'{formatar_moeda(gasto["valor"]):>18}'
        )
    return True


def adicionar_gasto(gastos):
    """Coleta os dados e adiciona um novo gasto à lista."""
    exibir_titulo('ADICIONAR GASTO')
    gasto = {
        'descricao': ler_descricao(),
        'valor': ler_valor(),
        'categoria': ler_categoria(),
        'data': ler_data(),
    }
    gastos.append(gasto)
    print('\nGasto adicionado com sucesso!')


def escolher_indice(gastos, acao):
    """Solicita o número de um gasto e devolve seu índice na lista."""
    if not exibir_tabela(gastos, f'{acao.upper()} GASTO'):
        return None

    while True:
        try:
            numero = int(input(f'Número do gasto que deseja {acao.lower()}: '))
            if 1 <= numero <= len(gastos):
                return numero - 1
        except ValueError:
            pass

        print('Digite o número de um gasto existente.')


def editar_gasto(gastos):
    """Permite alterar os campos de um gasto cadastrado."""
    indice = escolher_indice(gastos, 'Editar')
    if indice is None:
        return

    gasto = gastos[indice]
    print('\nPressione Enter para manter o valor atual.')
    gasto['descricao'] = ler_descricao(gasto['descricao'])
    gasto['valor'] = ler_valor(gasto['valor'])
    gasto['categoria'] = ler_categoria(gasto['categoria'])
    gasto['data'] = ler_data(gasto['data'])
    print('\nGasto atualizado com sucesso!')


def excluir_gasto(gastos):
    """Exclui um gasto após uma confirmação explícita."""
    indice = escolher_indice(gastos, 'Excluir')
    if indice is None:
        return

    gasto = gastos[indice]
    confirmacao = input(
        f'Excluir "{gasto["descricao"]}" no valor de '
        f'{formatar_moeda(gasto["valor"])}? [s/N]: '
    ).strip().lower()

    if confirmacao == 's':
        gastos.pop(indice)
        print('Gasto excluído com sucesso!')
    else:
        print('Exclusão cancelada.')


def mostrar_maior_gasto(gastos):
    """Localiza o gasto com maior valor."""
    if not gastos:
        exibir_tabela(gastos, 'MAIOR GASTO')
        return

    maior = max(gastos, key=lambda gasto: gasto['valor'])
    exibir_tabela([maior], 'MAIOR GASTO')


def mostrar_total(gastos):
    """Soma e exibe o valor de todos os gastos."""
    exibir_titulo('TOTAL DOS GASTOS')
    total = sum(gasto['valor'] for gasto in gastos)
    print(f'Total acumulado: {formatar_moeda(total)}')


def filtrar_por_categoria(gastos):
    """Exibe somente os gastos da categoria selecionada."""
    exibir_titulo('FILTRAR POR CATEGORIA')
    categoria = ler_categoria()
    filtrados = [
        gasto for gasto in gastos
        if gasto['categoria'] == categoria
    ]
    exibir_tabela(filtrados, f'CATEGORIA: {categoria.upper()}')


def mostrar_descricoes(gastos):
    """Exibe somente as descrições cadastradas."""
    exibir_titulo('DESCRIÇÕES')
    if not gastos:
        print('Nenhum gasto encontrado.')
        return

    for numero, gasto in enumerate(gastos, start=1):
        print(f'{numero}. {gasto["descricao"]}')


def ordenar_por_valor(gastos):
    """Exibe uma cópia ordenada, sem alterar a lista original."""
    ordenados = sorted(
        gastos,
        key=lambda gasto: gasto['valor'],
        reverse=True,
    )
    exibir_tabela(ordenados, 'GASTOS DO MAIOR PARA O MENOR')


def exibir_menu():
    """Exibe as ações disponíveis."""
    exibir_titulo('GERENCIADOR DE GASTOS')
    print('1. Adicionar gasto')
    print('2. Listar gastos')
    print('3. Mostrar maior gasto')
    print('4. Mostrar total')
    print('5. Filtrar por categoria')
    print('6. Mostrar descrições')
    print('7. Ordenar por valor')
    print('8. Editar gasto')
    print('9. Excluir gasto')
    print('0. Sair')


def main():
    """Mantém o programa em execução até o usuário escolher sair."""
    gastos = []

    while True:
        exibir_menu()
        escolha = input('Escolha uma opção: ').strip()

        if escolha == '1':
            adicionar_gasto(gastos)
        elif escolha == '2':
            exibir_tabela(gastos)
        elif escolha == '3':
            mostrar_maior_gasto(gastos)
        elif escolha == '4':
            mostrar_total(gastos)
        elif escolha == '5':
            filtrar_por_categoria(gastos)
        elif escolha == '6':
            mostrar_descricoes(gastos)
        elif escolha == '7':
            ordenar_por_valor(gastos)
        elif escolha == '8':
            editar_gasto(gastos)
        elif escolha == '9':
            excluir_gasto(gastos)
        elif escolha == '0':
            print('\nPrograma encerrado. Até a próxima!')
            break
        else:
            print('\nOpção inválida. Escolha um número do menu.')


if __name__ == '__main__':
    main()
