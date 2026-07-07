from modelo.avaliacao import Avaliacao
from modelo.cardapio.item_cardapio import ItemCardapio




class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._cardapio = []
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do Restaurante'.ljust(25)}| {'Categoria'.ljust(25)} | {'Avaliações'.ljust(25)}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.media_avaliacao}')

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)
    @property
    def media_avaliacao(self):
        soma = 0
        for avaliacao in self._avaliacoes:
            soma += avaliacao._nota

        try:
            media = soma / len(self._avaliacoes)
            return round(media, 1)
        except ZeroDivisionError:
            return 0.0

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

        else:
            print(f'Erro: O item fornecido não é um item de cardápio válido.')

    @property
    def exibir_cardapio(self):
        print(f"Cardápio do Restaurante {self._nome}\n")
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item,'descricao'):
                print(f'{i}. [Prato] {item._nome} - R${item._preco:.2f} | {item.descricao}')
            elif hasattr(item,'tamanho'):
                  print(f'{i}. [Bedida] {item._nome} - R${item._preco:.2f} | {item.tamanho}')
