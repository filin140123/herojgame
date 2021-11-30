# enemy init, reroll and corrections
from random import choice, randint

enemies_list = ['Zombie', 'Zombie', 'Warlock', 'Warlock',
                'Orc', 'Troll', 'Revenant', 'Ghost', 'Vampire', 'Marauder', 'Assassin', 'Bandit', 'Crusader', 'Gnome']

boss_list = ['Necromancer', 'Warchief', 'Alchemist']

undead_list = ['Zombie', 'Revenant', 'Ghost', 'Vampire', 'Necromancer', 'Horde of Zombies']

demonic_items = ['demonblade', 'soulring', 'stonemask']


def reroll_enemy(opponent):
    opponent['name'] = choice(enemies_list)
    opponent['mod'] = ''
    opponent['health'] = randint(60, 150)
    opponent['damage'] = randint(20, 40)
    opponent['crit_chance'] = 0
    opponent['crit_mul'] = 1.1
    opponent['armor'] = randint(105, 150) / 100
    opponent['lifesteal'] = False
    opponent['ls_coefficient'] = 8
    opponent['block_chance'] = randint(0, 10)
    opponent['gold'] = randint(5, 25)
    opponent['escape_bonus'] = 0
    opponent['bribe_value'] = randint(70, 130)
    opponent['persuade_bonus'] = 0
    opponent['banish_bonus'] = 0


def enemy_correction(opponent, hero, container):
    # bosses
    if hero['score'] % 10 == 0 and hero['score'] not in [0, 100]:
        opponent['name'] = choice(boss_list)
    if opponent['name'] == 'Warchief':
        opponent['block_chance'] = randint(10, 25)
        opponent['health'] = randint(200, 250)
        opponent['damage'] = randint(35, 60)
        opponent['armor'] = randint(140, 175) / 100
        opponent['crit_chance'] = 15
        opponent['crit_mul'] = 1.4
    if opponent['name'] == 'Necromancer':
        opponent['lifesteal'] = True
        opponent['health'] = randint(150, 200)
        opponent['damage'] = randint(45, 70)
        opponent['crit_chance'] += 15
        opponent['crit_mul'] += 1.25
    if opponent['name'] == 'Alchemist':
        opponent['health'] = randint(150, 200)
        opponent['damage'] = randint(45, 60)
        opponent['armor'] = randint(140, 175) / 100

    # common enemies
    if opponent['name'] == 'Zombie':
        opponent['health'] = randint(55, 90)
        opponent['armor'] = randint(105, 125) / 100
        opponent['block_chance'] = 0
        opponent['escape_bonus'] += 15
    if opponent['name'] == 'Vampire':
        opponent['lifesteal'] = True
        opponent['health'] = randint(60, 120)
        opponent['armor'] = randint(105, 125) / 100
    if opponent['name'] == 'Orc':
        opponent['health'] = randint(80, 160)
        opponent['block_chance'] += 5
    if opponent['name'] == 'Troll':
        opponent['health'] = randint(100, 160)
        opponent['armor'] = randint(140, 180) / 100
        opponent['block_chance'] += 10
        opponent['escape_bonus'] += 25
    if opponent['name'] == 'Revenant':
        opponent['damage'] = randint(33, 66)
        opponent['banish_bonus'] += 10
    if opponent['name'] == 'Ghost':
        opponent['block_chance'] = 0
        opponent['armor'] = 1
    if opponent['name'] == 'Warlock':
        opponent['block_chance'] = randint(1, 5)
        opponent['armor'] = randint(105, 125) / 100
        opponent['health'] = randint(60, 120)
        opponent['persuade_bonus'] += 5
    if opponent['name'] == 'Assassin':
        opponent['crit_chance'] += 20
        opponent['crit_mul'] += .95
        opponent['damage'] += 10
    if opponent['name'] == 'Marauder':
        opponent['crit_chance'] += 10
        opponent['crit_mul'] += .55
        opponent['damage'] += 10
        opponent['gold'] += 15
    if opponent['name'] == 'Bandit':
        opponent['damage'] += 10
        opponent['gold'] += 10
        opponent['armor'] += 0.1
        opponent['block_chance'] += 5
        opponent['persuade_bonus'] += 10
    if opponent['name'] == 'Gnome':
        opponent['persuade_bonus'] += 25
    if opponent['name'] == 'Crusader':
        opponent['damage'] += 15
        opponent['armor'] += 0.2
        opponent['block_chance'] += 5
        opponent['health'] += 50
        opponent['gold'] += 10
        if any(x not in container for x in demonic_items) and hero['class'] != 'Demonknight':
            opponent['persuade_bonus'] += 999

    enemy_mod(opponent)
    autoleveling(opponent, hero)


def enemy_mod(opponent):
    mod_chance = randint(1, 30)
    if mod_chance == 1:
        opponent['mod'] = 'Big '
        opponent['health'] += randint(60, 120)
    if mod_chance == 2 and opponent['name'] not in ['Troll', 'Ghost']:
        opponent['mod'] = 'Armored '
        opponent['armor'] += (.2 + (randint(5, 10) / 100))
    if mod_chance == 3 and opponent['lifesteal'] is False:
        opponent['mod'] = 'Blood-lusting '
        opponent['lifesteal'] = True
    if mod_chance in [4, 5] and opponent['name'] == 'Zombie':
        opponent['name'] = 'Horde of Zombies'
        opponent['health'] += 185
        opponent['damage'] += 5
        opponent['armor'] = 1
    if mod_chance == 6 and opponent['name'] not in ['Troll', 'Orc', 'Warlock']:
        opponent['mod'] = 'Weak '
        opponent['health'] -= 25
        opponent['damage'] -= 12
        opponent['block_chance'] = 0
    if mod_chance == 7 and all(opponent['name'] not in i for i in [boss_list, undead_list]):
        opponent['mod'] = 'Half-dead '
        opponent['health'] = 25
        opponent['damage'] -= 10
    if mod_chance == 8 and opponent['name'] not in boss_list:
        opponent['mod'] = 'Terrible '
        opponent['damage'] += 10
        opponent['crit_chance'] += 20
        opponent['crit_mul'] += (randint(4, 8) / 10)
    if mod_chance == 9 and opponent['name'] not in undead_list:
        opponent['mod'] = 'Wealthy '
        opponent['gold'] += 15
        opponent['health'] += 20
    if mod_chance == 10 and opponent['name'] != 'Assassin':
        opponent['mod'] = 'Slow '
        opponent['escape_bonus'] += 30
    if mod_chance == 11 and all(opponent['name'] not in i for i in [boss_list, undead_list]) and \
            opponent['name'] != 'Crusader':
        opponent['mod'] = 'Friendly '
        opponent['persuade_bonus'] += 999


def autoleveling(opponent, hero):
    opponent['level'] = int(hero['score'] / 10)
    opponent['bribe_value'] += opponent['level'] * 10
    opponent['health'] += opponent['level'] * 15
    opponent['damage'] += opponent['level'] * 2
    opponent['crit_chance'] += opponent['level'] * 2
    opponent['crit_mul'] += opponent['level'] * .1
    opponent['gold'] += opponent['level'] * 5
    if opponent['armor'] > opponent['max_armor']:
        opponent['armor'] = opponent['max_armor']


if __name__ == "__main__":
    enemy_correction(opponent, hero, container)
    enemy_mod(opponent)
    autoleveling(opponent, hero)
    reroll_enemy(opponent)
