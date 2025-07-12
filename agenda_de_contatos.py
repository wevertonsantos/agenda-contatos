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
    
    def remover_contato(self,nome,telefone):
        if nome in self.lista_contatos:
            self.lista_contatos.pop()

agenda = Agenda()
print(agenda.adicionar_contato("Maria","11988443300"))
print(agenda.adicionar_contato("Julio","11985243400"))
print(agenda.remover_contato("Julio","11985243400"))
print(agenda.lista_contatos)