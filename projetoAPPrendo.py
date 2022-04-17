class Pessoas:
    pessoa = 'Nome Qualquer'

    def __init__(self, nome, cidade, CEP, data_nascimento):
        self.nome = nome    # variável de instância que chama o método self.nome que é uma propriedade
        self.cidade = cidade
        self.cep = cep
        self.data_nascimento = data_nascimento
# os decoradores como recurso para esconder os atributos da classe e impedir o acesso direto a eles fora da classe
    @property
    def nome(self):
        return self.__nome # __ permite esconder o nome e data_nascimento dentro da classe, porque os torna inacessíveis fora da classe.
    @nome.setter
    def nome (self, valor):
        if valor == None or not valor.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")

    @property
    def data_nascimento(self):
            return self.__data_nascimento

    @data_nascimento.setter
        def data_nascimneto(self, valor):
            if valor == None or not valor.strip():
                raise ValueError("Data de nascimento não pode ser nulo nem em branco")


    def incluir(self, pessoa):
        if self.pesquisa(pessoa) == -1:
            self.pessoas.append(pessoa)

    def alterar(self, pessoas):
        for pessoa in self.pessoas:
            print(pessoa.nome, pessoa.cidade, pessoa.CEP, pessoa.data_nascimento)

    def excluir(self, pessoas):
        for pessoa in self.pessoas:
            if pessoa.nome == nome:
                self.pessoas.remove(pessoa)

    def pesquisa(self, pessoa):
        self.pesquisa(pessoa)
        try:
            return self.pessoas.index(pessoa)
        except ValueError:
            return -1


class responsavel_familiar(Pessoa):
    def __init__(self, *args, qtda_crianca, busca_prof, **kwargs):
        super(responsavel_familiar, self).__init__(*args, **kwargs)
        self.qtda_criança = qtde
        self.busca_prof = busca_prof

    @property
    def qtda_crianca(self):
        return self.__qtda_crianca

    @qtda_crianca.setter
    def qtda_crianca(self, valor):
        if valor == None or not valor.strip():
            raise ValueError("a quantidade de crianças não pode ser nulo nem em branco")

    def cadastrar(self):
        return self.cadastrar()

    def incluir_crianca(self):
        return self.incluir_criança()

    def excluir_crianca(self):
        return self.excluir_criança()

    def busca_professor(Professor):
        return self.busca_prof()

class Crianca(Pessoa):
    def __init__(self, *args, serie, senha, **kwargs):
        super().__init__(*args, **kwargs)
        self.serie = serie
        self.senha = senha

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, valor):
        if valor == None or not valor.strip():
            raise ValueError("A senha não pode ser nula nem em branco")

    def autenticar(self, serie, senha):
        return self.serie == serie and self.senha == senha

    def inserir_serie(self):
        return (self.serie)

    def trocar_serie(self):
        self.trocar_serie()

    def sair(self):
        self.sair(Criança) = False
        print("deslogado com sucesso")
#Depende do acesso da criança ao sistema, onde a quantidade de horas é
#dada pela subtração da hora_fim pela hora_inicio

class Historico_Interacao(Criança):
    def __init__(self, hora_inicio, hora_fim, question, percentual):
        self.inicio = hora_inicio
        self.fim = hora_fim
        self.question = question
        self.percentual = percentual

    def contar(Historico_Interacao):
        if percentual == None or not  valor.strip():
            raise ValueError ("Não há como traçar percentual. Nenhum acesso.")
        percentual = hora_fim - hora_inicio

class Professor(Pessoa):
    def __init__(self, *args, area, formacao, **kwargs):
        super(professor, self).__init__(*args, **kwargs)
        self.area = area
        self.formacao = formacao

    def incluir(self):
        return self.incluir()

    def excluir(self):
        return self.excluir()

#responsável por implementar métodos de comparação especiais (==, !=, >, <. >=, <=)
from functools import total_ordering
class TipoQuestion():
    def __init__(self, *args, disciplina, pergunta, resposta, feedback, ano, bimestre):
        self.disciplina = disciplina
        self.pergunta = pergunta
        self.resposta = resposta
        self.feedback = feedback
        self.ano = ano
        self.bimestre = bimestre

@property
def disciplina(self):
    return self.__disciplina
@disciplina.setter
def disciplina(self, valor):
    if valor == None or not valor.strip():
        raise ValueError("Disciplina não pode ser None ou em branco")
    self.__disciplina = valor

