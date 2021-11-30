from random import randint, choice

from colorama import Fore, Back, Style, init

from descriptions import *
from control_scheme import syntax_dict, creator_list, appendnames
from enemy_lib import enemy_correction, reroll_enemy, enemies_list, boss_list, undead_list
from inspect_lib import inspect_enemy, show_attributes, show_player_info, show_inventory, controls
from player_lib import inventory_check, rename, attribute_up, exp_points
from hero_classes import *
from hud import status

init()  # starting colorama

game_title = "The Hero's Journey"
game_title_len = len(game_title)

print(Fore.MAGENTA, end="")
print("╔" + "═" * (game_title_len + 2) + "╗")
print(f"║ {game_title} ║")
print("╚" + "═" * (game_title_len + 2) + "╝")
print(Style.RESET_ALL, end="")

player_name = input('Enter the name: ')
if player_name == '':
    player_name = 'John'

player = {
    'name': player_name,
    'class': '',
    'health': 100,
    'max_health': 100,
    'damage': 35,
    'crit_chance': 10,
    'crit_mul': 1.5,
    'armor': 1.1,
    'max_armor': 1.8,
    'healing_potions': 0,
    'potion_effect': 25,
    'allow_potions': True,
    'fireballs': 0,
    'fireball_dmg': 100,
    'bomb_dmg': 9,
    'lifesteal': False,
    'ls_coefficient': 8.0,
    'block_chance': 10,
    'escape_chance': 30,
    'persuade_chance': 10,
    'gold_bonus': 0,
    'stew_bonus': 0,
    'repair_armor_bonus': 0.01,
    'training_bonus': 0,
    'crit_training_bonus': 0,
    'banish_heal': 0,
    'discount': 0,
    'inv_size': 10,
    'score': 0,
    'gold': 0,
    'exp_points': 1,
}

player_attributes = {
    'STR': 0,
    'PER': 0,
    'END': 0,
    'CHR': 0,
    'INT': 0,
    'RCT': 0,
    'SRV': 0,
}

player_inventory = ['flask']


def character_creator():
    print(Fore.CYAN + f"1: Warrior, 2: Mage, 3: Thief, 4: Demonknight, 5: Bard, 6: Priest" + Style.RESET_ALL)
    while True:
        try:
            c_choise = input(f"\nChoose your class (type number or 'i' to inspect): ")

            print(Fore.BLACK + Back.WHITE)

            if c_choise in ['1', '']:
                warrior_class(player, player_inventory)
            if c_choise == '2':
                mage_class(player, player_inventory)
            if c_choise == '3':
                thief_class(player, player_inventory)
            if c_choise == '4':
                demonknight_class(player, player_inventory)
            if c_choise == '5':
                bard_class(player, player_inventory)
            if c_choise == '6':
                priest_class(player, player_inventory)

            if c_choise in syntax_dict['quit_list']:
                print(Style.RESET_ALL + "Bye!", end='')
                input()
                quit()

            if c_choise in syntax_dict['inspect_list']:
                print(Style.RESET_ALL, end='')
                print(classes_desc)
                continue

            if c_choise not in creator_list:
                print(Style.RESET_ALL, end='')
                print(Fore.RED + er_msg_crea + Style.RESET_ALL)
                continue

            inventory_check(player, player_inventory)
            print(Style.RESET_ALL, end='')
            break

        except IndexError:
            pass


merchant_stock = ['potion', 'scroll', 'stew', 'armorkit', 'whetstone', 'powder', 'acidbomb', 'slimebomb',
                  'smokebomb', 'banisher', 'redpepper', 'backpack']


