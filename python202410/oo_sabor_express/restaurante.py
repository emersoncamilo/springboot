class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

rest1 = Restaurante('Pizza', 'Italiano')
rest2 = Restaurante('Gregorio', 'Grego')
# restaurante1 = Restaurante()

# restaurantes = [restaurante1]

# print(vars(restaurante1))

Restaurante.listar_restaurantes()