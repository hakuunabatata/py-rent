print('===-===-===-===-===')
print('Bem-vindo a locadora de carros')
print('===-===-===-===-===')


def rent():
    show(True)

    print('\n\n\n')
    car = int(input('Qual carro quer alugar?\n'))

    days = int(
        input(f'Voce quer alugar {cars[car]["name"]} por quantos dias?\n')
    )

    print(
        f'O aluguel de {cars[car]["name"]} por {days} dias ficará um total de R$ {(cars[car]["price"] * days):.2f}\n')

    cars[car]["available"] = False


def show(available=True):
    print('===-===-===-===-===')
    print('Aluguel')
    print('===-===-===-===-===')

    index = 0
    for x in cars:
        if (x['available'] == available):
            print(f'[{index}] - {x["name"]} = R$ {x["price"]:.2f} / dia')
        index += 1

    print('\n\n\n\n')


def getBack():
    show(False)

    car = int(input('Qual carro quer devolvar?\n'))

    print(f'{cars[car]["name"]}  sendo devolvido')

    cars[car]['available'] = True


actions = [
    {
        'name': 'Mostrar portifolio',
        'function': show
    },
    {
        'name': 'Alugar um carro',
        'function': rent
    },
    {
        'name': 'Devolver um carro',
        'function': getBack
    }
]

cars = [
    {
        'name': 'Chevrolet Corsa',
        'price': 20,
        'available': True
    },
    {
        'name': 'Chevrolet Celta',
        'price': 15,
        'available': True
    },
    {
        'name': 'VW Fusca',
        'price': 35,
        'available': True
    },
    {
        'name': 'VW Brasilia',
        'price': 38,
        'available': True
    },
    {
        'name': 'Fiat Uno',
        'price': 20,
        'available': True
    },
    {
        'name': 'Fiat Uno da Net com Escada',
        'price': 200,
        'available': True
    }
]

repeat = True


while (repeat):
    index = 0

    print('\n\nOque deseja fazer ?')
    question = []
    for x in actions:
        question.append(f'{index} - {x["name"]}')
        index += 1

    action = int(input(' | '.join(question) + '\n'))

    actions[action]['function']()

    if (int(input('1 - Continuar | 0 - Sair\n')) == 0):
        repeat = False
