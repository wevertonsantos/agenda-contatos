'''
O que essa agenda irá ter?
1.adicionar contato
2.remover contato
4.alterar contato
3.listar contato
4.buscar contato

O que o contato terá?
pessoa:
    1.nome
    2.telefone

A lista de contato irá ter as funcionalidades de:
1.remover
2.adicionar
3.alterar
4.buscar
5.listar todos
'''

class Contato:
    def __init__(self,nome,telefone):
        self.nome = nome
        self.telefone = telefone

class Agenda:
    def __init__(self):
        self.lista_contatos = {}

    def adicionar_contato(self,nome,telefone):
        contato = Contato(nome,telefone)
        self.lista_contatos[nome] = contato.telefone
    
    def remover_contato(self,nome):
        if nome in self.lista_contatos:
            self.lista_contatos.pop(nome)
            print(f"Contato '{nome}' removido com sucesso.")
        else:
            print(f"Contato '{nome}' não encontrado.")
    
    def alterar_contato(self,nome,telefone):
        if nome in self.lista_contatos:
            self.lista_contatos.update({nome: telefone})
            print(f"Contato '{nome}' alterado com sucesso.")
        else:
            print(f"Contato '{nome}' não encontrado.")

    def buscar_contato(self,nome):
        if nome in self.lista_contatos:
            print(f"Contato: {nome}, telefone: {self.lista_contatos[nome]}")
        else:
            print(f"Contato '{nome}' não encontrado.")
    
    def listar_contatos(self):
        for contato in self.lista_contatos:
            print(f"Contato: {contato}, telefone: {self.lista_contatos[contato]}")


agenda = Agenda()
agenda.adicionar_contato("Maria","11999")
agenda.adicionar_contato("Julio","19888")
agenda.alterar_contato("Julio","11922")
agenda.listar_contatos()
print(agenda.lista_contatos)