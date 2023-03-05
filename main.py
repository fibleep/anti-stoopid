import tkinter
import customtkinter as ctk
from controller import Controller

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class Runner(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        controller = Controller()
        self.title("ANTI STOOPID")
        self.geometry("800x200")
        self.buttonLabel = ctk.CTkLabel(
            self, text="ENTER ANTI STOOPID MODE", font=("Arial", 20))
        self.button = ctk.CTkButton(self, text="CLICK", command=controller.toggle_focus, 
                                width=20, height=40, corner_radius=50, font=("Arial", 20))
        self.buttonLabel.pack()
        self.button.pack()


if __name__ == "__main__":
    app = Runner()
    app.mainloop()
