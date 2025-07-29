print("Welcome to Fantasy Quest")

sword_damage= 10
player_health= 100
health_after_attack= player_health -sword_damage

print (f"Lollifred's health is {player_health}")
print (f"Lollifred's is hit by a sword for {sword_damage} damage...")
print(f"Lollifred's health is now {health_after_attack}")

print("Use the arrow keys to move")

player_health= 1000
print(player_health)

player_health= 1000 -900
print(player_health)

player_health= 900-100
print(player_health)

player_health= 800-100
print(player_health)

player_health= 1000
arrmor_mult= 2

armored_hlth= player_health*2

print(armored_hlth)


player_health= 100
poison_mgic= True
poison_attck=-10

poison_hlth = player_health+ poison_attck
print(poison_hlth)

print(f"player health is a/an {type(player_health)}")
print(f"poison magic is a/an {type(poison_mgic)}")

enemy= None
print(enemy is None)

