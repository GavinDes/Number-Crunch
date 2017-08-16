#!/usr/bin/env python3

from random import randint
from colors import Blue, Red, Yellow, Green, Magenta

"""
Num Crunch is a CLI number guessing game which involves a randomly
generated number that one to four players must guess to earn a point.
The game ends when one (or more players) reach the score limit.
"""

print("""
 _   _                    ____                       _     
| \ | |_   _ _ __ ___    / ___|_ __ _   _ _ __   ___| |__  
|  \| | | | | '_ ` _ \  | |   | '__| | | | '_ \ / __| '_ \ 
| |\  | |_| | | | | | | | |___| |  | |_| | | | | (__| | | |
|_| \_|\__,_|_| |_| |_|  \____|_|   \__,_|_| |_|\___|_| |_|

""")
while True: # Variables will default to these among start or reset
   exit = 0
   turns = 0
   one_p = 0; two_p = 0; three_p = 0; four_p = 0; five_p = 0
   comps = ("Lauryn", "Faith", "Gavin", "Neil", "Carrie",
            "Chase", "Casey", "Rhiannon", "Daniel", "Ryan",
            "Lane", "Nolan", "Taylor", "Jessy", "Bob",
            "Josh", "Jon", "Lyri", "Robert","Debra", "Jason")
   while True:
      try:
         diff = int(input("[1] Easy [2] Medium [3] Hard\n"))
      except:
         print("Error!\n"); continue
      else:
         if diff == 1:
            x = 5
         elif diff == 2:
            x = 10
         elif diff == 3:
            x = 20
         else:
            continue
      break
   while True:
      try:
         players = int(input("\n[1] Two Players [2] Three Players [3] Four Players [4] Five Players\n"))
      except:
         print("Error!\n"); continue
      else:
         if players > 4 or players < 1: continue
      break
   while True:
      try:
         player_var = int(input("\n[1] Multiplayer [2] Single Player [3] Custom\n"))
      except:
         print("\nError!\n"); continue
      else:
         if player_var > 3 or player_var < 1:
            continue
      break
   if player_var == 1:
      p1_is = 1
      name1 = str(input("\nPlayer One Name:\n"))
      p2_is = 1
      name2 = str(input("\nPlayer Two Name:\n"))
      if players == 2 or 3 or 4:
         p3_is = 1
         name3 = str(input("\nPlayer Three Name:\n"))
      if players == 3 or 4:
         p4_is = 1
         name4 = str(input("\nPlayer Four Name:\n"))
      if players == 4:
         p5_is = 1
         name5 = str(input("\nPlayer Five Name:\n"))
   elif player_var == 2:
      p1_is = 1
      name1 = str(input("\nPlayer One Name:\n"))
      p2_is = 2
      name2 = comps[randint(0,20)]
      while name2 == name1: # So bot names don't repeat
         name2 = comps[randint(0, 20)]
      if players == 2 or players == 3 or players == 4:
         p3_is = 2
         name3 = comps[randint(0,20)]
         while name3 == name2 or name3 == name1:
            name3 = comps[randint(0,20)]
      if players == 3 or players == 4:
         p4_is = 2
         name4 = comps[randint(0,20)]
         while name4 == name2 or name4 == name1 or name4 == name3:
            name4 = comps[randint(0,20)]
      if players == 4:
         p5_is = 2
         name5 = comps[randint(0, 20)]
         while name5 == name2 or name5 == name1 or name5 == name3 or name5 == name4:
            name5 = comps[randint(0, 20)]
   else:
      while True:
         try:
            p1_is = int(input("\nPlayer One Is A: [1] Person [2] Computer\n"))
         except:
            print("\nError!\n"); continue
         else:
            if p1_is > 2 or p1_is < 1:
               continue
         break
      if p1_is == 1:
         name1 = str(input("\nPlayer One Name:\n"))
      else:
         name1 = comps[randint(0,20)]
      while True:
         try:
            p2_is = int(input("\nPlayer Two Is A: [1] Person [2] Computer\n"))
         except:
            print("\nError!\n"); continue
         else:
            if p2_is > 2 or p2_is < 1:
               continue
         break
      if p2_is == 1:
         name2 = str(input("\nPlayer Two Name:\n"))
      else:
         name2 = comps[randint(0,20)]
         while name2 == name1:
            name2 = comps[randint(0,20)]
      if players == 2 or players == 3 or players == 4:
         while True:
            try:
               p3_is = int(input("\nPlayer Three Is A: [1] Person [2] Computer\n"))
            except:
               print("\nError!\n"); continue
            else:
               if p3_is > 2 or p3_is < 1:
                  continue
            break
         if p3_is == 1:
            name3 = str(input("\nPlayer Three Name:\n"))
         else:
            name3 = comps[randint(0,20)]
            while name3 == name2 or name3 == name1:
               name3 = comps[randint(0, 20)]
      if players == 3 or players == 4:
         while True:
            try:
               p4_is = int(input("\nPlayer Four Is A: [1] Person [2] Computer\n"))
            except:
               print("\nError!\n"); continue
            else:
               if p4_is > 2 or p4_is < 1:
                  continue
            break
         if p4_is == 1:
            name4 = str(input("\nPlayer Four Name:\n"))
         else:
            name4 = comps[randint(0,20)]
            while name4 == name2 or name4 == name1 or name4 == name3:
               name4 = comps[randint(0, 20)]
      if players == 4:
         while True:
            try:
               p5_is = int(input("\nPlayer Five Is A: [1] Person [2] Computer\n"))
            except:
               print("\nError!\n"); continue
            else:
               if p5_is > 2 or p5_is < 1:
                  continue
            break
         if p5_is == 1:
            name5 = str(input("\nPlayer Five Name:\n"))
         else:
            name5 = comps[randint(0,20)]
            while name5 == name2 or name5 == name1 or name5 == name3 or name5 == name4:
               name5 = comps[randint(0, 20)]
   while True:
      try:
         end_var = int(input("\n[1] Best to Three [2] Best to Five [3] Best to Ten [4] Custom\n"))
      except:
         print("\nError!\n"); continue
      else:
         if end_var == 1:
            z = 3
         elif end_var == 2:
            z = 5
         elif end_var == 3:
            z = 10
         elif end_var == 4:
            while True:
               try:
                  z = int(input("\nScore Limit:\n"))
               except:
                  print("\nError!\n"); continue
               break
         else:
            continue
      break
   while True:
      turn_limit = str(input("\nEnable turn limit? [y/n]\n"))
      if turn_limit == "y":
         try:
            w = int(input("\nTurn Limit:\n"))
         except:
            print("\nError!\n")
            continue
      else: turn_limit = "n"
      break
   print()
   while True:
      print(Green.text("[{}]".format(name1), "light"))
      if p1_is == 1:
         try:
            p1 = int(input("pick any number between 1-{}:\n".format(x)))
         except ValueError:
            print("\nError!\n"); continue
      else:
         p1 = randint(1, x); print(p1)
      print(Blue.text("\n[{}]".format(name2), "light"))
      if p2_is == 1:
         try:
            p2 = int(input("pick any number between 1-{}:\n".format(x)))
         except ValueError:
            print("\nError!\n"); continue
      else:
         p2 = randint(1, x); print(p2)
      if players == 2 or players == 3 or players == 4:
         print(Red.text("\n[{}]".format(name3), "light"))
         if p3_is == 1:
            try:
               p3 = int(input("pick any number between 1-{}:\n".format(x)))
            except ValueError:
               print("\nError!\n"); continue
         else:
            p3 = randint(1, x); print(p3)
         if players == 3 or players == 4:
            print(Yellow.text("\n[{}]".format(name4), "light"))
            if p4_is == 1:
               try:
                  p4 = int(input("pick any number between 1-{}:\n".format(x)))
               except ValueError:
                  print("\nError!\n"); continue
            else:
               p4 = randint(1, x); print(p4)
            if players == 4:
               print(Magenta.text("\n[{}]".format(name5), "light"))
               if p5_is == 1:
                  try:
                     p5 = int(input("pick any number between 1-{}:\n".format(x)))
                  except ValueError:
                     print("\nError!\n"); continue
               else:
                  p5 = randint(1, x)
                  print(p5)
      print()
      magic_num = randint(1, x)
      if players == 1:
         if p1 == magic_num:
            print("{} Gained A Point!".format(Green.text(name1,"light")))
            one_p += 1
         if p2 == magic_num:
            print("{} Gained A Point!".format(Blue.text(name2,"light")))
            two_p += 1
         print("Score: {"+Green.text(one_p, "light")+"}-"+
               "{"+Blue.text(two_p, "light")+"}\n")
         print("The Number Was: {}\n".format(magic_num))
         if turn_limit == "y":
            turns += 1
            if turns == w:
               print("Game Over!\n")
               again = str(input("Do you want to play again? [y/n]\n"))
               if again == "y":
                  exit = 1
                  break
               break
         if one_p == z or two_p == z:
            print("Game Over!\n")
            again = str(input("Do you want to play again? [y/n]\n"))
            if again == "y":
               exit = 1
               break
            break
         else:
            continue
      if players == 2:
         if p1 == magic_num:
            print("{} Gained A Point!".format(Green.text(name1,"light")))
            one_p += 1
         if p2 == magic_num:
            print("{} Gained A Point!".format(Blue.text(name2,"light")))
            two_p += 1
         if p3 == magic_num:
            print("{} Gained A Point!".format(Red.text(name3,"light")))
            three_p += 1
         print("Score: {" + Green.text(one_p, "light") + "}-" +
               "{" + Blue.text(two_p, "light") + "}-"+"{"+Red.text(three_p,"light")+"}\n")
         print("The Number Was: {}\n".format(magic_num))
         if turn_limit == "y":
            turns += 1
            if turns == w:
               print("Game Over!\n")
               again = str(input("Do you want to play again? [y/n]\n"))
               if again == "y":
                  exit = 1
                  break
               break
         if one_p == z or two_p == z or three_p == z:
            print("Game Over!\n")
            again = str(input("Do you want to play again? [y/n]\n"))
            if again == "y":
               exit = 1
               break
            break
         else:
            continue
      if players == 3:
         if p1 == magic_num:
            print("{} Gained A Point!".format(Green.text(name1,"light")))
            one_p += 1
         if p2 == magic_num:
            print("{} Gained A Point!".format(Blue.text(name2,"light")))
            two_p += 1
         if p3 == magic_num:
            print("{} Gained A Point!".format(Red.text(name3,"light")))
            three_p += 1
         if p4 == magic_num:
            print("{} Gained A Point!".format(Yellow.text(name4,"light")))
            four_p += 1
         print("Score: {" + Green.text(one_p, "light") + "}-" +
               "{" + Blue.text(two_p, "light") + "}-" + "{" + Red.text(three_p, "light") + "}-"
               "{"+Yellow.text(four_p, "light")+"}\n")
         print("The Number Was: {}\n".format(magic_num))
         if turn_limit == "y":
            turns += 1
            if turns == w:
               print("Game Over!\n")
               again = str(input("Do you want to play again? [y/n]\n"))
               if again == "y":
                  exit = 1
                  break
               break
         if one_p == z or two_p == z or three_p == z or four_p == z:
            print("Game Over!\n")
            again = str(input("Do you want to play again? [y/n]\n"))
            if again == "y":
               exit = 1
               break
            break
         else:
            continue
      if players == 4:
         if p1 == magic_num:
            print("{} Gained A Point!".format(Green.text(name1,"light")))
            one_p += 1
         if p2 == magic_num:
            print("{} Gained A Point!".format(Blue.text(name2,"light")))
            two_p += 1
         if p3 == magic_num:
            print("{} Gained A Point!".format(Red.text(name3,"light")))
            three_p += 1
         if p4 == magic_num:
            print("{} Gained A Point!".format(Yellow.text(name4,"light")))
            four_p += 1
         if p5 == magic_num:
            print("{} Gained A Point!".format(Magenta.text(name5,"light")))
            five_p += 1
         print("Score: {" + Green.text(one_p, "light") + "}-" +
               "{" + Blue.text(two_p, "light") + "}-" + "{" + Red.text(three_p, "light") + "}-"
               "{" + Yellow.text(four_p, "light") + "}-"+
               "{" + Magenta.text(five_p, "light") + "}\n")
         print("The Number Was: {}\n".format(magic_num))
         if turn_limit == "y":
            turns += 1
            if turns == w:
               print("Game Over!\n")
               again = str(input("Do you want to play again? [y/n]\n"))
               if again == "y":
                  exit = 1
                  break
               break
         if one_p == z or two_p == z or three_p == z or four_p == z or five_p == z:
            print("Game Over!\n")
            again = str(input("Do you want to play again? [y/n]\n"))
            if again == "y":
               exit = 1
               break
            break
         else:
            continue
         continue
   if exit == 1: 
      print()
      continue
   break
#TODO Clean up code, Fix any error \n
#TODO add closest to numbers point
#TODO numbers can be or instead of the whole variable