@property
def pergunta(self):
        return self.__pergunta

@pergunta.setter
def pergunta(self, valor):
    if valor == None or not valor.strip():
        raise ValueError("Pergunta não pode ser None ou em branco")
    self.__pergunta = valor

@property
def resposta(self):
    return self.__resposta
@resposta.setter
def resposta(self, valor):
    if valor == None or not valor.strip():
        raise ValueError("Disciplina não pode ser None ou em branco")
    self.__resposta = valor

# método str para exibir o nome da disciplina entre parenteses
    def __str__(self):
        return "({0})".format(self.disciplina)
#métodos eq e lt para ativar a comparação de questões por ano
    def __eq__(self, other):
        if other is None: #Compara None para quando não há informação de ano
            return False
        return self.ano == other.ano
    def __lt__(self, other):
        return self.ano < other.ano

#Transformando a classe TipoQuestion em uma Classe Lista Única

class ListaUnica
    def__init__(self, TipoQuestion):
        self.lista = []
        self.TipoQuestion = tipoQuestion
    def __len__(self):
        return len(self.lista)
    def __iter__(self):
        return iter(self.lista)
    def __getitem__(self, p):
        return self.lista[p]
    def indiceValido(sel, i):
        return i>=0 and i<len(self.lista)
    def adiciona(self, question):
        if self.pesquisa(question) == -1:
            self.lista.append(question)
    def remove(self, question):
        self.lista.remove(question)
    def pesquisa(self, question):
        self.verifica_tipo(question)
                raise TypeError("Tipo Invalido!")
            else:
                return self.question_class[posicao]
    def ordena(self, chave = None):
            self.lista.sort(key= chave)
    def validar():
        if resposta == True:
            feedback = resposta
            print("Você acertou")
        else:
            print("Tente responder novamente, não está correto!")

#Definindo uma classe Menu para acessar as questões no APPrendo
#Menu simples: opção sair como padrão, o método exibe mostra o menu na tela e percorre a lista de opções
#O método execute mostra continuamente o menu, pedindo uma escolha ao usuário
class Menu:
    def __init__(self):
        self.opcoes = [["Sair", None]]
    def adicionaopcao = (self, nome, funcao):
        self.opcoes.append([nome, funcao])
    def exibe(self):
        print("================")
        print("Menu")
        print("======\n")
        for i, opcao in enumerate(self.opcoes):
            print("[{0}] - {1}".format(i, opcao[0]))
        print()
    def execute(self):
        while True:
            self.exibe()
            escolha = valida_faixa_inteiro("Escolha uma opcao: ", 0, len(self.opcoes)-1)
            if escolha == 0:
                break
            self.opcoes[escolha][1]()

#Perpectiva para inicializar o APPrendo
print ("Digite seu nome: ")
nome = raw_input()
if nome != "":
    print("Olá, " + nome + "!")
else:
    while nome == "":
        print("Digite seu nome: ")
        nome = raw_input()
    print("Oi," + nome + "!")
    print("Inicie seus estudos!")
print("Até o próximo bloco")

#Como não tenho o banco de dados, a estrutura das perguntas no banco de dados seria algo como
base = {
    'Pergunta 01':{
        'pergunta':'Quanto é 4x4?',
        'alternatia':{'a':'12','b':'24','c':'16','d':'20'},
        'resposta_certa':'c',
    },
    'Pergunta 02':{
        'pergunta':'Quanto é 6 / 3?',
        'alternativas':{'a':'2','b':'1','c':'3','d':'4'},
        'resposta_certa':'a',
    },
}
respostas_certas = 0
for pkeys, pvalues in base.items():
    print(f'{pkeys}:{pvalues["pergunta"]}')

    for rkeys, rvalues in pvalues['alternativas'].items():
        print(f'[{rkeys}]:{rvalues}')

    resposta = input('Escolha uma alternativa: [a], [b], [c] ou [d]')

    if resposta == pvalues['resposta_certa']
        print("Resposta Correta!!!!")
        respostas_certas += 1
    else:
        print("Não é bem isso, responda novamente!")

    if respostas_certas == 0:
        print("Você não acertou nenhuma questão.")
    elif respostas_certas == 1:
        print("Você acertou 50% das questões.")
    else:
        print("Excelente! Você acertou 100% das questões")
