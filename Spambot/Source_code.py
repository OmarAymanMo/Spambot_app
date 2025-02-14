import customtkinter as ctk
import keyboard
from time import sleep
from tkinter import messagebox
import threading


ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue") 

class MainScreen(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        
        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        title_label = ctk.CTkLabel(self.content, text="Message Spammer", font=("Arial", 24, "bold"))
        title_label.grid(row=0, column=0, padx=10, pady=(10, 20))

        self.message_input = ctk.CTkEntry(self.content, placeholder_text="Enter your message", width=300, height=40)
        self.message_input.grid(row=1, column=0, pady=(0, 10))

        self.count_input = ctk.CTkEntry(self.content, placeholder_text="Number of times", width=300, height=40)
        self.count_input.grid(row=2, column=0, pady=(0, 10))

        send_button = ctk.CTkButton(self.content, text="Send", width=150, height=40, command=self.send_messages)
        send_button.grid(row=3, column=0, pady=(0, 20))

        copyright = ctk.CTkLabel(self.content, text="© 2025 by Omar Ayman", font=ctk.CTkFont(size=12))
        copyright.grid(row=4, column=0, pady=(10, 0))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def send_messages(self):
        try:
            if self.message_input.get() == "":
                self.show_error_popup("Please enter a message!")
                return

            count = int(self.count_input.get())
            if count <= 0:
                self.show_error_popup("Please enter a valid number!")
                return

            self.show_confirmation_popup()
        except ValueError:
            self.show_error_popup("Please enter a valid number!")

    def start_sending(self, num_of_messages):
        message = self.message_input.get()
        for _ in range(num_of_messages):
            keyboard.write(message)
            keyboard.press_and_release("enter")
            sleep(0.015)

    def show_error_popup(self, message):
        messagebox.showerror("Error", message)

    def show_confirmation_popup(self):
        if int(self.count_input.get()) > 1000:
            confirmation = messagebox.askyesno("Warning", f"Are you sure you want to send {int(self.count_input.get())} messages?")
        else:
            confirmation = True
        if confirmation:
            response = messagebox.askyesno("Switch to a Chat", "You have 10 seconds to switch to a chat. Do you want to proceed?")
            if response:
                count = int(self.count_input.get())
                sleep(10) 
                threading.Thread(target=self.start_sending, args=(count,), daemon=True).start()

class SpamBotApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Spam_Bot")
        self.geometry("340x300")
        self.resizable(False, False)
        self.iconbitmap("Omarbot.ico")
        MainScreen(self).pack(fill='both', expand=True)

if __name__ == "__main__":
    app = SpamBotApp()
    app.mainloop()
