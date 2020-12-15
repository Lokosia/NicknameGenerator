#Nickname Generator
import random

lib_solo = ['Samnium', 'Larnum', 'Latium', 'Dakkar', 'Lokosia', 'Пивасилий',
            'Квасилий', 'Infractor', 'POLICER', 'Трогательный']

lib_1 = ['Disco', 'Super', 'Party', 'Crazy']
lib_2 = ['Super', 'DJ', 'Mega', 'Porno', 'Midnight']
lib_3 = ['Star', 'MC', 'Killer', 'Dancer']

length = random.randint(1, 3)

if length == 1:
    result = random.choice(lib_solo)

if length != 1:
    ok = False
    while not ok:
        res_1 = random.choice(lib_1)
        res_2 = random.choice(lib_2)
        res_3 = random.choice(lib_3)
        if res_1 != res_2:
            if length == 2:
                if res_2 != 'Super' and res_2 != 'Mega' and res_2 != 'Midnight':
                    ok = True
            else:
                ok = True
    if length == 2:
        result = res_1 + res_2
    else:
        result = res_1 + res_2 + res_3
print(result)