def merchant_event():
    merch = choice(merchant_stock)

    # merchant item correction
    if player['class'] == 'Demonknight':
        while merch == 'banisher':
            merch = choice(merchant_stock)
    if 'redpepper' in player_inventory:
        while merch == 'redpepper':
            merch = choice(merchant_stock)
    if player['inv_size'] == 16:
        while merch == 'backpack':
            merch = choice(merchant_stock)

    # price correction
    price = (randint(50, 99) - player['discount'] + (enemy['level'] * 10))
    if merch == 'backpack':
        price += 300

    print(Fore.YELLOW + Back.BLACK + f"\nYou've met the merchant. He offers you the "
          + Fore.MAGENTA + f"{merch} " + Fore.YELLOW + f"for {price} gold" + Style.RESET_ALL)

    m_choice = input(f"Wanna buy it? ([yes] or [y]): ")
    m_choice = m_choice.lower()

    print(Fore.BLACK + Back.YELLOW)

    if m_choice in ['y', 'yes'] and player['gold'] >= price:
        if merch == 'potion':
            player['healing_potions'] += 1
            print(merch_msgs['potion'])
        if merch == 'acidbomb':
            player_inventory.append('acidbomb')
            print(merch_msgs['acidbomb'])
        if merch == 'smokebomb':
            player_inventory.append('smokebomb')
            print(merch_msgs['smokebomb'])
        if merch == 'slimebomb':
            player_inventory.append('slimebomb')
            print(merch_msgs['slimebomb'])
        if merch == 'scroll':
            player['fireballs'] += 1
            print(merch_msgs['scroll'])
        if merch == 'stew':
            player['max_health'] += (10 + player['stew_bonus'])
            player['health'] = player['max_health']
            print(merch_msgs['stew'], f"+{10 + player['stew_bonus']}")
        if merch == 'armorkit':
            player['armor'] += (.03 + player['repair_armor_bonus'])
            if player['armor'] > player['max_armor']:
                player['armor'] = player['max_armor']
            print(merch_msgs['armorkit'], f"{int((.03 + player['repair_armor_bonus']) * 100)}% armor")
        if merch == 'whetstone':
            player['damage'] += 4
            print(merch_msgs['whetstone'])
        if merch == 'powder':
            player['crit_chance'] += 4
            print(merch_msgs['powder'])
        if merch == 'banisher':
            player_inventory.append('banisher')
            print(merch_msgs['banisher'])
        if merch == 'redpepper':
            player_inventory.append('redpepper')
            print(merch_msgs['redpepper'])
        if merch == 'backpack':
            player['inv_size'] += 2
            print(merch_msgs['backpack'])
        player['gold'] -= price
    elif m_choice in ['y', 'yes'] and player['gold'] < price:
        print(Style.RESET_ALL + "Sorry, you don't have enough gold to buy this!")
    print(Style.RESET_ALL + "Merchant waves to you while you go...")


enemy = {  # enemy stat sheet
    'name': choice(enemies_list),
    'mod': '',
    'health': randint(60, 150),
    'max_health': 999,
    'damage': randint(20, 40),
    'crit_chance': 0,
    'crit_mul': 1.05,
    'armor': randint(105, 150) / 100,
    'max_armor': 1.8,
    'lifesteal': False,
    'ls_coefficient': 8,
    'block_chance': randint(0, 10),
    'escape_bonus': 0,
    'level': 0,
    'gold': randint(5, 25),
    'bribe_value': 100,
    'persuade_bonus': 0,
    'banish_bonus': 0,
}


def attack(unit, target):
    # calc block chance
    block = randint(1, 100)
    if block <= target['block_chance']:
        print(Back.BLUE + f"\n--- {target['name']} blocked {unit['name']}'s attack!:" + Style.RESET_ALL)
        status(player, enemy, undead_list, boss_list)
    else:
        # calc armor based dmg
        armor_based_dmg = int(unit['damage'] * (2 - target['armor']))
        # calc crit chance and dmg
        crit = randint(1, 100)
        if crit <= unit['crit_chance'] != 0:
            armor_based_dmg = int(armor_based_dmg * unit['crit_mul'])
            crit_note = ' by critical strike!'
        else:
            crit_note = ''
        # calc dmg and print
        target['health'] -= armor_based_dmg
        print(
            Back.RED +
            f"\n--- {unit['name']} attacks {target['name']} for {armor_based_dmg}({unit['damage']}) dmg{crit_note}:"
            + Style.RESET_ALL
        )
        status(player, enemy, undead_list, boss_list)
        # lifesteal check
        if unit['lifesteal'] is True:
            healing(unit, round(armor_based_dmg / unit['ls_coefficient']), ' by vampirism')


