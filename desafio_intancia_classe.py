class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_japones = Restaurante()
restaurante_japones.nome = 'Temaki'
restaurante_japones.categoria = 'Japonesa'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Hut'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

restaurantes = [restaurante_japones, restaurante_pizza]

nome_restaurante1 = restaurante_japones.nome
nome_restaurante2 = restaurante_pizza.nome
categoria = Restaurante.categoria

print(f'''
    Nome do restaurante: {restaurante_japones.nome}
    Categoria do restaurante: {restaurante_japones.categoria}
    Restaurante ativo: ''',end='')

if restaurante_japones.ativo:
    print(f'O restaurante está ativo.\n')
else:
    print(f'O restaurante não está ativo.\n')



if restaurante_pizza.categoria == 'Fast Food':
    print(f'A categoria do restaurante {nome_restaurante2} é {restaurante_pizza.categoria}.')
else :
    print(f'A categoria do restaurante {nome_restaurante2} não é Fast Food.')
