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
        if len(nome) > 0 and len(telefone) > 0:
            if not telefone.isdigit():
                print("Número de telefone inválido!")
            else:
                contato = Contato(nome,telefone)
                self.lista_contatos[nome] = contato.telefone
        else:
            print("Você digitou dados vazio. Tente novamente!")
    
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
        if len(self.lista_contatos) > 0:
            for contato in self.lista_contatos:
                print(f"Contato: {contato}, telefone: {self.lista_contatos[contato]}")
        else:
            print("Lista de contatos vazia")

def main():
    agenda = Agenda()
    while True:
        try:
            escolha = int(input("1. Listar contatos\n2. Adicionar contato\n3. Remover contato\n4. Alterar contato\n5. Buscar contato\n6. Sair\nEscolha uma opção: "))
            if escolha == 1:
                agenda.listar_contatos()
            elif escolha == 2:
                nome_novo_contato = input("Digite o nome do contato que gostaria: ").strip().title()
                numero_novo_contato = input("Digite o número do contato: ")
                agenda.adicionar_contato(nome_novo_contato,numero_novo_contato)
            elif escolha == 3:
                nome_contato_para_remover = input("Digite o nome do contato que deseja remover: ").strip().title()
                agenda.remover_contato(nome_contato_para_remover)
            elif escolha == 4:
                nome_contato_para_alterar = input("Digite o nome do contato que deseja alterar: ").strip().title()
                numero_contato_para_alterar = input("Digite o novo número do contato: ")
                agenda.alterar_contato(nome_contato_para_alterar,numero_contato_para_alterar)
            elif escolha == 5:
                nome_contato_para_buscar = input("Digite o nome do contato para buscar: ").strip().title()
                agenda.buscar_contato(nome_contato_para_buscar)
            elif escolha == 6:
                print("Você saiu da agenda!")
                break
        except ValueError:
            print("Você digitou algo errado!")

main()