def fireball_attack(unit, target):  # isolated
    if unit['fireballs'] > 0:
        unit['fireballs'] -= 1
        target['health'] -= unit['fireball_dmg']
        print(Back.RED + f"\n--- {unit['name']} fireballing {target['name']} for {unit['fireball_dmg']} pure dmg:")
        print(Style.RESET_ALL, end='')
        status(player, enemy, undead_list, boss_list)
    else:
        print(Fore.BLACK + Back.WHITE + f"\nYou don't have fireball scrolls!" + Style.RESET_ALL)


def acidbomb():
    if 'acidbomb' in player_inventory:
        player_inventory.remove('acidbomb')
        enemy['armor'] = 1.0
        enemy['health'] -= (player['bomb_dmg'] + 3)
        print(
            Back.MAGENTA + f"\n--- {player['name']} throw acidbomb on {enemy['name']}, "
                           f"enemy's armor destroyed and {player['bomb_dmg']} pure dmg dealt:" + Style.RESET_ALL)
        status(player, enemy, undead_list, boss_list)
    else:
        print(Fore.BLACK + Back.WHITE + f"\nYou don't have that bomb!" + Style.RESET_ALL)


def slimebomb():
    if 'slimebomb' in player_inventory:
        player_inventory.remove('slimebomb')
        enemy['damage'] = int(enemy['damage'] / 3)
        enemy['health'] -= (player['bomb_dmg'] - 3)
        print(
            Back.MAGENTA + f"\n--- {player['name']} throw slimebomb on {enemy['name']}, "
                           f"enemy's dmg decreased to 1/3 and {player['bomb_dmg']} pure dmg dealt:" + Style.RESET_ALL)
        status(player, enemy, undead_list, boss_list)
    else:
        print(Fore.BLACK + Back.WHITE + f"\nYou don't have that bomb!" + Style.RESET_ALL)


def smokebomb():
    if 'smokebomb' in player_inventory:
        player_inventory.remove('smokebomb')
        enemy['escape_bonus'] += 50
        enemy['health'] -= (player['bomb_dmg'] - 9)
        print(
            Back.MAGENTA + f"\n--- {player['name']} throw smokebomb on {enemy['name']}, "
                           f"escape chance increased by 50% and {player['bomb_dmg'] - 9} pure dmg dealt:"
            + Style.RESET_ALL)
        status(player, enemy, undead_list, boss_list)
    else:
        print(Fore.BLACK + Back.WHITE + f"\nYou don't have that bomb!" + Style.RESET_ALL)


def soulorb(hero, container, opponent):
    if 'soulorb' in container:
        container.remove('soulorb')
        orb_effect = int(30 + (hero['damage'] / hero['ls_coefficient']))
        hero['health'] += orb_effect
        if hero['health'] >= hero['max_health']:
            hero['health'] = hero['max_health']
        opponent['health'] -= orb_effect
        print(Back.MAGENTA + f"\n--- {hero['name']} using soulorb on {opponent['name']} and steal {orb_effect} health:")
        print(Style.RESET_ALL, end='')
        status(player, enemy, undead_list, boss_list)
    else:
        print(Fore.BLACK + Back.WHITE + f"\nYou don't have that orb!" + Style.RESET_ALL)


def banisher(hero, opponent, container, undead_l):
    if 'banisher' in container and opponent['name'] in undead_l:
        container.remove('banisher')
        b_ef = hero['banish_heal'] + opponent['banish_bonus']
        opponent['health'] -= 999
        print(Back.MAGENTA + f"\n--- {hero['name']} banishing {opponent['name']} and heals {b_ef} health:")
        print(Style.RESET_ALL, end='')
        status(player, enemy, undead_list, boss_list)
    elif 'banisher' in container and opponent['name'] not in undead_l:
        print(Fore.BLACK + Back.WHITE + f"\nYou can't banish living enemy!" + Style.RESET_ALL)
    else:
        print(Fore.BLACK + Back.WHITE + f"\nYou don't have banisher!" + Style.RESET_ALL)


def healing(unit, heal_amount, source=''):  # isolated
    before = unit['health']
    unit['health'] += int(heal_amount)
    if unit['health'] > unit['max_health']:
        unit['health'] = unit['max_health']
    actual_heal = unit['health'] - before
    print(Back.GREEN + Fore.BLACK + f"\n--- {unit['name']} heals {actual_heal}({heal_amount}) of health{source}:")
    print(Style.RESET_ALL, end='')
    status(player, enemy, undead_list, boss_list)


