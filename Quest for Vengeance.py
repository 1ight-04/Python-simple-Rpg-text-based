
# Game : Quest for Vengeance

import time
import random
from tqdm import tqdm

for i in tqdm(range(10), desc="Loading", colour="green", bar_format="{l_bar}{bar}|{n_fmt}/{total_fmt}"):
    time.sleep(0.1)  # adds the delay
print("Done!")

max_level = 30


def game_setup():
    while input("Quest for Vengeance \nPress x to continue\n>: ") != 'x':
    name = input("Enter a Username of choice: ")
    print(f"Name: {name} \tClass: Magic Swordsman")
    for i in tqdm(range(10), desc="Loading", colour="green", bar_format="{l_bar}{bar}|{n_fmt}/{total_fmt}"):
        time.sleep(0.1)  # Simulate some work
    print("Done!")
    return name


name = game_setup()

player = {
    'name': name,
    'class': 'Swordsman',
    'level': 1,
    'exp': 0,
    'hp': 69,
    'max_hp': 69,
    'power': 10,
    'weapon': 'Katana',
    'zone': 'Verdanthia',
    'boss_defeated': False,
    'monsters_defeated': 0,
    'skills': [],
    'weapons': ['Katana'],
    'admin_mode': False
}

zones = {
    # A dictionary to place the zones within are the required level to travel to the zones also the level required to fight the final boss
    'Verdanthia': {
        'level_req': 1,
        'boss_level': 5,
        'multiplier': 1.5,  # the multi of the zone
        'welcome': """System: you have arrived to the first world """,
        'boss_killed': """Notice: You have defeated the boss of Verdanthia!\nYou: he’s more powerful than the other monsters. But still weak.System:You will now be sent to zone 2""",
        'boss': {'name': 'Grand Tree', 'hp': 250, 'power': 50, 'exp': 50}
    },
    'Tundria': {
        'level_req': 5,
        'boss_level': 8,
        'multiplier': 2.5,
        'welcome': """System: You have arrived to the second world.
""",
        'boss_killed': "Notice: You have defeated the boss of Cerberus! You will now be sent to zone 4",
        'boss': {'name': 'Iblis', 'hp': 450, 'power': 100, 'exp': 150}
    },
    'Zephyria': {
        'level_req': 11,
        'boss_level': 15,
        'multiplier': 9,
        'welcome': """System: You have arrived to the third world.
""",
        'boss_killed': "Notice: You have defeated the boss of Zephyria! You will now be sent to the final zone!",
        'boss': {'name': 'Angel of Judgement', 'hp': 550, 'power': 150, 'exp': 200}
    },
    'Aetheria': {
        'level_req': 15,
        'boss_level': 20,
        'multiplier': 15,
        'welcome': f"""System: You have arrived to the fourth world.

""",
        'boss_killed': "Notice: You have defeated the boss of Aetheria.\nI have finally avenged you, Sensei... [Game completed! You Have cleared the Labyrinth. The Labyrinth will now collapse]",
        'boss': {'name': 'Phantom', 'hp': 650, 'power': 200, 'exp': 250}
    }
}

enemies = [  # the dictionary stores the list of enemies that the player has chance to fight
    {'name': 'Goblin', 'hp': 50, 'power': 15, 'exp': 10, 'chance': 0.4},
    {'name': 'Orc', 'hp': 70, 'power': 20, 'exp': 15, 'chance': 0.3},
    {'name': 'Troll', 'hp': 90, 'power': 25, 'exp': 20, 'chance': 0.2},
    {'name': 'Demon', 'hp': 100, 'power': 30, 'exp': 30, 'chance': 0.05},
    {'name': 'Dark Elf', 'hp': 150, 'power': 40, 'exp': 40, 'chance': 0.05}
]

skills = [  # the dictionary stores the list of skills that the player can unlock
    {'name': 'Slash of Death', 'level': 1, 'damage': 15},
    {'name': 'Venom', 'level': 6, 'damage': 30},
    {'name': 'Zero Gravity', 'level': 12, 'damage': 50},
    {'name': 'Guardian Shield', 'level': 18, 'damage': 70},
    {'name': 'The slash of Tiamat', 'level': 22, 'damage': 100},
    {'name': 'Celestial Navigation', 'level': 25, 'damage': 300},
    {'name': 'Supernova', 'level': 30, 'damage': 600}

]

