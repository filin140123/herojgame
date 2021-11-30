# control scheme

syntax_dict = {
    'quit_list': ['quit', 'q', 'exit'],
    'attack_list': ['attacks', 'attack', 'a'],
    'status_list': ['status', 's', 'stat', 'statistics'],
    'help_list': ['help', '?', '???', 'manual', 'h', 'controls', 'ctrls', 'c', 'tutorial', 'tut'],
    'inspect_list': ['inspect', 'ins', 'i', 'show'],
    'enemy_list': ['enemy', 'e', 'en', 'oppo', 'villain'],
    'player_list': ['melee', 'player', 'j', 'me', 'p'],
    'drink_list': ['drink', 'd'],
    'fireball_list': ['fireball', 'fire', 'fb', 'f'],
    'acidbomb_list': ['acid', 'acidbomb', 'ac', 'acb'],
    'slimebomb_list': ['slime', 'slimebomb', 'sl', 'slb'],
    'smokebomb_list': ['smoke', 'smokebomb', 'sm', 'smb'],
    'soulorb_list': ['soulorb', 'sorb', 'soulo', 'so'],
    'attribute_list': ['attribute', 'attr', 'at', 'skills'],
    'escape_list': ['escape', 'esc', 'run', 'runaway', 'r'],
    'persuade_list': ['pers', 'persuade', 'per', 'talk'],
    'bribe_list': ['bribe', 'br', 'bribing'],
    'banisher_list': ['banisher', 'b', 'ba', 'ban'],
    'inventory_list': ['inv', 'inventory', 'backpack', 'items'],
    'drop_list': ['drop'],
}

creator_list = ['', '1', '2', '3', '4', '5', '6'] + syntax_dict['quit_list'] + syntax_dict['inspect_list']


def appendnames(hero, opponent):
    syntax_dict['player_list'].append(
        hero['name'].lower()
    )
    syntax_dict['enemy_list'].extend(
        [opponent['name'].lower(), opponent['mod'].lower(), f"{opponent['mod'].lower()} {opponent['name'].lower()}"]
    )


if __name__ == '__main__':
    appendnames(hero, opponent)