def healing_potion():
    if player['healing_potions'] > 0:
        player['healing_potions'] -= 1
        healing(player, player['potion_effect'], ' by potion')
    else:
        print(Fore.BLACK + Back.WHITE + f"\nYou don't have healing potions!" + Style.RESET_ALL)


def gold(hero, opponent):
    hero['gold'] += (opponent['gold'] + hero['gold_bonus'])
    print(Back.YELLOW + Fore.BLACK + f"\nYou found {opponent['gold'] + hero['gold_bonus']} gold! ({hero['gold']} now)")


def loot():
    merchant_chance = randint(1, 4)
    potion_drop_chance = randint(1, 10)
    stew_drop_chance = randint(1, 15)
    armor_event_chance = randint(1, 10)
    training_event_chance = randint(1, 10)
    fireball_drop_chance = randint(1, 10)
    stonemask_drop_chance = randint(1, 10)
    demonblade_drop_chance = randint(1, 10)
    shield_drop_chance = randint(1, 10)
    ghost_debuff_chance = randint(1, 10)
    gloves_drop_chance = randint(1, 10)
    bomb_drop_chance = randint(1, 20)
    speedboots_drop_chance = randint(1, 10)
    soulorb_drop_chance = randint(1, 10)
    coolhat_drop_chance = randint(1, 10)
    skillpoint_drop_chance = randint(1, 10)
    luckycoin_drop_chance = randint(1, 10)
    rosary_drop_chance = randint(1, 10)
    banisher_drop_chance = randint(1, 2)
    sword_drop_chance = randint(1, 10)
    armorpants_drop_chance = randint(1, 10)

    print(Back.WHITE + Fore.BLACK, end='')

    if sword_drop_chance == 10 and all(x not in player_inventory for x in ['demonblade', 'sword']) \
            and ic('sword') and enemy['name'] in ['Orc', 'Assassin', 'Marauder']:
        player_inventory.append('sword')
        player['damage'] += 15
        print(loot_msgs['sword'])
    if armorpants_drop_chance == 10 and 'armorpants' not in player_inventory and ic('armorpants') \
            and enemy['name'] in ['Bandit', 'Crusader', 'Orc']:
        player_inventory.append('armorpants')
        player['armor'] += .2
        print(loot_msgs['armorpants'])
    if luckycoin_drop_chance > 8 and enemy['name'] == 'Gnome' and \
            'luckycoin' not in player_inventory and ic('luckycoin'):
        player_inventory.append('luckycoin')
        player['gold_bonus'] += 5
        print(loot_msgs['luckycoin'])
    if rosary_drop_chance > 8 and enemy['name'] == 'Crusader' and 'rosary' not in player_inventory and ic('rosary'):
        player_inventory.append('rosary')
        player['banish_heal'] += 10
        print(loot_msgs['rosary'])
    if skillpoint_drop_chance == 10:
        player['exp_points'] += 1
        print(Back.CYAN + Fore.BLACK + loot_msgs['exp_point'] + Back.WHITE + Fore.BLACK)
    if coolhat_drop_chance == 10 and enemy['name'] == 'Troll' and 'coolhat' not in player_inventory and ic('coolhat'):
        player_inventory.append('coolhat')
        player['persuade_chance'] += 10
        print(loot_msgs['coolhat'])
    if bomb_drop_chance == 1 and enemy['name'] not in undead_list and ic('acidbomb'):
        player_inventory.append('acidbomb')
        print(loot_msgs['acidbomb'])
    elif bomb_drop_chance == 2 and enemy['name'] not in undead_list and ic('slimebomb'):
        player_inventory.append('slimebomb')
        print(loot_msgs['slimebomb'])
    elif bomb_drop_chance == 3 and enemy['name'] not in undead_list and ic('smokebomb'):
        player_inventory.append('smokebomb')
        print(loot_msgs['smokebomb'])
    if soulorb_drop_chance > 8 and enemy['name'] in undead_list and ic('soulorb'):
        player_inventory.append('soulorb')
        print(loot_msgs['soulorb'])
    if 7 < potion_drop_chance < 10 and enemy['name'] != 'Zombie' and player['allow_potions'] is True:
        player['healing_potions'] += 1
        print(loot_msgs['one_potion'], f"({player['healing_potions']} now)")
    elif potion_drop_chance == 10 and enemy['name'] != 'Zombie' and player['allow_potions'] is True:
        player['healing_potions'] += 2
        print(loot_msgs['two_potion'], f"({player['healing_potions']} now)")
    elif stew_drop_chance in [14, 15]:
        player['max_health'] += (10 + player['stew_bonus'])
        player['health'] = player['max_health']
        print(loot_msgs['stew'], f"and max health +{10 + player['stew_bonus']} ({player['max_health']} now)")
    if armor_event_chance in [1, 2]:
        player['armor'] += (.02 + player['repair_armor_bonus'])
        if player['armor'] > player['max_armor']:
            player['armor'] = player['max_armor']
        print(loot_msgs['armor_up'], f"+{int((.02 + player['repair_armor_bonus']) * 100)}% armor",
              f"({round(player['armor'], 2)} now)")
    elif armor_event_chance in [3, 4]:
        player['armor'] -= .04
        if player['armor'] < 1.0:
            player['armor'] = 1.0
        print(Back.RED + Fore.WHITE + loot_msgs['armor_down'], f"({round(player['armor'], 2)} now)"
              + Back.WHITE + Fore.BLACK)
    if training_event_chance == 1:
        player['damage'] += (2 + player['training_bonus'])
        print(loot_msgs['training_dmg'], f"{2 + player['training_bonus']} dmg! ({player['damage']} now)")
    elif training_event_chance == 2:
        player['block_chance'] += 1
        print(loot_msgs['training_block'], f"({player['block_chance']}% now)")
    elif training_event_chance == 3:
        player['crit_mul'] += (.05 + player['crit_training_bonus'])
        print(loot_msgs['training_critmul'], f"({int(player['crit_mul'] * 100)}% now)")
    if 3 < fireball_drop_chance < 9 and enemy['name'] in ['Warlock', 'Revenant']:
        player['fireballs'] += 1
        print(loot_msgs['fireball'], f"({player['fireballs']} now)")
    elif fireball_drop_chance > 8 and enemy['name'] == 'Warlock' and \
            'firebook' not in player_inventory and ic('firebook'):
        player_inventory.append('firebook')
        player['fireball_dmg'] += 25
        player['fireballs'] += 1
        print(loot_msgs['firebook'])
    if stonemask_drop_chance > 7 and enemy['name'] == 'Vampire' and ic('stonemask') and \
            all(x not in player_inventory for x in ['stonemask', 'soulring']) and player['class'] != 'Priest':
        sm_cons = input("You've found Stonemask. Do you want to take it? (Demonic item)")
        if sm_cons in ['yes', 'y']:
            player_inventory.append('stonemask')
            player['lifesteal'] = True
            print(loot_msgs['stonemask'])
    if demonblade_drop_chance > 8 and enemy['name'] == 'Marauder' and \
            'demonblade' not in player_inventory and player['class'] != 'Priest' and ic('demonblade'):
        db_cons = input("You've found Demonblade. Do you want to take it? (Demonic item)")
        if db_cons in ['yes', 'y']:
            if 'sword' in player_inventory:
                player_inventory.remove('sword')
                player['damage'] += 15
                print(loot_msgs['dblade_sw'])
            else:
                player['damage'] += 25
                print(loot_msgs['dblade_nosw'])
        player_inventory.append('demonblade')
    if shield_drop_chance > 8 and enemy['name'] == 'Orc' and 'shield' not in player_inventory and ic('shield'):
        player_inventory.append('shield')
        player['block_chance'] += 8
        print(loot_msgs['shield'])
    if ghost_debuff_chance < 3 and enemy['name'] == 'Ghost':
        player['damage'] -= 5
        player['max_health'] -= 5
        if player['health'] > player['max_health']:
            player['health'] = player['max_health']
        print(Back.RED + Fore.WHITE + loot_msgs['ghost_debuff'] + Back.WHITE + Fore.BLACK)
    if speedboots_drop_chance > 8 and enemy['name'] == 'Bandit' and \
            'speedboots' not in player_inventory and ic('speedboots'):
        player_inventory.append('speedboots')
        player['escape_chance'] += 10
        print(loot_msgs['speedboots'])
    if enemy['name'] == 'Warchief' and 'wristbands' not in player_inventory and ic('wristbands'):
        player_inventory.append('wristbands')
        player['armor'] += .1
        player['damage'] += 5
        print(loot_msgs['wrbands'])
    if enemy['name'] == 'Necromancer' and 'soulring' not in player_inventory and \
            player['class'] != 'Priest' and ic('soulring'):
        sr_cons = input("You've found Soulring. Do you want to take it? (Demonic item)")
        if sr_cons in ['yes', 'y']:
            if 'stonemask' in player_inventory:
                player_inventory.remove('stonemask')
            player_inventory.append('soulring')
            player['lifesteal'] = True
            player['max_health'] += 25
            player['ls_coefficient'] -= 1
            print(loot_msgs['soulring'])
    if enemy['name'] == 'Necromancer' and player['class'] == 'Priest':
        player['health'] = player['max_health']
        print(loot_msgs['necro_priest'])
    if enemy['name'] == 'Alchemist' and 'herbkit' not in player_inventory and \
            player['class'] != 'Demonknight' and ic('herbkit'):
        player_inventory.append('herbkit')
        player['potion_effect'] += 10
        player['healing_potions'] += 1
        print(loot_msgs['alch_loot'])
    if enemy['name'] == 'Alchemist' and player['class'] == 'Demonknight':
        player['health'] = player['max_health']
        print(loot_msgs['alch_demon'])
    if gloves_drop_chance > 8 and enemy['name'] == 'Assassin' and 'gloves' not in player_inventory and ic('gloves'):
        player_inventory.append('gloves')
        player['crit_chance'] += 5
        print(loot_msgs['gloves'])
    if banisher_drop_chance == 1 and enemy['name'] == 'Crusader' and ic('banisher'):
        player_inventory.append('banisher')
        print(loot_msgs['banisher'])

    if merchant_chance == 1:
        merchant_event()

    print(Style.RESET_ALL)
    input(f"Okay, let's go...")


