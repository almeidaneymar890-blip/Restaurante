from modelo.restaurante import Restaurante


bistro_paris = Restaurante('BiStRô Paris', 'FRANCESA')
sushi_zen = Restaurante('sushi zen', 'jAPOSENA')
# cantina_roma = Restaurante('CANtina ROMA', 'Italiana')
# burger_king = Restaurante('Burger King', 'Fast Food')
# taco_loco = Restaurante('Taco Loco', 'Mexicana')
# churrascaria_sul = Restaurante('Churrascaria Pampa', 'Carnes')
# vegan_delight = Restaurante('Vegan Delight', 'Vegetariana')
# padaria_central = Restaurante('Padaria Central', 'Panificadora')
# cafe_amargo = Restaurante('Café Amargo', 'Cafeteria')
# sorveteria_gelo = Restaurante('Sorveteria Gelo', 'Sobremesas')
# mar_aberto = Restaurante('Mar Aberto', 'Frutos do Mar')
# kebab_house = Restaurante('Kebab House', 'Árabe')
# thai_spicy = Restaurante('Thai Spicy', 'Tailandesa')
# doceria_fina = Restaurante('Doceria Fina', 'Confeitaria')
# boteco_esquina = Restaurante('Boteco da Esquina', 'Bar e Petiscos')

Restaurante.listar_restaurantes(Restaurante)

bistro_paris.receber_avaliacao('jose', 5)
arroz = Prato('Arroz Branco', 30.00, 'Arroz Bom e Barato')
bistro_paris.adicionar_no_cardapio(arroz)

Restaurante.listar_restaurantes(Restaurante)