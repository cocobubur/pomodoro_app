import tkinter as tk
from playsound import playsound
import time

# Global variables to manage the timer state
paused = False # Pause button
time_remaining = 0 # countdown timer
pomodoro_counter = 0 # variable that counts how many pomodoro sesssions completed


sound_file = "/Users/davidositorus/Documents/passion_projects/timerApp/Present heal.mp3" # change to alarm sound
icon_file = "/Users/davidositorus/Downloads/Digital_Watch_App.png" # change app icon

# button to start pomodoro
def start_timer(): 
    global time_remaining # uses the declared global variable 
    # try-except block to get time remaining based on input time
    try:
        time_remaining = int(entry.get()) # get input time
    except ValueError:
        label.config(text="Please enter a valid number.") # raise exception for negative numbers or non-numbers
        return

    label.config(text=f"Time remaining: {time_remaining} seconds") # set label text 
    entry.config(state='disabled') # set state of entry field to disabled
    start_button.config(state='disabled') # set state of start button to disabled
    pause_button.config(state='normal') # set state of pause button to normal
    
    countdown() # begin countdown

# countdown time function, logic for timer countdown
def countdown():
    global time_remaining, paused, entry, start_button, pause_button, pomodoro_counter, pomodoro_label# use global variables

    while time_remaining > 0 and not paused: # while countdown has not finished and not pausing
        mins, secs = divmod(time_remaining, 60) # use divmod function to get remainder of time-remaining
        time_format = f'{mins:02d}:{secs:02d}' # set time format to 2 decimal points for minutes and seconds
        label.config(text=f"Time remaining: {time_format}") # set text for label field of time remaining
        root.update() # update root function event loop
        time.sleep(1) # delay time by one second
        time_remaining -= 1 # reduce countdown by one second

    if time_remaining == 0: # if time has reduced to 0 seconds
        pomodoro_counter += 1
        entry.config(state='normal') # set entry field's state to normal
        start_button.config(state='normal') # set start button's state to normal
        pause_button.config(state='disabled', text="Pause") # disable pause button and set text to pause
        pomodoro_label.config(text=f"Pomodoros completed: {pomodoro_counter}")
        # label.config(text="Time's up! Pomodoro complete!") # set text 
        playsound(sound_file) # play alarm
        

        

def pause_resume_timer():
    global paused
    if paused: # if already paused, then unpause when it is reclicked
        paused = False
        pause_button.config(text="Pause")
        countdown()
    else: # unpaused, so now pause after button is pressed
        paused = True 
        pause_button.config(text="Resume") # set button's text indicator to display resume for resuming

def create_app():
    global root, entry, label, start_button, pause_button, pomodoro_counter, pomodoro_label # declare global variables

    root = tk.Tk() # initialize app and store in root variable name
    root.title("Pomodoro Timer App") # set title of app
    label = tk.Label(root, text="Timer App") # set label name variable for the root object with name
    label.pack() 

    # Set the app logo (icon)
    logo = tk.PhotoImage(file=icon_file)  # Use .png for Linux/Windows/MacOS
    root.iconphoto(False, logo) # give root object an icon photo

    # Create entry/user-input field for seconds
    entry = tk.Entry(root, width=10, font=('Arial', 30)) # declare entry widget variable to display text
    entry.pack(pady=20) # set field pack widget size dimensions
    
    # Create a label to display the time
    label = tk.Label(root, text="Enter time in seconds", font=('Comic_Sans', 14))
    label.pack(pady=30, padx= 30)
    
    # Create a label to display the pomodoro session counter
    pomodoro_label = tk.Label(root, text= f"Pomodoros completed: {pomodoro_counter}", font=('Comic_Sans', 14))
    pomodoro_label.pack(pady=30, padx= 30)
    
    # Create a start button
    start_button = tk.Button(root, text="Start Timer", command=start_timer, font=('Arial', 14)) # command sets function to be triggered when pressed
    start_button.pack(pady=19.2, padx= 10.8)

    # Create a pause/resume button
    pause_button = tk.Button(root, text="Pause", command=pause_resume_timer, font=('Arial', 14), state='disabled')
    pause_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_app()
