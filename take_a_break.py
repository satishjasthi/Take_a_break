import webbrowser
import time

from Tkinter import * # \ libraries for creating pop up messages
import tkMessageBox   # /

name = raw_input('Please enter your name \n')
work_time = raw_input('\n Hi ' + name + ' Please enter the number of minutes you would like to work :) \n')
work_time = float(work_time)
work_time = work_time * 60
break_time = raw_input('\n Hi ' + name + ' Please enter your break time in minutes :) \n')
break_time = float(break_time)
break_time = break_time * 60

count  = 0
while count <4:
	time.sleep(work_time) # pauses the program for given number of seconds ,here it's 10 sec
	root = Tk().withdraw()  # hiding the main window
	var1 = tkMessageBox.askyesno("Break Time", ('Hi ' + name + " would you like to take a break? "))

	if var1 == True:
		 webbrowser.open('https://www.youtube.com/watch?v=h3Ceprv9wJs')
		 count += 1
                 time.sleep(break_time)
                 var3  = tkMessageBox.askyesno("Back to work","Hi " + name + " your break session is over,would you like to go back to work?")
                 if var3 == True:
                          continue
                 else :
                          break

	else:
                var2 = tkMessageBox.askyesno("Back to work",("Hi " + name + " would you like to continue your work?"))
                if var2 == True:
                         continue
		else:
                         break









