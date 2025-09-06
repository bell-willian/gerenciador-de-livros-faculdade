#Comecei importando a lib matplotlib
import matplotlib.pyplot as plt
#Agora criei a classe livro
class Livro:
    def __init__(self, titulo, autor, genero, quant):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quant = quant
#Criei a lista vazia que vai armazenar os livros
list_livros = []
#Criei uma função que cadastra um novo livro
def novo_livro(titulo, autor,genero,quant):
    nome_livro = Livro(titulo, autor, genero,quant)
    list_livros.append(nome_livro)
#Agora uma função para listar os livros
def todos_livros():
    for livro in list_livros:
        print(f"Título: {livro.titulo}, Autor: {livro.autor}, Genero: {livro.genero}, Quantidade: {livro.quant}")
#Agora outra função para buscar os livros
def buscar_livro(nome):
    for indice, livro in enumerate(list_livros):
        if nome == livro.titulo:
            print(f"Livro encontrado, o indice do seu livro é {indice}")
            return
    print("Livro não encontrado")
#Agora decidi usar um laço de repetição para fazer as solicitaçoes ao usuario
while(True):
    #nessa parte o usuario decide se quer cadastrar os livros
    cadastrar = input("Deseja cadastrar um livro? (1/0)")
    #nessa estrutura de condição eu faço a solicitação ao usuario do titulo, autor, genero e quantidade e após isso uso a função novo_livro para cadastrar o livro
    if cadastrar == "1":
        titulo = input("Qual título do livro: ")
        autor = input("Qual autor do livro: ")
        genero = input("Qual genero do livro: ")
        quant = int(input("Qual a quantidade de livros: "))
        novo_livro(titulo,autor,genero,quant)
        continue
    #Agora o usuario decide se quer buscar um livro
    buscar = input("Deseja buscar algum livro? (1/0)")
    #Agora nessa estrutura de condição eu solicito ao usuario o titulo do livro e uso a função buscar_livro para achar o livro
    if buscar == "1":
        nome = input("Digite o nome do título: ")
        buscar_livro(nome)
    #Agora o usuario decide se quer listar os livros
    listar = input("Deseja listar os livros? (1/0)")
    #Caso o usuario queira eu chamo a função todos_livros para listar os livros
    if listar == "S":
        todos_livros()
    #Agora pergunto o usuario se ele deseja continuar caso queira todo o laço se repetira caso não queira será mostrado o grafico em barra ao usuario
    continua = input("Deseja continuar a cadastrar, listar ou buscar? (1/0)")
    if continua == "0":
        break

#Aqui criei 2 listas para armazenar a quantidade e genero dos livros
quanti = []
genero = []
#Agora usei um laço for para armazenar nessas 2 listas a quantidade e genero
for livro in list_livros:
    quanti.append(livro.quant)
    genero.append(livro.genero)
#Agora usei a lib matplotlib para criar o grafico em barras
plt.bar(genero,quanti)
plt.xlabel('Genero')
plt.ylabel('Quantidade')
plt.title("Grafico de livros")
plt.show()