weapons = [  # the dictionary stores the list of weapons that the player can unlock
    {'name': 'Celestial Sword', 'power': 15, 'chance': 40},
    {'name': 'Celestial Bow', 'power': 20, 'chance': 30},
    {'name': 'Celestial Sythe', 'power': 25, 'chance': 20},
    {'name': 'Celestial Platinum Blade', 'power': 30, 'chance': 10}
]


def main_menu():  # this print the main menu where the player can choose what to do
    """Prints the main menu options"""
    print("\nMain Menu:")
    print(">> 1. Explore")
    print(">> 2. Train")
    print(">> 3. Travel")
    print(">> 4. Stat")
    print(">> 5. Go Admin" if not player['admin_mode'] else ">> 5. Exit Admin")


def main():  # the funtion performs the where when the player selects a choice from the main menu
    print(f"Welcome, {player['name']}, to Quest for Vengeance!")
    print(zones[player['zone']]['welcome'])
    while True:
        main_menu()
        choice = input("Choose an action:\n ").strip().lower()
        if choice in ['1', 'explore']:
            explore()
        elif choice in ['2', 'train']:
            train()
        elif choice in ['3', 'travel']:
            travel()
        elif choice in ['4', 'stat']:
            stat()
        elif choice == '5':
            if player['admin_mode']:  # choice to go admin mode
                exit_admin_mode()
            else:
                enter_admin_mode()
        else:
            print("Invalid choice! Try again.")


def explore():  # this funtion handels the explore funtion from the main menu in which the player can travel and fight funtoin tofight enemies.
    for i in tqdm(range(10), desc="Exploring", colour="green", bar_format="{l_bar}{bar}|{n_fmt}/{total_fmt}"):
        time.sleep(0.1)  # Simulate some work
    print("Done!")
    print(f"\nExploring {player['zone']}")
    if player['monsters_defeated'] < 4:
        enemy = random_enemy()
        if battle(enemy):
            player['monsters_defeated'] += 1
            player['power'] += 2
            print("Continue quest to avenge your teacher.")
            print(f"\n>> +2 Power\n")
        else:
            print("Rest before exploring again.")
    else:
        print(f"Prepare to face the final boss of {player['zone']}!")
        boss = zones[player['zone']]['boss']
        if battle(boss):
            player['boss_defeated'] = True
            print(zones[player['zone']]['boss_killed'])
        else:
            print("You were defeated by the boss. Train and try again.")
    input("Press Enter...")


def random_enemy():  # this funtion randimizes the enemies from the enemy list above
    base_enemy = random.choices(enemies, weights=[e['chance'] for e in enemies])[0]
    multiplier = zones[player['zone']]['multiplier']
    enemy = {
        'name': base_enemy['name'],
        'hp': base_enemy['hp'] * multiplier,
        'power': base_enemy['power'] * multiplier,
        'exp': base_enemy['exp'] * multiplier,
        'chance': base_enemy['chance']
    }
    return enemy


def battle(
        enemy):  # the funtion the main battle funtion that handles the fighting system in which the players damages and the enemies damages and hp
    print(f"\n{enemy['name']} appeared!")
    while enemy['hp'] > 0 and player['hp'] > 0:
        print(f"\n>> {player['name']} HP: {player['hp']} / {player['max_hp']}")
        print(f">> {enemy['name']} HP: {enemy['hp']}")

        # Player's turn
        print("\nAttaaaaaaack:")
        print("1. Attack")
        print("2. Use Skill")
        choice = input("Choose your move\n>>:")

        if choice == '1':
            player_damage = player_attack(enemy)
        elif choice == '2':
            player_damage = use_skill(enemy)
        else:
            print("You took too long...")
            player_damage = 0

        enemy['hp'] -= player_damage
        print(f">> Your Damage: {player_damage}")
        if enemy['hp'] <= 0:
            print(f"{enemy['name']} defeated!!")
            player['exp'] += enemy['exp']
            check_level()
            find_loot()
            return True
        else:
            print(f"Good move but not enough!")
            enemy_damage = enemy_attack(enemy)
            player['hp'] -= enemy_damage
            print(f">> Enemy Damage: {enemy_damage}")
            if player['hp'] <= 0:
                print("You got destroyed! Train and try again.")
                return False
    return True


