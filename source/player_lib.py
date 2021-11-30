# player character initialization, checks and progression
from colorama import Fore, Back, Style
from inspect_lib import show_attributes


def inventory_check(hero, container):
    if 'sword' in container:
        hero['damage'] += 15
    if 'demonblade' in container:
        hero['damage'] += 25
    if 'armorpants' in container:
        hero['armor'] += .2
    if 'stonemask' in container:
        hero['lifesteal'] = True
    if 'firebook' in container:
        hero['fireball_dmg'] += 25
        hero['fireballs'] += 1
    if 'shield' in container:
        hero['block_chance'] += 10
    if 'wristbands' in container:
        hero['armor'] += .1
        hero['damage'] += 5
    if 'soulring' in container:
        hero['lifesteal'] = True
        hero['max_health'] += 25
        hero['ls_coefficient'] -= 1
    if 'herbkit' in container:
        hero['potion_effect'] += 10
        hero['healing_potions'] += 2
    if 'gloves' in container:
        hero['crit_chance'] += 5
    if 'speedboots' in container:
        hero['escape_chance'] += 10
    if 'coolhat' in container:
        hero['persuade_chance'] += 10
    if 'luckycoin' in container:
        hero['gold_bonus'] += 5
    if 'rosary' in container:
        hero['banish_heal'] += 10
    if 'redpepper' in container:
        hero['stew_bonus'] += 10


def rename(hero, new_name):
    hero['name'] = new_name.capitalize()
    print(Back.WHITE + Fore.BLACK + f"\nNow your name is {hero['name']}...\n" + Style.RESET_ALL)


def attribute_up(hero, hero_atts, attr, a_desc):
    if hero['exp_points'] > 0:
        hero_atts[attr] += 1
        hero['exp_points'] -= 1
        print(Back.CYAN + Fore.BLACK + f"\n{attr} is raised to {hero_atts[attr]}!" + Style.RESET_ALL)
        attribute_up_effect(hero, attr)
        show_attributes(hero, hero_atts, a_desc)
    else:
        print(Fore.RED + f"\nYou don't have experience points!\n" + Style.RESET_ALL)


def attribute_up_effect(hero, attr):
    if attr == 'STR':
        hero['damage'] += 2
        hero['crit_mul'] += .04
        hero['crit_training_bonus'] += .01
    if attr == 'PER':
        hero['escape_chance'] += 2
        hero['gold_bonus'] += 1
    if attr == 'END':
        hero['max_health'] += 2
        hero['stew_bonus'] += 2
        hero['training_bonus'] += 1
    if attr == 'CHR':
        hero['discount'] += 2
        hero['persuade_chance'] += 2
    if attr == 'INT':
        hero['fireball_dmg'] += 3
        hero['bomb_dmg'] += 5
        hero['ls_coefficient'] -= .2
        if hero['ls_coefficient'] < 1.0:
            hero['ls_coefficient'] = 1.0
        hero['banish_heal'] += 3
    if attr == 'RCT':
        hero['crit_chance'] += 1
        hero['block_chance'] += 1
    if attr == 'SRV':
        hero['potion_effect'] += 2
        hero['repair_armor_bonus'] += .01


def exp_points(hero):
    if hero['score'] % 5 == 0:
        hero['exp_points'] += 1
        print(Fore.CYAN + f"\nYou gained exp point! ({hero['exp_points']} now)\n" + Style.RESET_ALL)


if __name__ == '__main__':
    inventory_check(hero, container)
    rename(hero, new_name)
    attribute_up(hero, hero_atts, attr, a_desc)
    attribute_up_effect(hero, attr)
    exp_points(hero)
