import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Storage Management")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0,1,2,3), weight=1)

        # create sidebar frame with widgets
        self.menu_frame = customtkinter.CTkFrame(self, width=240, corner_radius=0)
        self.menu_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.menu_frame.grid_rowconfigure(4, weight=1)
        self.add_button_1 = customtkinter.CTkButton(
                                                    self.menu_frame, 
                                                    text="Add Item",
                                                    command=self.add_item_page
                                                    )
        self.add_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.remove_item_button_2 = customtkinter.CTkButton(
                                                    self.menu_frame, 
                                                    text="Remove Item",
                                                    command=self.remove_item_page
                                                    )
        self.remove_item_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.available_check_button_3 = customtkinter.CTkButton(
                                                    self.menu_frame, 
                                                    text="Available",
                                                    command=self.available_check_page
                                                    )
        self.available_check_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.menu_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.menu_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.menu_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.menu_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # # create main entry and button
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        # self.entry.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        # self.main_button_1.grid(row=0, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # # create textbox
        # self.textbox = customtkinter.CTkTextbox(self, width=250)
        # self.textbox.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def add_item_page(self):
        print("Added")
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")


    def remove_item_page(self):
        print("Removed")

    def available_check_page(self):
        print("Checked")


if __name__ == "__main__":
    app = App()
    app.mainloop()