def player_attack(enemy):  # this funtion handles the power of the player
    return random.randint(1, 1) * player['power']  # damage the player deals


def enemy_attack(enemy):  # this funtion handels the power of the enemies
    return random.randint(1, 1) * enemy['power']  # damage the enemy deals


def use_skill(enemy):  # this funtion handles he use of the skill
    print("Skill:\n")
    for i, skill in enumerate(skills, 1):
        if player['level'] >= skill['level']:
            print(f">> {i}. {skill['name']}")
        else:
            print(f">> {i}. {skill['name']} (🔒)")
    choice = input("Choose your skill: \n>>: ")
    for i, skill in enumerate(skills, 1):
        if player['level'] >= skill['level']:
            if str(i) == choice:
                return skill['damage'] + player['power']  # Return the damage scaled with player's power
    print("Skill not found")
    return 0


def train():  # this funtion the traning mechanism in which the player can choose to train from the main menu and when he trains he gains +20 exp to level up and has chance of getting a skill.
    if player['level'] == max_level:
        print("You have reached the max level")
        print("\n>> Power : +20 ")
        player['power'] += 20  # increase player's power by ten
    else:
        for i in tqdm(range(10), desc="Training", colour="green", bar_format="{l_bar}{bar}|{n_fmt}/{total_fmt}"):
            time.sleep(0.2)  # Simulate some work
        print("Done!")
        player['exp'] += 15
        player['power'] += 0.7
        check_level()
        found_skill = random.random() < 0.4  # 40% chance to find a skill
        rewards = []
        if found_skill:
            available_skills = [skill for skill in skills if skill['name'] not in player['skills']]
            if available_skills:
                weights = [skill['damage'] for skill in available_skills]
                new_skill = random.choices(available_skills, weights=weights, k=1)[0]
                player['skills'].append(new_skill['name'])
                rewards.append(f"Skill: {new_skill['name']}")
                print(f"\nYou learned a new skill: {new_skill['name']}!")
        print("\nTraining successfully completed.")
        print(f"\n>> +10 EXP\n")
        print(f"\n>> +0.7 Power\n")
        if rewards:
            print("Rewards>:")
            for reward in rewards:
                print(reward)
        else:
            print("You had a very tiring training.")
        input("Press Enter...")


def find_loot():  # this funtion handles the loot finding system in which the player can train or explore after those two he gain a certain weapn and increases the players power
    found_weapon = random.random() < 0.4  # 40% chance to find a weapon
    if found_weapon:
        available_weapons = [weapon for weapon in weapons if weapon['name'] not in player['weapons']]
        if available_weapons:
            weights = [weapon['chance'] for weapon in available_weapons]
            new_weapon = random.choices(available_weapons, weights=weights, k=1)[0]
            print(f"\n>> Found Weapon: {new_weapon['name']}")
            print(f"\n>> Power: +{new_weapon['power']}")

            if new_weapon['power'] > player['power']:
                print(f"You equip {new_weapon['name']}.")

                if player['weapon'] in player['weapons']:
                    player['weapons'].remove(player['weapon'])
                player['weapon'] = new_weapon['name']
                player['power'] += new_weapon['power']
            else:
                print(f"The weapon you just found is not as powerful as {player['weapon']}")
                player['weapons'].append(new_weapon['name'])
                player['power'] += new_weapon['power']


