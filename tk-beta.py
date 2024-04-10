import customtkinter
import os
from PIL import Image
import time

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Panel")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
        self.sw_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "music_sw_black.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "music_sw_light.png")), size=(20, 20))
        self.tts_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "music_tts_black.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "music_tts_light.png")), size=(20, 20))
        self.mario_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "music_mario_black.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "music_mario_light.png")), size=(20, 20))
        self.frog_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "music_frog_black.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "music_frog_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" Panel", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Music",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Controlls",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Settings",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=5, column=0, sticky="ew")

        #self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["System", "Light", "Dark"],
        #                                                        command=self.change_appearance_mode_event)
        #self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom")
        self.home_frame_button_4.grid(row=5, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0.5, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)

        self.music_frames = customtkinter.CTkFrame(self.second_frame, corner_radius=0.5)
        self.music_frames.grid_columnconfigure(0, weight=1)
        self.music_frames.grid(row=0, column=0, padx=0.5, pady=0.5)

        self.music_title_image = customtkinter.CTkLabel(self.music_frames, text="", image=self.large_test_image)
        self.music_title_image.grid(row=0, column=0, padx=20, pady=10)

        self.music_mario_button = customtkinter.CTkButton(self.music_frames, text=" Mario Theme", image=self.mario_image)
        self.music_mario_button.grid(row=3, column=0, padx=20, pady=10)

        self.music_sw_button = customtkinter.CTkButton(self.music_frames, text=" Star Wars", image=self.sw_image)
        self.music_sw_button.grid(row=4, column=0, padx=20, pady=10)

        self.music_frog_button = customtkinter.CTkButton(self.music_frames, text=" Crazy Frog", image=self.frog_image)
        self.music_frog_button.grid(row=5, column=0, padx=20, pady=10)

        self.music_tts_button = customtkinter.CTkButton(self.music_frames, text=" TT Little Star", image=self.tts_image)
        self.music_tts_button.grid(row=6, column=0, padx=20, pady=10)

        self.volume_switcher = customtkinter.CTkSlider(self.music_frames)
        self.volume_switcher.grid(row=7, column=0, padx=20, pady=10)

        self.loop_button = customtkinter.CTkSwitch(self.music_frames, text=" Loop")
        self.loop_button.grid(row=8, column=0, padx=20, pady=10)

        self.volume_switcher.set(0)

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
            print("Hi! Frame 2 activated! =3")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")
        print("Hi! Frame 2 registerd! =3")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    #def change_appearance_mode_event(self, new_appearance_mode):
    #    customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()