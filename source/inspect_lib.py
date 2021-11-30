# inspect and show defs
from colorama import Fore, Style
from random import choice


def inspect_enemy(target, desc, mod='', mod_desc=''):
    if mod != '':
        print(Fore.CYAN + f"\n{target}: {desc}" + f"\n{mod.strip()}: {mod_desc}" + Style.RESET_ALL)
    else:
        print(Fore.CYAN + f"\n{target}: {desc}" + Style.RESET_ALL)


def show_attributes(hero, hero_attr, descriptions):

    attr_title = f"{hero['name']}'s attributes"
    attr_title_len = len(attr_title)

    print(Fore.CYAN)
    print("╔" + "═" * (attr_title_len + 2) + "╗")
    print(f"║ {attr_title} ║")
    print("╚" + "═" * (attr_title_len + 2) + "╝")

    for i in hero_attr:
        print(f"{i}: {str(hero_attr[i])} --- {descriptions[i]}")
    print(Style.RESET_ALL)
    

def show_player_info(hero):
    print(Fore.CYAN)
    for i in hero:
        print(f"{i}: {str(hero[i])}")
    print(Style.RESET_ALL)


def show_inventory(hero, container, size, i_desc):

    inv_title = f"{hero['name']}'s inventory"
    inv_title_len = len(inv_title)

    print(Fore.GREEN)
    print("╔" + "═" * (inv_title_len + 2) + "╗")
    print(f"║ {inv_title} ║")
    print("╚" + "═" * (inv_title_len + 2) + "╝")
    for i in container:
        lns = (10 - len(i)) * " "
        print(f"[- {i.capitalize()}{lns} -] --- {i_desc[i]}")
    if len(container) < size:
        for i in range(size - len(container)):
            print("[-    ----    -]")
    print(Style.RESET_ALL)
    

def controls(atts, container):
    print(f"Available commands: ")
    print(f"-> melee attack")
    print(f"-> fireball attack")
    print(f"-> drink potion")
    if 'acidbomb' in container:
        print(f"-> acidbomb attack")
    if 'slimebomb' in container:
        print(f"-> slimebomb attack")
    if 'smokebomb' in container:
        print(f"-> smokebomb attack")
    if 'soulorb' in container:
        print(f"-> soulorb attack")
    if 'banisher' in container:
        print(f"-> banisher attack")
    print(f"-> show attributes")
    print(f"-> {choice(list(atts.keys()))} up (or another attribute)")
    print(f"-> inspect enemy")
    print(f"-> rename [name] - gives your character new name")
    print(f"...or type 'status', 'help' or 'quit'")


if __name__ == "__main__":
    inspect_item(item, desc)
    inspect_enemy(item, desc, mod='', mod_desc='')
    show_attributes(hero, hero_attr, descriptions)
    show_player_info(hero)
    show_inventory(hero, container, size, i_desc)
    controls(atts, container)