def check_level():  # this function handels the leveling system inw hich the player has to gain exp to level up so this checks if th eplayer has enough exp if yes then levels up and after leveling up the players power and hp increases
    while player['exp'] >= player['level'] * 20:
        if player['level'] >= max_level:
            print(f"{player['name']} you have reached {player['level']} (🏁)")
            player['exp'] = player['level'] * 20
            break
        else:
            player['exp'] -= player['level'] * 20
            player['level'] += 1
            player['max_hp'] += 10
            player['hp'] = player['max_hp']
            player['power'] += 7

            for skill_name in player['skills']:
                for skill in skills:
                    if skill['name'] == skill_name and player['level'] >= skill['level']:
                        print(f"{player['name']}! You have leveled up to {player['level']} 👏!")
                        print(f"You can now use the skill: {skill_name}!")
                        break
            else:
                print(f"{player['name']}! You have leveled up to {player['level']} 👏!")


def travel():  # this funtion handels the traveling system in ehich the pplayer has complete the required thing s which are the level and defeating certain monsters.
    for i in tqdm(range(25), desc="To celestial portal", colour="green", bar_format="{l_bar}{bar}|{n_fmt}/{total_fmt}"):
        time.sleep(0.1)  # Simulate some work
    if not player['boss_defeated'] and not player['admin_mode']:
        print(f"Defeat the boss of {player['zone']} to unlock the next zone")
        return

    available_zones = [name for name, info in zones.items() if player['level'] >= info['level_req']]
    for i, zone in enumerate(available_zones, 1):
        print(f"-->>{i}. {zone} (Level {zones[zone]['level_req']} required)")

    choice = int(input("Choose a zone to travel to\n>: ")) - 1
    if 0 <= choice < len(available_zones):
        player['zone'] = available_zones[choice]
        player['monsters_defeated'] = 0
        player['boss_defeated'] = False
        print(zones[player['zone']]['welcome'])

    input("Press Enter...")


def stat():  # this funtion print the players current stat when the pplayer chooses the stat from the main menu.
    for i in tqdm(range(20), desc="Checking Stats ", colour="green", bar_format="{l_bar}{bar}|{n_fmt}/{total_fmt}"):
        time.sleep(0.1)  # Simulate some work
    print("Done!")
    stats = [
        f"\t>: Name: {player['name']}",
        f"\t>: Class: {player['class']}",
        f"\t>: Level: {player['level']}",
        f"\t>: Exp: {player['exp']}",
        f"\t>: HP: {'♾️' if player['admin_mode'] else player['hp']}",
        f"\t>: Power: {player['power']}",
        f"\t>: Weapon: {player['weapon']}",
        f"\t>: Zone: {player['zone']}"
    ]
    print("\n".join(stats))

    input("Press Enter...")


def enter_admin_mode():
    # This function handles entering admin mode, granting the player god-like powers
    for i in tqdm(range(10), desc="Entering God mode", colour="green", bar_format="{l_bar}{bar}|{n_fmt}/{total_fmt}"):
        time.sleep(0.1)
    player['admin_mode'] = True
    player['level'] = max_level
    player['exp'] = max_level * 30
    player['hp'] = float('inf')
    player['max_hp'] = float('inf')
    player['power'] = 6966969
    player['skills'] = [skill['name'] for skill in skills]
    player['weapons'] = [weapon['name'] for weapon in weapons]
    player['zone'] = 'Verdanthia'
    for zone in zones:
        zones[zone]['level_req'] = 0
    print("You have entered Admin Mode! Enjoy your god-like powers.")


def exit_admin_mode():  # this funtion handles the exit form the admin mode which brings the player back to the normal mode where has not infinite stat.
    for i in tqdm(range(10), desc="Leaving God mode", colour="green", bar_format="{l_bar}{bar}|{n_fmt}/{total_fmt}"):
        time.sleep(0.1)  # Simulate some work
    print("Done!")
    player['admin_mode'] = False
    player['level'] = 1
    player['exp'] = 0
    player['hp'] = 69
    player['max_hp'] = 69
    player['power'] = 10
    player['skills'] = []
    player['weapons'] = ['Katana']
    player['zone'] = 'Verdanthia'
    for zone, info in zones.items():
        info['level_req'] = {
            'Verdanthia': 1,
            'Tundria': 5,
            'Cerberus': 8,
            'Zephyria': 11,
            'Aetheria': 15
        }[zone]
    print("You have exited Admin Mode. Back to normal gameplay.")


if __name__ == "__main__":  # This ensures the game starts when the script is run directly

    main()