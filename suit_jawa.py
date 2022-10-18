import random
from traceback import print_tb
from unittest import result

user = str(input("Pilih (Batu, Gunting, Kertas): "))

result = ["Batu", "Gunting", "Kertas"]
action = random.choice(result)

print (f"\n Anda memilih {user}, Bot {action}. \n")

if user == action:
    print (f"{user} Seri")
elif user == "Batu":
    if action == "Gunting":
        print("Batu menang! Anda Juara!")
    else:
        print("Kertas Menang!, Anda Kalah.")
elif user == "Kertas":
    if user == "Batu":
        print("Kertas Menang!, Anda juara!")
    else:
        print("Gunting Mendang, Anda Kalah.")
elif user == "Gunting":
    if action == "Kertas":
        print("Gunting Menang, Anda Juara!")
    else:
        print("Batu memang, Anda Kalah")
