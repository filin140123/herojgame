def warrior_class(hero, container):
    print(f"You choose Warrior...\n")
    hero['class'] = 'Warrior'
    container.extend(['sword', 'armorpants'])
    hero['healing_potions'] += 1
    hero['armor'] += .2


def mage_class(hero, container):
    print(f"You choose Mage...\n")
    hero['class'] = 'Mage'
    container.extend(['firebook', 'slimebomb'])
    hero['healing_potions'] += 2
    hero['fireballs'] += 2
    hero['exp_points'] += 2


def thief_class(hero, container):
    print(f"You choose Thief...\n")
    hero['class'] = 'Thief'
    container.extend(['gloves', 'speedboots', 'smokebomb'])
    hero['healing_potions'] += 1
    hero['crit_chance'] += 10
    hero['crit_mul'] += .5
    hero['gold'] += 50


def demonknight_class(hero, container):
    print(f"You choose Demonknight...\n")
    hero['class'] = 'Demonknight'
    container.extend(['demonblade', 'stonemask', 'soulorb'])
    container.remove('flask')
    hero['allow_potions'] = False
    hero['block_chance'] += 10
    hero['ls_coefficient'] = 4


def bard_class(hero, container):
    print(f"You choose Bard...\n")
    hero['class'] = 'Bard'
    container.extend(['luckycoin'])
    hero['healing_potions'] += 4
    hero['persuade_chance'] += 20
    hero['escape_chance'] += 5
    hero['gold'] += 100
    hero['discount'] += 10


def priest_class(hero, container):
    print(f"You choose Priest...\n")
    hero['class'] = 'Priest'
    container.extend(['banisher', 'banisher', 'banisher', 'banisher', 'banisher'])
    hero['healing_potions'] += 2
    hero['max_health'] = 150
    hero['health'] = 150
    hero['banish_heal'] += 20
    hero['block_chance'] += 5


if __name__ == '__main__':
    warrior_class(hero, container)
    mage_class(hero, container)
    thief_class(hero, container)
    demonknight_class(hero, container)
    bard_class(hero, container)
    priest_class(hero, container)
