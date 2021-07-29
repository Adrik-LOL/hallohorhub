#!/usr/bin/python

__autor__ = "AdrianoTech#7163"
__server__ = "Halloween Horror : https://discord.com/invite/eU5G5TF"
clear = lambda: os.system('cls')

import time
import os

print(__autor__, "Present in collaborating with", __server__)
time.sleep(5)
clear()
print("██╗░░██╗░█████╗░██╗░░░░░██╗░░░░░░█████╗░░██╗░░░░░░░██╗███████╗███████╗███╗░░██╗")
print("██║░░██║██╔══██╗██║░░░░░██║░░░░░██╔══██╗░██║░░██╗░░██║██╔════╝██╔════╝████╗░██║")
print("███████║███████║██║░░░░░██║░░░░░██║░░██║░╚██╗████╗██╔╝█████╗░░█████╗░░██╔██╗██║")
print("██╔══██║██╔══██║██║░░░░░██║░░░░░██║░░██║░░████╔═████║░██╔══╝░░██╔══╝░░██║╚████║")
print("██║░░██║██║░░██║███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░███████╗███████╗██║░╚███║")
print("╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░╚══╝")
print("                                                                               ")
print("██╗░░██╗░█████╗░██████╗░██████╗░░█████╗░██████╗░  ██╗░░██╗██╗░░░██╗██████╗░    ")
print("██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██║░░██║██║░░░██║██╔══██╗    ")
print("███████║██║░░██║██████╔╝██████╔╝██║░░██║██████╔╝  ███████║██║░░░██║██████╦╝    ")
print("██╔══██║██║░░██║██╔══██╗██╔══██╗██║░░██║██╔══██╗  ██╔══██║██║░░░██║██╔══██╗    ")
print("██║░░██║╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░░██║  ██║░░██║╚██████╔╝██████╦╝    ")
print("╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═╝░░╚═╝░╚═════╝░╚═════╝░    ")
print("")
print("1 : Server Invite")
print("2 : What our server offer")
print("3 : Our ToS")
selection = input("Input : ")

numinput = selection
numinput = int(numinput)

if numinput == 1:
  clear()
  print("Here we Go! https://discord.com/invite/eU5G5TF")
  time.sleep(10)
  clear()
  while 1:
    os.system("hallohorhub.py")
    print("Restarting...")
    exit()
elif numinput == 2:
   clear()
   print("This server offer a lot of fun with other halloween fans, watch horror movie and more!")
   time.sleep(20)
   clear()
   while 1:
    os.system("hallohorhub.py")
    print("Restarting...")
    exit()
elif numinput == 3:
    clear()
    f = open("tos.hub", "r")
    print(f.read())
    wait = input("PRESS ANY KEY TO EXIT")




