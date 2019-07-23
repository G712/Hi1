import pygame
import random

print("--------------------------------------------------------------------------------------------------------------")
print("-----------        ----------         ---       ---         -----------")
print("     -              -                                            -")
print("     -              --------               ---                   -")
print("     -              -                                            - ")
print("     -              --------           ---       ---             -")
print()
print()
print()
print("     --------       --------         -                 -  ---------      --       -     ------------     ")
print("     -      -       -        -         -             -    -              -  -     -           -          ")
print("     --------       -        -           -         -      --------       -    -   -           -          ")
print("     -      -       -       -              -    -         -              -      - -           -             ")
print("     -      -       -------                  -            ---------      -        -           -          ")
print("-     -          ------         -------")
print("-     -          -    -         -")
print("-     -          ------         -------")
print("-     -          -     -        -")
print("-------          -      -       -------")
print("------------------------------------------------------------------------------------------------------------")
name = input("Hello! Please enter your name: ")
print("Well, hello, " + name + "!")
user_class = input("Ok, " + name + ", let's start creating your hero. First, choose a class; either warrior, or mage.")
if user_class == "Warrior":
    print("So, " + name + " the warrior, let's continue.")
    user_questlevel = input("Now, choose a quest level: easy, med, or hard.")
    if user_questlevel == "Hard":
        print("Hard? Well then, let's start.")
        print()
        print("A troll lives near a town. Every day, the troll attacks the town. Your job is to kill the troll.")
        print("The troll will attack at sunrise.")
        choice1 = input("It is close to sunrise. You are armed with a sword. Will you visit the troll's lair, or rest?")
        if choice1 == "Rest":
            print("You get some rest.")
            print("*STOMP. STOMP.* The small inn you are staying in gets smashed on by the troll.")
            print("You see the sun slowly rising over the town.")
            print("The sun has risen.")
            print("With one final stomp, you are crushed.")
            print("GAME OVER...")
            exit()
        if choice1 == "Easy":
            print("Easy, you say? Easy it is. Let's start.")
            print("You are armed with a sword, and leather armor.")
            print("Your job is too defend a town nearby from being destroyed by an atomic bomb from a nearby evil guy.")
            choice2 = input("Do you go find the evil guy? Or maybe go interact with the town?(Enter Town or Guy)")
            if choice2 == "Guy":
                print("You embark on an adventure to find the evil guy. I know, it sounds lame.")

if user_class == "Mage":
    print(name + ", the mage. Huh. Not bad. Well, let's continue with your hero creation.")
    user_questlevel = input("Ok. Let's choose a level. Enter easy or hard:")
else:
    print("Sorry, but you didn't enter warrior or mage. Make sure the first letter is capital!")
    print("-----------------------------------------------------------------------------------")
    print("Taking you to main menu...")
    print("Please run the program again.")