def drop_item(item):  # TODO: проработать чтобы не уходило в отрицалово!!!
    if item == "flask":
        player['allow_potions'] = False
        player['healing_potions'] = 0
    if item == "sword":
        player['damage'] -= 15
    if item == "armorpants":
        player['armor'] -= 0.2
    if item == "stonemask":
        player['lifesteal'] = False
    if item == "demonblade":
        player['damage'] -= 25
    if item == "firebook":
        player['fireball_dmg'] -= 25
    if item == "shield":
        player['block_chance'] -= 8
    if item == "wristbands":
        player['damage'] -= 5
        player['armor'] -= 0.1
    if item == "soulring":
        player['max_health'] -= 25
        player['ls_coefficient'] += 1
        player['lifesteal'] = False
    if item == "herbkit":
        player['potion_effect'] -= 10
    if item == "gloves":
        player['crit_chance'] -= 5
    if item == "speedboots":
        player['escape_chance'] -= 10
    if item == "coolhat":
        player['persuade_chance'] -= 10
    if item == "luckycoin":
        player['gold_bonus'] -= 5
    if item == "rosary":
        player['banish_heal'] -= 10
    if item == "redpepper":
        player['stew_bonus'] -= 10

    if player['armor'] < 1:
        player['armor'] = 1
    if player['health'] > player['max_health']:
        player['health'] = player['max_health']
    if player['max_health'] < 1:
        player['max_health'] = 1
    if player['damage'] < 1:
        player['damage'] = 1
    if player['block_chance'] < 0:
        player['block_chance'] = 0

    player_inventory.remove(item)
    print(Fore.GREEN + f"You dropped {item} and it's vanished..." + Style.RESET_ALL)


