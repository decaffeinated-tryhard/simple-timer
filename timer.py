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
seconds=0
cur_time = 0

def update():
    if is_running == True:
        global seconds
        global cur_time
        cur_time=int(time.time())
        seconds = start_time - cur_time
        print (is_running)
        print(start_time)
        print(cur_time)

is_running=False

start_time=0

def start_timer():
    global is_running
    is_running=True
    global start_time
    start_time= int(time.time())
    update()

def printfffff():
    print (is_running)
    print(start_time)
    print(cur_time)


# #tk boilerplate
root = tk.Tk()

label=tk.Label(root,text=seconds)
label.pack()
root.title("timer")
button = tk.Button(root, text="start", width=25, command=start_timer)
button.pack()
button = tk.Button(root, text="debug", width=25, command=printfffff)
button.pack()

root.mainloop()