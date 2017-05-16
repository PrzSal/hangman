#!/usr/bin/env python3
import random
import time
import sys

def logo():
    print
    ('''
    ██████╗ ██╗   ██╗███╗   ██╗██████╗  █████╗ ██╗     ███████╗ ██████╗
    ██╔══██╗╚██╗ ██╔╝████╗  ██║██╔══██╗██╔══██╗██║     ██╔════╝██╔════╝
    ██║  ██║ ╚████╔╝ ██╔██╗ ██║██║  ██║███████║██║     █████╗  ██║
    ██║  ██║  ╚██╔╝  ██║╚██╗██║██║  ██║██╔══██║██║     ██╔══╝  ██║
    ██████╔╝   ██║   ██║ ╚████║██████╔╝██║  ██║███████╗███████╗╚██████╗
    ╚═════╝    ╚═╝   ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ F5.00
    ''')


def draw_hangman():
    hangman =(
    '''






    [][][]
            ''',
    '''




        []
        []
    [][][]
            ''',
    '''


        []
        []
        []
        []
    [][][]
            ''',
    '''
        []
        []
        []
        []
        []
        []
    [][][]
            ''',
    '''
        [][][]
        []   |
        []
        []
        []
        []
    [][][]
            ''',
    '''
        [][][]
        []   |
        []   o
        []  -0-
        []   ^
        []
    [][][]
            ''')
    return hangman


def ask_for_letter_again(letter, used=[]):
    '''In this funcion input guess letter'''
    print("\n You've already lettered the letter:", letter, "\n", used)
    letter = input("\n\nEnter your guess: ").upper()
    return letter


def print_summary_ask_again(number_of_tries, gametime):
    '''This funcion inform about what do you want after end game'''
    print ("After " + str(number_of_tries) + " TRIES, IT TOOK YOU " + str(int(gametime)) + "sec")
    again = ''
    while again != 'yes' and again != "no":
        again = input('Do you want to play again (yes/no): ')
        #gametime = 0
    if again == 'no':
        sys.exit()
    return again#, gametime


def number_of_tries_guess(letter, city_to_guess, hidden_capital, used, word):
    '''This funcion worked on input letter and added to true statment'''
    new = ''
    letter_in_city_to_guess = []
    for i in range(len(city_to_guess)):
        letter_in_city_to_guess += city_to_guess[i]
        if letter == city_to_guess[i]:
            new += letter
        elif word == city_to_guess[i]:
            new += word
        else:
            new += hidden_capital[i]
    hidden_capital = new
    print(hidden_capital)
    return hidden_capital, used


def open_close_txt():
    files = open("capitals.txt")    # otwieranie pliku z listą państwo-stolica
    reader = files.readlines()
    files.close()
    return reader


def random_choice(reader):
    print ("Welcome to Hangman. Good luck!")
    choices = random.choice(reader).upper()
    choices = choices.split(" | ")
    return choices


def randomisiation_cities(choices, city_to_guess, country):
    choices[1] = choices[1].strip()
    city_to_guess = choices[1]
    country = choices[0]

    hidden_capital = "_" * len(city_to_guess)
    print("Country: ", country)
    print("Capitol: ", city_to_guess)
    word = input("Enter capitol name: ").upper()
    return word, city_to_guess, country, hidden_capital


def main():

    logo()
    hangman = draw_hangman()
    reader = open_close_txt()

    again = "yes"
    while again == "yes" or wrong < max_wrong or hidden_capital != city_to_guess:
        city_to_guess = ''
        country = ''
        number_of_tries = 1
        hidden_capital = ''
        letter = ''
        used = ['']
        wrong = 0
        start = time.time()
        if again == "no":
            sys.exit()

        else:   # losowowanie stolic
            choices = random_choice(reader)
            word, city_to_guess, country, hidden_capital = randomisiation_cities(choices, city_to_guess, country)
            max_wrong = len(hangman) - 1
            print(country)

            if word == city_to_guess:    # jesli zgadlismy odrazu wygrywamy po jednej probie
                number_of_tries = 1
                again = print_summary_ask_again(number_of_tries, time.time() - start)  # funkcja wygranej i pytanie o powtorka

            elif word not in city_to_guess and len(word) >= 2:   # jesli nie zgadlismy ruszamy dalej z bledem
                print('No gueesed')
                again = print_summary_ask_again(number_of_tries, time.time() - start)    # print ("\n You are wrong !!! :( \n")

            else:
                letter = letter + word
                print ("country: ", country)
                again = 'yes'
                while again == 'yes' and wrong < max_wrong and hidden_capital != city_to_guess:
                    letter = ask_for_letter_again(letter, used)
                    print("\nSo far, the word is:\n", hidden_capital)    # wprowadzamy literki
                    while (letter in used):
                        letter = ask_for_letter_again(letter)
                    used.append(letter)

                    if letter in city_to_guess or word in city_to_guess:
                        print ("\n Yes! The letter", letter, "is in the Capital :)")  # literka jest ok, podstawiana jest pod "_" i zaliczamy probe
                        number_of_tries += 1
                        hidden_capital, used = number_of_tries_guess(letter, city_to_guess, hidden_capital, used, word)   # wywolanie funkcjii zwracajacej odpowiednia wartosc "guess"

                    if letter not in city_to_guess:
                        print(city_to_guess)
                        print("\nSorry,", letter, "isn't in this city_to_guess name.")
                        wrong += 1  # bledna literka jest dopisywana do listy
                        number_of_tries += 1
                        print(hangman[wrong])

            if wrong == max_wrong:    # przegrywamy
                print ("\nYou've been hanged!")
                print ("\nThe city_to_guess was", city_to_guess)
                again = print_summary_ask_again(number_of_tries, time.time() - start)

            elif hidden_capital == city_to_guess:
                print ("\nYou guessed it!")     # wygralismy
                again = print_summary_ask_again(number_of_tries, time.time() - start)


main()
