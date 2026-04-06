#holy shit i pushed to git anyways let's code now

import tkinter as tk 
import time

#timer function
#i just discovered an edge case while trying to find ways to measure time elasped
#if the system time changes while the timer is running it can cause whacky behaviour
#nothing to worry about rn but definitely in future
#anyways

# start_sec = 0
# new_sec = 0
# seconds = 0
# start_sec = int(time.time())
# for i in range (100000000):

#     new_sec= int(time.time())
#     seconds = new_sec - start_sec 
#     print (seconds)
    
#timer works BARELY
def update():
    if is_running == True:
        seconds = start_timer - int(time.time())


is_running=False
def start_timer():
    is_running=True
    start_time= int(time.time())
    update()



# #tk boilerplate
root = tk.Tk()
label-tk.Label(root,text=seconds)

root.title("timer")
button = tk.Button(root, text="start", width=25, command=start_timer())
button.pack()
root.mainloop()