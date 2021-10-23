
#Task 1

#CharacterNames
wizard = "Wizard"
elf = "Elf"
human = "Human"
dragon = "Dragon"

#HealthPoints
wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300

#CharacterDamage
wizard_dmg = 150
elf_dmg = 100
human_dmg = 20
dragon_dmg = 50

#End Task #1



#Task 3

while True:
 #Task 2
 print("\n 1) Wizard \n 2) Elf\n 3) Human")

 character = input("Choose your character: ")
 
#End Task 2
 if character == "1":
  character = wizard
  my_hp = wizard_hp
  my_damage = wizard_dmg
  break
 elif character == "2":
  character = elf
  my_hp = elf_hp
  my_damage = elf_dmg
  break
 elif character == "3":
  character = human
  my_hp = human_hp
  my_damage = human_dmg
  break
 
 print("Unknown Character")

print("You have chosen the character: " + character)
print("Health: " + str(my_hp))
print("Damage: " + str(my_damage))
#End of Task 3

#Task 4
while True:
 dragon_hp = dragon_hp - my_damage
 my_hp = my_hp - dragon_dmg
 
 #Character Attacks
 print("\n The " + character + " damaged the Dragon!")
 print("The Dragon's hitpoints are now: " + str(dragon_hp))

 #Dragon Dies
 if(dragon_hp <= 0):
  print("\n The Dragon has lost the battle!")
  break
 #Dragon Wins
 elif(my_hp <= 0):
  print("\n The " + character + " has lost the battle!")

 #Dragon Attacks 
 print("The Dragon strikes back at the " + character)
 print("The " + character + "'s hitpoints are now: " + str(my_hp))

 #Character Dies 
 if(my_hp <= 0):
  print("\n The " + character + " has lost the battle!")
 #Character Wins
 elif(dragon_hp <= 0):
  print("\n The Dragon has lost the battle!")

#End of Task 4