def ic(new_item):
    if len(player_inventory) >= player['inv_size']:
        print(Style.RESET_ALL, end="")
        question = input(f"Here {new_item.capitalize()}, but your inventory is full. "
                         f"Would you like to throw away something unnecessary?: ")
        if question in ['y', 'yes']:
            drop = None
            show_inventory(player, player_inventory, player['inv_size'], equipment_desc)
            while drop not in player_inventory:
                drop = input("Choose item to drop: ")
            drop_item(drop)
            return True
        else:
            return False
    else:
        return True


# 'end of battle' defs

def persuading(hero, opponent, container):
    pe_chance = (randint(1, 100) - opponent['persuade_bonus'])
    if pe_chance < hero['persuade_chance'] and any(opponent['name'] not in ls for ls in [undead_list, boss_list]) and \
            player['class'] != 'Demonknight' or pe_chance < hero['persuade_chance'] and \
            opponent['name'] not in boss_list and player['class'] == 'Demonknight':
        print(Fore.GREEN + f"\nYou've managed to persuade the enemy...\n" + Style.RESET_ALL)
        hero['score'] += 1
        input(f"Press any key to continue...")
        gold(hero, opponent)
        loot()
        next_enc(hero, opponent, container)
    else:
        print(Fore.RED + f"\nYour persuading skills fails you..." + Style.RESET_ALL)
        attack(opponent, hero)


