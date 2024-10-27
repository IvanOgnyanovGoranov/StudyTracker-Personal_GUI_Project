from tkinter import Tk, Label, Button, font
from study_tracker_app import StudyTrackerApp

# Main application window
window = Tk()
window.title("Study Tracker")
window.config(padx=50, pady=50, bg="#1E1E1E")

# Create timer label
timer_font = font.Font(family="Century Gothic", size=30, weight="bold")
timer_label = Label(window, text='00:00', font=timer_font, fg="#FCFCFC", bg="#1E1E1E")
timer_label.grid(column=1, row=2)

# Labels
subjects_font = font.Font(family="Century Gothic", size=10, weight="bold")

daily_goal = Label(window, text='Pick your subject of study', font=subjects_font, fg="#FCFCFC", bg="#1E1E1E")
daily_goal.grid(column=1, row=1)

# Create an instance of the StudyTrackerApp class
app = StudyTrackerApp(window, timer_label, daily_goal)

# Buttons
start_button = Button(window, text='Start Timer', command=app.timer.start_timer)
start_button.grid(column=0, row=3)

stop_button = Button(window, text='Stop Timer', command=app.timer.stop_timer)
stop_button.grid(column=2, row=3)

add_time_button = Button(window, text='Add Time', command=app.add_study_time)
add_time_button.grid(column=1, row=5)

reset_button = Button(window, text='Reset', command=app.timer.reset_timer)
reset_button.grid(column=1, row=4)

manage_subjects_button = Button(window, text='Manage Subjects', command=app.manage_subjects)
manage_subjects_button.grid(column=1, row=0)

pick_subject_button = Button(window, text='Pick Subject', command=app.pick_subject)
pick_subject_button.grid(column=0, row=0)

show_stats_button = Button(window, text='Show Stats', command=app.show_stats)
show_stats_button.grid(column=2, row=0)

# Start the main loop
window.mainloop()