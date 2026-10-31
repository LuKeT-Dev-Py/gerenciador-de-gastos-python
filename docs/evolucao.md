# Evolução e decisões do gerenciador de gastos

A [versão original](../versao_original.py) preserva a primeira solução do desafio. A [versão refatorada](../gerenciador_gastos.py) organiza as tarefas em funções e é a indicada para execução. O projeto foi desenvolvido durante o Curso de Python 3, de Otávio Miranda, na Udemy.

## Principais alterações

| Antes | Depois | Motivo |
|---|---|---|
| Todo o programa dentro de um único `while` | Responsabilidades divididas em funções | Facilita a leitura, os testes e futuras alterações |
| Chaves como `Gasto` e variável `dicta` | Nomes padronizados, como `descricao` e `gasto` | Torna a intenção do código mais clara |
| Categorias digitadas por extenso | Categorias apresentadas em um menu numérico | Evita erros de digitação |
| Gastos exibidos como dicionários | Tabela com colunas alinhadas | Melhora a experiência no terminal |
| Sem registro de data | Data validada no formato `DD/MM/AAAA` | Acrescenta contexto aos registros |
| Registros imutáveis | Opções para editar e excluir | Permite corrigir e administrar os dados |
| Valores como números comuns | Formatação brasileira (`R$ 25,90`) | Facilita a interpretação |
| `except` genérico | Exceções específicas, como `ValueError` | Evita esconder erros inesperados |
| Execução imediata ao importar | Proteção com `if __name__ == '__main__'` | Permite importar as funções sem iniciar o menu |

## Conceitos praticados

- listas, tuplas e dicionários;
- funções e retorno de valores;
- laços `while` e `for`;
- condicionais;
- tratamento de exceções;
- compreensão de listas;
- `lambda`, `max`, `sum` e `sorted`;
- importação do módulo `datetime`;
- validação e formatação de dados;
- organização de um programa em responsabilidades menores.

## Aprendizados novos

### Validação de datas com `datetime`

`datetime.strptime(texto, '%d/%m/%Y')` tenta interpretar o texto de acordo com
o formato informado. Datas inexistentes, como `31/02/2026`, geram
`ValueError`; o programa captura esse erro e solicita outra data.

### Bloco `if __name__ == '__main__'`

O bloco executa `main()` somente quando o arquivo é iniciado diretamente. Se o
arquivo for importado por outro programa, suas funções ficam disponíveis sem
abrir o menu automaticamente.

### Funções com responsabilidade única

Cada função cuida de uma tarefa, como ler um valor, formatar moeda ou editar um
registro. Essa separação reduz repetições e deixa o fluxo principal mais fácil
de entender.



A demonstração está disponível em [PNG](demonstracao.png) e [SVG](demonstracao.svg).

[Voltar ao README](../README.md).
