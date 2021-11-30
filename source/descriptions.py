# description dicts

attr_desc = {
    'STR': '+2 damage, +4% critical damage, +1 crit dmg from trainings',
    'PER': '+2% escape chance, +1g from loot',
    'END': '+2 max hp, +2 max hp from stews, +1 dmg from trainings',
    'CHR': '-2g to prices, +2% persuade chance',
    'INT': '+3 fireball dmg, +5 bombs dmg, +lifesteal effect, +3 hp from banishing',
    'RCT': '+1% crit chance, +1% block chance',
    'SRV': '+2 hp from potions, +0.01 from repairing armor',
}

lowcase_player_attr = {k.lower(): v for k, v in attr_desc.items()}

equipment_desc = {
    'flask': 'allows to drink healing potions',
    'sword': '+15 dmg',
    'armorpants': '+0.2 armor',
    'stonemask': 'healing at least 1/8 of dmg, considering the armor',
    'demonblade': '+25 dmg',
    'firebook': '+25 fireball dmg and 1 fireball scroll',
    'shield': '+8% block chance',
    'wristbands': '+0.1 armor and +5 dmg',
    'soulring': 'healing with attacks, and +25 max health',
    'herbkit': '+10 healing from potions',
    'gloves': 'crit chance +5%',
    'acidbomb': 'destroys armor of enemy, one-time use',
    'slimebomb': 'decreases damage of enemy, one-time use',
    'smokebomb': '+50% escape chance',
    'soulorb': 'steals some health from the enemy',
    'speedboots': '+10% escape chance',
    'coolhat': '+10% persuade chance',
    'banisher': 'kills any undead enemy instantly, one-time use',
    'luckycoin': '+5 gold from loot',
    'rosary': '+10 hp from banishing',
    'redpepper': '+10 max health from stews',
}

enemies_desc = {
    'Zombie': 'Weak, but no health potions in reward!',
    'Warlock': 'Can drop fireball scroll',
    'Orc': 'More health and block chance than another enemies',
    'Troll': 'Much more health, armor and block chance than other enemies',
    'Revenant': 'More dmg, more banish heal, can drop fireball scroll',
    'Ghost': 'No armor and block, but can debuff you',
    'Vampire': 'Cures himself with attacks, can drop Stonemask',
    'Marauder': 'More damage than other enemies, can drop Demonblade',
    'Assassin': 'More damage and crits than other enemies',
    'Bandit': 'Slightly more damage, armor and block chance, can drop Speedboots',
    'Horde of Zombies': 'Much... much more health!',
    'Necromancer': 'Boss. Cures himself with attacks, more crits, drops Soulring',
    'Warchief': 'Boss. More durable than other bosses, drops Wristbands',
    'Alchemist': 'Boss. Nothing great, nothing terrible. Drops Herbkit',
    'Crusader': 'Powerful, but friendly if you do not have demonic items. Can drop Banisher or Rosary',
    'Gnome': 'Easier to persuade, can frop Luckycoin',
}

modification_desc = {
    'Big ': 'More health',
    'Armored ': 'More armor',
    'Blood-lusting ': 'Cures himself with attacks',
    'Weak ': 'Less health, armor and damage',
    'Half-dead ': 'Only have 25 health points',
    'Terrible ': 'More damage and crits',
    'Wealthy ': 'Drops more gold',
    'Slow ': 'You can escape more easily',
    'Friendly ': 'Guaranteed persuasion',
}

loot_msgs = {
    'coolhat': "You found Troll's coolhat! +10% to persuading chance",
    'acidbomb': "You found one acidbomb. Use it to destroy enemy's armor completely",
    'slimebomb': "You found one slimebomb. Use it to decrease enemy's damage",
    'smokebomb': "You found one smokebomb. Use it to increase your escaping chance",
    'soulorb': "You found soulorb! Use it to steal some health from the enemy",
    'one_potion': "You found one healing potion!",
    'two_potion': "You found two healing potions!",
    'stew': "You found delicious stew! Your health was fully recovered...",
    'armor_up': "You found scraps and repaired your armor!",
    'armor_down': "You look at your armor and see that it's worn out... -4% armor",
    'exp_point': "You feel like you gain more experience. +1 exp point",
    'training_dmg': "You've trained your martial skills and gain",
    'training_block': "You've trained your blocking skill and gain 1% block chance!",
    'training_critmul': "You've trained your attack precision and gain 5% critical damage!",
    'fireball': "You found fireball scroll!",
    'firebook': "You found Magic Firebook! +25 fireball dmg and 1 fireball scroll for free",
    'stonemask': "You found the stonemask of vampirism! Now you heal 1/8 of your attacks (depends on INT)",
    'dblade_sw': "You found the demonblade! +25 dmg (instead of sword's +15)",
    'dblade_nosw': "You found the demonblade! +25 dmg",
    'shield': "You found shield! +8% block chance",
    'ghost_debuff': "You feel weakness in your body after that fight... -5 dmg and max health",
    'speedboots': "You found bandit's speedboots! +10% escape chance",
    'wrbands': "You found Warchief's wristbands! +10% armor and +5 dmg",
    'soulring': "You found Necromancer's soulring! Now you heal 1/7 of your attacks and gain +25 max health",
    'alch_loot': "You found Alchemist's herbkit! Your potions heals +10 more hp, and you get one potion",
    'alch_demon': "Alchemist's soul-power healed you completely...",
    'gloves': "You found black leather gloves! Your critical dmg chance has increased by 5%",
    'banisher': "You found Banisher! Use it to slay any undead enemy. One time use.",
    'necro_priest': "Banishing Necromancer to hell healed you completely...",
    'luckycoin': 'You found Luckycoin! +5 gold from loot',
    'rosary': 'You found Rosary! +10 hp from banishing',
    'sword': 'You found Sword! +15 dmg',
    'armorpants': 'You found Armorpants! +20% armor',
}

merch_msgs = {
    'potion': "You've bought the healing potion",
    'scroll': "You've bought the fireball scroll",
    'stew': "You've bought the stew — health fully restored, max health",
    'armorkit': "You've bought the armorkit",
    'whetstone': "You've bought the whetstone: +4 dmg",
    'powder': "You've bought the herbal powder: +4% critical chance",
    'acidbomb': "You've bought the acidbomb — use it to completely destroy enemy's armor",
    'slimebomb': "You've bought the slimebomb — use it to decrease enemy's damage",
    'smokebomb': "You've bought the smokebomb — gives +50% escape chance, one time use",
    'banisher': "You've bought the banisher — use in to kill undead enemy instantly. One time use",
    'redpepper': "You've bought the redpepper. +10 max hp from stews!",
    'backpack': "You've bought the backpack. +2 inventory size"
}

classes_desc = '''
Warrior — Have sword and armorpants. Have more armor (+20%) and one healing potion

Mage — Have firebook, slimebomb, 2 healing potions, 2 fireballs and +2 exp points at start

Thief — Have gloves and speedboots. Have more critical chance and critical damage...
also have one healing potion, smokebomb and 50 gold.

Demonknight — Have demonblade, stonemask and soulorb. Have +10% block chance...
and can't find healing potions, but have x2 vampirism healing.

Bard — Have 30% chance to persuade enemy. Merchants give 25% discount...
also have 4 healing potions and 100 gold. +5% escape chance.

Priest — Have 5 banishers and 150 health points. Can't have vampirism or demonblade...
banishing undeads healing Priest for 20 health. +5% block chance and 2 potions.
'''

er_msg_crea = "Type number of class, please. Or type 'q' to exit if you want"
er_msg_main = "Type proper command, please. Type 'h' for help or 'q' to exit"