def bribing(hero, opponent, container):
    if hero['gold'] >= opponent['bribe_value'] and any(opponent['name'] not in ls for ls in [undead_list, boss_list]):
        hero['gold'] -= opponent['bribe_value']
        print(Fore.GREEN + f"\nYou've managed to bribe the enemy...\n" + Style.RESET_ALL)
        hero['score'] += 1
        input(f"Press any key to continue...")
        loot()
        next_enc(hero, opponent, container)
    else:
        print(Fore.RED + f"\nYour don't have enough gold for a bribe..." + Style.RESET_ALL)


def escaping(hero, opponent, container):  # isolated
    esc_chance = (randint(1, 100) - opponent['escape_bonus'])
    if esc_chance < hero['escape_chance']:
        print(Fore.GREEN + f"\nYou've managed to escape from enemy...\n" + Style.RESET_ALL)
        input(f"Press any key to continue...")
        next_enc(hero, opponent, container)
    else:
        print(Fore.RED + f"\nYour escape chances fails you..." + Style.RESET_ALL)
        attack(opponent, hero)


def hero_travels_further(hero):  # isolated
    print(f"\n{hero['name']} travels further...")
    input("Press any key to continue...\n")
    if hero['score'] % 10 == 0 and hero['score'] != 0:
        print(Back.WHITE + Fore.BLACK + "New BOSS appears!\n" + Style.RESET_ALL)
    else:
        print(Back.WHITE + Fore.BLACK + "New enemy appears!\n" + Style.RESET_ALL)


def enemy_slayed(hero, opponent, container):  # isolated
    hero['score'] += 1
    print(f"\n{opponent['name']} is dead!")
    exp_points(hero)
    input(f"Press any key to continue...")
    gold(hero, opponent)
    loot()
    next_enc(hero, opponent, container)


def hero_slayed(hero):  # isolated
    print(f"\n{hero['name']} is dead!")
    print(f"Enemies slayed: {hero['score']}")


def next_enc(hero, opponent, container):
    hero_travels_further(hero)
    reroll_enemy(opponent)
    enemy_correction(opponent, hero, container)
    appendnames(hero, opponent)
    status(player, enemy, undead_list, boss_list)


# start

print(f"\nWelcome, {player['name']}! Your journey begins...\n")
character_creator()
controls(player_attributes, player_inventory)
print(Back.WHITE + Fore.BLACK + f"\nFirst enemy appears on your way...\n" + Style.RESET_ALL)
enemy_correction(enemy, player, player_inventory)
status(player, enemy, undead_list, boss_list)

# game cycle

