import sys
import os
import time
import termcolor

# Get user input for speed##
speed = input("Enter speed of the animation (in seconds): ")

# Define patterns
patterns = [
    ["◻︎   ","◻︎   ","◻︎   ","◻︎   ","◻︎   ","◻︎   ","◻︎   ","◻︎   ","◻︎   ","◻︎   ","◻︎   "],
    ["◼︎   ","◼︎   ","◼︎   ","◼︎   ","◼︎   ","◼︎   ","◼︎   ","◼︎   ","◼︎   ","◼︎   ","◼︎   "]
]

# Define colors
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

i = 0
while (True):  # change for loop to while loop
    if keyboard.is_pressed('esc'):  # if 'esc' is pressed, break the loop
        break
    os.system("clear")
    if i%11 == 0 :
        patterns[0] = ["◻︎   ","◻︎   ","◻︎   ","◻︎   ","◻︎   ","◻︎   ","◻︎   ","◻︎   ","◻︎   ","◻︎   ","◻︎   "]
    print(patterns[0][0]+patterns[0][1]+patterns[0][2]+patterns[0][3])
    print(patterns[0][9] + "Waiting " + patterns[0][4])
    print(patterns[0][8]+patterns[0][7]+patterns[0][6]+patterns[0][5])
    patterns[0][i%11] = termcolor.colored("◼︎   ", colors[i%len(colors)])

    patterns[1][i%11] = termcolor.colored("◼︎   ", colors[i%len(colors)])
    print(patterns[1][0]+patterns[1][1]+patterns[1][2]+patterns[1][3])
    print(patterns[1][9] + "Waiting " + patterns[1][4])
    print(patterns[1][8]+patterns[1][7]+patterns[1][6]+patterns[1][5])
    patterns[1][i%11] = "◻︎   "
    
    time.sleep(float(speed))
    i += 1  # increment is