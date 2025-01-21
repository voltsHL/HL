import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Infernium - Combat Warriors 12b")
root.geometry("600x400")
root.configure(bg="#2E1A47")

# Sidebar frame (Left Panel)
sidebar = tk.Frame(root, bg="#1F1230", width=150, height=400)
sidebar.pack(side="left", fill="y")

# Sidebar buttons
sections = ["Player", "Legit", "Rage", "Parry", "ESP", "Sounds", "Changer", "World", "Misc"]
for section in sections:
    btn = tk.Button(sidebar, text=section, bg="#3B245F", fg="white", relief="flat", width=15)
    btn.pack(pady=5, padx=5)

# Main panel frame (Right Side)
main_panel = tk.Frame(root, bg="#2E1A47")
main_panel.pack(side="right", expand=True, fill="both", padx=20, pady=20)

# Title label
title_label = tk.Label(main_panel, text="Player", font=("Arial", 16, "bold"), bg="#2E1A47", fg="white")
title_label.pack(pady=10)

# Function to update labels with slider values
def update_values():
    walk_speed_label.config(text=f"Walk Speed: {walk_speed.get()}")
    fly_speed_label.config(text=f"Fly Speed: {fly_speed.get()}")
    fov_label.config(text=f"FOV: {fov.get()}")

# Walk Speed
walk_speed = tk.IntVar(value=40)
walk_speed_label = tk.Label(main_panel, text="Walk Speed: 40", bg="#2E1A47", fg="white")
walk_speed_label.pack()
walk_speed_slider = ttk.Scale(main_panel, from_=0, to=100, orient="horizontal", variable=walk_speed, command=lambda e: update_values())
walk_speed_slider.pack()

# Fly Toggle
fly_toggle = tk.BooleanVar()
fly_toggle_btn = ttk.Checkbutton(main_panel, text="Fly Toggle", variable=fly_toggle)
fly_toggle_btn.pack()

# Fly Speed
fly_speed = tk.IntVar(value=50)
fly_speed_label = tk.Label(main_panel, text="Fly Speed: 50", bg="#2E1A47", fg="white")
fly_speed_label.pack()
fly_speed_slider = ttk.Scale(main_panel, from_=0, to=100, orient="horizontal", variable=fly_speed, command=lambda e: update_values())
fly_speed_slider.pack()

# FOV Toggle
fov_toggle = tk.BooleanVar()
fov_toggle_btn = ttk.Checkbutton(main_panel, text="FOV Toggle", variable=fov_toggle)
fov_toggle_btn.pack()

# FOV
fov = tk.IntVar(value=70)
fov_label = tk.Label(main_panel, text="FOV: 70", bg="#2E1A47", fg="white")
fov_label.pack()
fov_slider = ttk.Scale(main_panel, from_=30, to=120, orient="horizontal", variable=fov, command=lambda e: update_values())
fov_slider.pack()

# Run the application
root.mainloop()