while True:
    try:
        action = input(f"\nNext move: ")
        action = action.lower().strip()
        if action in syntax_dict['status_list']:
            status(player, enemy, undead_list, boss_list)
        elif action in syntax_dict['help_list']:
            controls(player_attributes, player_inventory)
        elif action in syntax_dict['escape_list']:
            escaping(player, enemy, player_inventory)
            if player['health'] < 1:
                hero_slayed(player)
                break
        elif action in syntax_dict['persuade_list']:
            persuading(player, enemy, player_inventory)
            if player['health'] < 1:
                hero_slayed(player)
                break
        elif action in syntax_dict['bribe_list']:
            bribing(player, enemy, player_inventory)
        elif action in syntax_dict['quit_list']:
            break

        # split() for multi-word commands
        else:
            action = action.split(' ')
            if action[1] in syntax_dict['attack_list'] and action[0] in syntax_dict['player_list']:

                attack(player, enemy)
                if enemy['health'] < 1:
                    enemy_slayed(player, enemy, player_inventory)
                    continue

                attack(enemy, player)
                if player['health'] < 1:
                    hero_slayed(player)
                    break

            elif action[0] in syntax_dict['fireball_list'] and action[1] in syntax_dict['attack_list']:
                fireball_attack(player, enemy)
                if enemy['health'] < 1:
                    enemy_slayed(player, enemy, player_inventory)
                    continue

                attack(enemy, player)
                if player['health'] < 1:
                    hero_slayed(player)
                    break

            elif action[0] in syntax_dict['acidbomb_list'] and action[1] in syntax_dict['attack_list']:
                acidbomb()
                if enemy['health'] < 1:
                    enemy_slayed(player, enemy, player_inventory)
                    continue

                attack(enemy, player)
                if player['health'] < 1:
                    hero_slayed(player)
                    break

            elif action[0] in syntax_dict['slimebomb_list'] and action[1] in syntax_dict['attack_list']:
                slimebomb()
                if enemy['health'] < 1:
                    enemy_slayed(player, enemy, player_inventory)
                    continue

                attack(enemy, player)
                if player['health'] < 1:
                    hero_slayed(player)
                    break

            elif action[0] in syntax_dict['smokebomb_list'] and action[1] in syntax_dict['attack_list']:
                smokebomb()
                if enemy['health'] < 1:
                    enemy_slayed(player, enemy, player_inventory)
                    continue

            elif action[0] in syntax_dict['banisher_list'] and action[1] in syntax_dict['attack_list']:
                banisher(player, enemy, player_inventory, undead_list)
                if enemy['health'] < 1:
                    enemy_slayed(player, enemy, player_inventory)
                    continue

            elif action[0] in syntax_dict['soulorb_list'] and action[1] in syntax_dict['attack_list']:
                soulorb(player, player_inventory, enemy)
                if enemy['health'] < 1:
                    enemy_slayed(player, enemy, player_inventory)
                    continue

                attack(enemy, player)
                if player['health'] < 1:
                    hero_slayed(player)
                    break

            elif action[0] in syntax_dict['drink_list']:
                healing_potion()
            elif action[1] in syntax_dict['inventory_list'] and action[0] in syntax_dict['inspect_list']:
                show_inventory(player, player_inventory, player['inv_size'], equipment_desc)
                status(player, enemy, undead_list, boss_list)
            elif action[1] in syntax_dict['attribute_list'] and action[0] in syntax_dict['inspect_list']:
                show_attributes(player, player_attributes, attr_desc)
                status(player, enemy, undead_list, boss_list)
            elif action[1] in syntax_dict['player_list'] and action[0] in syntax_dict['inspect_list']:
                show_player_info(player)
                status(player, enemy, undead_list, boss_list)
            elif action[1] == 'up' and action[0] in player_attributes.keys() or \
                    action[1] == 'up' and action[0] in lowcase_player_attr.keys():
                attribute_up(player, player_attributes, action[0].upper(), attr_desc)
                status(player, enemy, undead_list, boss_list)
            elif action[1] in player_inventory and action[0] in syntax_dict['drop_list']:
                drop_item(action[1])
                show_inventory(player, player_inventory, player['inv_size'], equipment_desc)
                status(player, enemy, undead_list, boss_list)
            elif action[1] in syntax_dict['enemy_list'] and action[0] in syntax_dict['inspect_list']:
                if enemy['mod'] != '':
                    inspect_enemy(
                        enemy['name'], enemies_desc[enemy['name']], enemy['mod'], modification_desc[enemy['mod']])
                else:
                    inspect_enemy(enemy['name'], enemies_desc[enemy['name']])
            elif action[0] == 'rename':
                rename(player, action[1])
                appendnames(player, enemy)
                status(player, enemy, undead_list, boss_list)

    except IndexError:
        print(Fore.RED)
        print(er_msg_main + Style.RESET_ALL)

# quit or gameover

print("\nBye!", end='')
input()
