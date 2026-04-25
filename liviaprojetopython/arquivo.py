# Escrever em Arquivos

'''
Comando para Ler e Escrever Arquivos

with open(file="caminho do arquivo", mode='Modo de Leitura ou Escrita',
     encoding='decodificado') as apelido:
         bloco de codigo
'''

'''
O Modo de Escrita - W
O Modo de Leitrua - R
o Modo de Acrescimo - A
'''

nome_do_arquivo = "pepsico.txt"
with open(file=nome_do_arquivo, mode="w", encoding='utf8') as arquivo:
    print(f''' O incidente 349 da Pepsi (1992, Filipinas) foi uma falha catastrófica de marketing onde um erro 
de produção emitiu 800 mil tampinhas premiadas com o número "349", prometendo 1 milhão de pesos filipinos a cada cidadão. 
   A recusa da Pepsi em pagar, oferecendo valor irrisório, gerou revolta popular, 32 mortes, e milhares de processos.''')  # noqa: F541
