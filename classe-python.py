class Carro:
    def __init__(self, marca, modelo, ano, cor, preço):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__preço = preço

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_ano(self):
        return self.__ano

    def get_cor(self):
        return self.__cor

    def get_preco(self):
        return self.__preço