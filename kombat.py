import json

def who_initiates(secuence):
    count_mov_p1 = len([mov for mov in secuence['player1']['movimientos'] if mov != ''])
    count_str_p1 = len([str for str in secuence['player1']['golpes'] if str != ''])

    count_mov_p2 = len([mov for mov in secuence['player2']['movimientos'] if mov != ''])
    count_str_p2 = len([str for str in secuence['player2']['golpes'] if str != ''])

    total_p1 = count_mov_p1 + count_str_p1
    total_p2 = count_mov_p2 + count_str_p2

    if total_p1 > total_p2 or count_mov_p1 > count_mov_p2 or count_str_p1 > count_str_p2:
        return 'player2', 'player1'
    if total_p2 > total_p1 or count_mov_p2 > count_mov_p1 or count_str_p2 > count_str_p1:
        return 'player1', 'player2'

    return 'player1', 'player2'


def movement_special(combination, skills):
    for skill in skills.keys():
        if combination.endswith(skill):
            return skills[skill]


def printer_events(movement, hit, skills):
    movement = movement
    hit = hit
    special_hit =  movement_special(movement + hit, skills['special'])
    points = 0

    if special_hit:
        points = special_hit[1]
        print(f"{skills['name']} conecta un {special_hit[0]}")
    if not hit:
        print(f"{skills['name']} se mueve")
    if hit and not movement:
        points = 1
        print(f"{skills['name']} lanza una {skills['basic'][hit][0]}")
    if not special_hit and hit and movement:
        points = 1
        print(f"{skills['name']} se mueve y lanza un(a) {skills['basic'][hit][0]}")

    return points


def talana_kombat(secuence: list):
    try:
        secuence = json.loads(secuence)
    except Exception as e:
        raise ValueError('Ingrese un valor que con la sgte estructura: {"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}')

    skills = {
        'player1': {
            'name': 'Tonyn',
            'points': 5,
            'special': {
                'DSDP': ['Taladoken', 3],
                'SDK': ['Remuyuken', 2]
            },
            'basic': {
                'K': ['patada', 1],
                'P': ['puñete', 1]
            }
        },
        'player2': {
            'name': 'Arnaldor',
            'points': 5,
            'special': {
                'SAK': ['Remuyuken', 3],
                'ASAP': ['Taladoken', 2]
            },
            'basic': {
                'K': ['patada', 1],
                'P': ['puñete', 1]
            }
        }
    }

    init_player, end_player = who_initiates(secuence)

    index = 0
    while skills[init_player]['points'] > 0 and skills[end_player]['points']  > 0:

        if len(secuence[init_player]['movimientos']) > index:
            remaining_points_ip = printer_events(
                secuence[init_player]['movimientos'][index],
                secuence[init_player]['golpes'][index],
                skills[init_player]
            )

            skills[end_player]['points'] -= remaining_points_ip

        if len(secuence[end_player]['movimientos']) > index:
            remaining_points_ep = printer_events(
                secuence[end_player]['movimientos'][index],
                secuence[end_player]['golpes'][index],
                skills[end_player]
            )
            skills[init_player]['points'] -= remaining_points_ep

        index += 1

    if skills[init_player]['points'] <= 0:
        return print(f"{skills[end_player]['name']} gana la pelea y aun le queda {skills[end_player]['points']} de energía")
    else:
        return print(f"{skills[init_player]['name']} gana la pelea y aun le queda {skills[init_player]['points']} de energía")

secuence = input("Ingrese la secuencia de combate: ")
talana_kombat(secuence)
