from datetime import datetime
from datetime import timezone
import tkinter as tk
from tkinter import ttk, messagebox
import pystray
from PIL import Image, ImageTk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Silksong Clock")
        self.iconbitmap("./images/icon.ico")
        self.protocol("WM_DELETE_WINDOW", self.minimize_to_tray)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Silksong.TFrame", foreground="white", background="black")
        style.configure(
            "Silksong.TButton",
            foreground="white",
            background="#e83046",
            font=("Arial", 13),
        )
        style.map("Silksong.TButton", background=[("active", "#7e1919")])

        self.logo = Image.open("./images/logo_silksong.png").resize((161, 83))
        self.logo = ImageTk.PhotoImage(self.logo)

        frame = ttk.Frame(self, style="Silksong.TFrame", padding=10)
        frame.grid(column=1)

        self.timer_var = tk.StringVar()

        self.title_label = ttk.Label(
            frame,
            background="black",
            foreground="white",
            text="Silksong Launch Clock",
            font=("Arial", 16),
        )
        self.title_label.grid(column=0, row=0, columnspan=2)

        self.logo_label = ttk.Label(
            frame,
            image=self.logo,
            background="black",
            foreground="white",
            font=("Arial", 13),
        )
        self.logo_label.grid(column=0, row=1)

        self.time_label = ttk.Label(
            frame,
            background="black",
            foreground="#e83046",
            textvariable=self.timer_var,
            font=("Arial", 13),
        )
        self.time_label.grid(column=0, row=2)

        self.quit_button = ttk.Button(
            frame,
            text="Quit",
            command=self.destroy,
            style="Silksong.TButton",
        )
        self.quit_button.grid(column=0, row=3)

        self.countdown_timer()

    def minimize_to_tray(self):
        self.withdraw()
        image = Image.open("./images/icon.ico")
        menu = (
            pystray.MenuItem("Show", self.show_window),
            pystray.MenuItem("Quit", self.quit_window),
        )
        icon = pystray.Icon("name", image, "Silksong Clock", menu)
        icon.run()

    def quit_window(self, icon):
        icon.stop()
        self.destroy()

    def show_window(self, icon):
        icon.stop()
        self.after(0, self.deiconify)

    def countdown_timer(self):
        start_time = datetime.now(tz=timezone.utc)
        end_time = datetime(2025, 9, 4, 14, 0, 0, tzinfo=timezone.utc)

        silksong_launch_time = end_time - start_time
        counter = int(silksong_launch_time.total_seconds())

        years = silksong_launch_time.days // 365
        months = (silksong_launch_time.days % 365) // 30
        days = (silksong_launch_time.days % 365) % 30
        hours = silksong_launch_time.seconds // 3600
        minutes = (silksong_launch_time.seconds % 3600) // 60
        seconds = silksong_launch_time.seconds % 60

        if counter > 0:
            counter = int(silksong_launch_time.total_seconds())
            self.timer_var.set(
                f"Launch in: {years} years, {months} months, {days} days, {hours:02}:{minutes:02}:{seconds:02}"
            )

            self.after(1000, lambda: self.countdown_timer())
        else:
            self.game_launched()

    def game_launched(self):
        self.timer_var.set(f"Silksong has launched!!!!!!!!!!")
        self.time_label.config(foreground="green")
        messagebox.showinfo("Launched on Steam!", "Silksong has launched on Steam")
