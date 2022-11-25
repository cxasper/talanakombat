import json

def who_initiates(secuence):
    count_mov_p1 = len([mov for mov in secuence['player1']['movimientos'] if mov != ''])
    count_str_p1 = len([mov for mov in secuence['player1']['golpes'] if mov != ''])

    count_mov_p2 = len([mov for mov in secuence['player2']['movimientos'] if mov != ''])
    count_str_p2 = len([mov for mov in secuence['player2']['golpes'] if mov != ''])

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

def printer_events(secuence: list):

    try:
        secuence = json.loads(secuence)
        # secuence = {"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}
    except Exception as e:
        raise ValueError('Ingrese un valor que con la sgte estructura: {"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}')

    skills = {
        'player1': {
            'name': 'Tonyn',
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

    points_p1 = 5
    points_p2 = 5

    init_player, end_player = who_initiates(secuence)

    for index, movement in enumerate(secuence[init_player]['movimientos']):
        hit = secuence[init_player]['golpes'][index]
        special_hit =  movement_special(
            movement + hit, skills[init_player]['special']
        )

        if special_hit:
            points_p2 -= special_hit[1]
            print(f"{skills[init_player]['name']} conecta un {special_hit[0]}")
        if not hit:
            print(f"{skills[init_player]['name']} se mueve")
        if hit and not movement:
            points_p2 -= 1
            print(f"{skills[init_player]['name']} lanza una {skills[init_player]['basic'][hit][0]}")
        if not special_hit and hit and movement:
            points_p2 -= 1
            print(f"{skills[init_player]['name']} se mueve y lanza un(a) {skills[init_player]['basic'][hit][0]}")
        if points_p2 <= 0:
            return print(f"{skills[init_player]['name']} gana la pelea y aun le queda {points_p2}")


        movement = secuence[end_player]['movimientos'][index]
        hit = secuence[end_player]['golpes'][index]
        special_hit =  movement_special(
            movement + hit, skills[end_player]['special']
        )

        if special_hit:
            points_p1 -= special_hit[1]
            print(f"{skills[end_player]['name']} conecta un {special_hit[0]}")
        if not hit:
            print(f"{skills[end_player]['name']} se mueve")
        if hit and not movement:
            points_p1 -= 1
            print(f"{skills[end_player]['name']} lanza una {skills[end_player]['basic'][hit][0]}")
        if not special_hit and hit and movement:
            points_p1 -= 1
            print(f"{skills[end_player]['name']} se mueve y lanza un(a) {skills[end_player]['basic'][hit][0]}")
        if points_p1 <= 0:
            return print((f"{skills[end_player]['name']} gana la pelea y aun le queda {points_p2}"))

secuence = input()
printer_events(secuence)
