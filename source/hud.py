from colorama import Fore, Style


def status(hero, opponent, u_list, b_list):
    # health counter correction
    if hero['health'] < 0:
        hero['health'] = 0
    if opponent['health'] < 0:
        opponent['health'] = 0

    # persuade chance correction
    if any(opponent['name'] in i for i in [u_list, b_list]):
        pers_ch = 'no chance'
    elif (hero['persuade_chance'] + opponent['persuade_bonus']) >= 100:
        pers_ch = Fore.GREEN + 'guaranteed!' + Style.RESET_ALL
    else:
        pers_ch = f"{hero['persuade_chance'] + opponent['persuade_bonus']}%"

    # escape chance correction
    if (hero['escape_chance'] + opponent['escape_bonus']) >= 100:
        esc_ch = Fore.GREEN + 'guaranteed!' + Style.RESET_ALL
    else:
        esc_ch = f"{hero['escape_chance'] + opponent['escape_bonus']}%"

    # bribe variable correction
    if any(opponent['name'] in i for i in [u_list, b_list]):
        br_v = "can't bribe"
    elif hero['gold'] < opponent['bribe_value']:
        br_v = 'not enough gold'
    else:
        br_v = f"{opponent['bribe_value']} gold"

    # info
    print(
        f"- {hero['name']}, {hero['class']}:",
        f"{hero['health']}/{hero['max_health']}"
        if int(opponent['damage'] * (2 - hero['armor'])) <= hero['health']
        else Fore.RED + f"{hero['health']}/{hero['max_health']}" + Style.RESET_ALL,
        f"health, "
        f"{hero['damage']} dmg, "
        f"{round(hero['armor'], 2)} armor, "
        f"{hero['block_chance']}% block, "
        f"crits: {hero['crit_chance']}% of {int(hero['crit_mul'] * 100)}% dmg "
        + Fore.CYAN + "//" + Style.RESET_ALL,
        Fore.CYAN + f"You have {hero['exp_points']} unused exp!" + Style.RESET_ALL
        if hero['exp_points'] > 0
        else f"{5 - (hero['score'] % 5)} battles til exp point"
    )

    print(
        f"-- Inventory: [SHOW INV], Attributes: [SHOW AT]"
        + Fore.CYAN + " // " + Style.RESET_ALL +
        f"healing potions: {hero['healing_potions']}, "
        f"fireballs: {hero['fireballs']}, "
        f"gold: {hero['gold']}"
    )

    print(
        f"- {opponent['mod']}{opponent['name']}, level {opponent['level'] + 1}:",
        f"{opponent['health']}" if int(hero['damage'] * (2 - opponent['armor'])) <= opponent['health']
        else Fore.RED + f"{opponent['health']}" + Style.RESET_ALL,
        f"health, "
        f"{opponent['damage']} dmg, "
        f"{round(opponent['armor'], 2)} armor, "
        f"{opponent['block_chance']}% block chance"
    )

    print(f"- Escape chance: {esc_ch} / Persuade chance: {pers_ch} / Bribe value: {br_v}")
    

if __name__ == "__main__":
    status(hero, opponent, u_list, b_list)
