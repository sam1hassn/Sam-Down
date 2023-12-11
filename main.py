from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout ,BoxLayout
from kivy.uix.settings import SettingsWithTabbedPanel
from pytube import YouTube
from pytube.cli import on_progress
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.text import LabelBase
from kivy.core.clipboard import Clipboard
from kivy.clock import Clock
from kivmob import KivMob, TestIds
from kivmob import RewardedListenerInterface




class VideoDownloaderApp(MDApp):
    def build(self):
        self.screen = MDScreen()
        self.theme_cls.theme_style = "Light"  # اختر Dark لاستخدام الوضع الداكن
        self.theme_cls.primary_palette = "Blue"  # اختر اللون الذي تفضله هنا
        
        self.show_banner_ad()
        self.Rewarded_Video()

        
       
  

        # Textfield for entering video URL
        self.url_input = MDTextField(
            hint_text="Enter video URL",
            helper_text="Example: https://www.youtube.com/watch?v=your_video_id",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            size_hint=(0.8, None),
            height=dp(48),
            helper_text_mode="on_focus"
        )
        self.screen.add_widget(self.url_input)

        # Label for displaying video title
        self.video_title_label = MDLabel(
            text="Video Title: ",
            theme_text_color="Secondary",
            halign="center",
            pos_hint={"center_x": 0.15, "center_y": 0.35},
        )
        self.screen.add_widget(self.video_title_label)

        # Label title main
        self.main_title_label = MDLabel(
            text="Sam Downloader ",
            theme_text_color="Primary",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.85},
            font_style ="H4",
        )
        self.screen.add_widget(self.main_title_label)

        # Label for displaying video size
        self.video_size_label = MDLabel(
            text="Video Size: ",
            theme_text_color="Secondary",
            halign="center",
            pos_hint={"center_x": 0.15, "center_y": 0.3},
        )
        self.speed_label = MDLabel(
            text="Speed: ",
            halign="center",
            theme_text_color="Secondary",
            pos_hint={"center_x": 0.15, "center_y": 0.25},
        )
        self.screen.add_widget(self.speed_label)
        self.screen.add_widget(self.video_size_label)

         # Dropdown menu for selecting video quality
        self.quality_menu_button = MDRaisedButton(
            text="Select Quality",
            pos_hint={"center_x": 0.5, "center_y": 0.75},
            on_release=self.show_quality_menu,
        )
        self.screen.add_widget(self.quality_menu_button)

        # Default quality selection
        self.selected_quality = "360p"

        # Button for change color
        self.change_color_button = MDRaisedButton(
            text="Dark",
            pos_hint={"center_x": 0.1, "center_y": 0.95},
            on_release=self.change_color,
        )
        self.screen.add_widget(self.change_color_button)

          # Button for pasting text
        self.paste_button = MDFillRoundFlatButton(
            text="Paste",
            pos_hint={"center_x": 0.9, "center_y": 0.6},
            on_release=self.paste_text,
            
        )
        self.screen.add_widget(self.paste_button)


        # Button to start download
        self.download_button = MDRaisedButton(
            text="Download",
            pos_hint={"center_x": 0.65, "center_y": 0.5},
            on_release=self.download_video,
        )
        self.screen.add_widget(self.download_button)
        # Button to start download
        self.Audio_button = MDRaisedButton(
            text="Audio Only",
            pos_hint={"center_x": 0.35, "center_y": 0.5},
            on_release=self.download_audio,
        )
        self.screen.add_widget(self.Audio_button)

        # Progress bar to show download progress
        self.progress_bar = MDProgressBar(
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            size_hint=(0.8, None),
            height=dp(20),
        )
        self.screen.add_widget(self.progress_bar)

        return self.screen


    def download_video(self, *args):
        self.show_interstitial_ad()
        # Get the video URL from the input field
        video_url = self.url_input.text
        
      

        try:
            # Create a YouTube object
            yt = YouTube(video_url,on_progress_callback=self.on_progress)
            
            # Get the highest resolution stream
            video_stream = yt.streams.filter(res=self.selected_quality).first()
            self.display_video_info(video_stream)
            
            # Define the location for saving the video
            save_location = "/home/sam/Desktop/Downlaoder/"
            
            # Download the video
            
          
            video_stream.download(save_location)

            # Display a success message
            self.show_success_dialog()

        except Exception as e:
            # Display an error message if the download fails
            self.show_error_dialog(str(e))
            print(e)

    def download_audio(self, *args):
        self.show_interstitial_ad()
        # Get the video URL from the input field
        video_url = self.url_input.text

        try:
            # Create a YouTube object
            yt = YouTube(video_url, on_progress_callback=self.on_progress)

            # Get the highest resolution audio stream
            audio_stream = yt.streams.filter(only_audio=True).first()
            self.display_video_info(audio_stream)
            file_name = f'{audio_stream.title}.mp3'
            # Define the location for saving the audio
            save_location = "/home/sam/Desktop/Downlaoder/"

            # Download the audio
            audio_stream.download(save_location,filename=file_name)

            # Display a success message
            self.show_success_dialog()

        except Exception as e:
            # Display an error message if the download fails
            self.show_error_dialog(str(e))

    def change_color(self,*args):
              self.show_interstitial_ad()
              # self.theme_cls.theme_style = "Dark"  # اختر Dark لاستخدام الوضع الداكن
              # self.theme_cls.primary_palette = "Blue"  # اختر اللون الذي تفضله هنا
              if self.theme_cls.theme_style == "Dark":
                  self.theme_cls.theme_style = "Light"
                  self.theme_cls.primary_palette = "Blue"
                  self.change_color_button.text="Dark"
              else:
                  self.theme_cls.primary_palette = "DeepPurple"
                  self.theme_cls.theme_style = "Dark"
                  self.change_color_button.text="Light"
      
    def show_success_dialog(self):
        # Display a success message
        success_dialog = MDDialog(
            title="Success",
            text="Video downloaded successfully!",
            size_hint=(0.7, 0.3),
        )
        success_dialog.open()

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        progress = (bytes_downloaded / total_size) * 100

        # Calculate download speed
        download_speed = stream.filesize / (total_size - bytes_remaining)

        # Update the progress bar
        self.progress_bar.value = progress

        # Update the speed label
        self.speed_label.text = f"Speed: {download_speed:.2f} bytes/s"

    def display_video_info(self, video_stream):
        # Display video title and size
        self.video_title_label.text = f"Video Title: {video_stream.title}"
        self.video_size_label.text = f"Video Size: {self.format_size(video_stream.filesize)}"

    def format_size(self, size_in_bytes):
        # Convert bytes to a human-readable format
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_in_bytes < 1024.0:
                break
            size_in_bytes /= 1024.0
        return "{:.2f} {}".format(size_in_bytes, unit)
        
    def show_quality_menu(self, instance_button):
        
        # Video quality options
        quality_options = ["144p", "240p", "360p","480p", "720p"]

        # Create the dropdown menu
        self.quality_menu = MDDropdownMenu(
            caller=instance_button,
            items=[
                { "text": quality,
                  "viewclass": "OneLineListItem",
                  "on_release": lambda x=quality: self.set_selected_quality(x)}
                for quality in quality_options
            ],
            width_mult=4,
        )
        # Open the dropdown menu
        self.quality_menu.open()

    def set_selected_quality(self, selected_quality):
        
        # Update the selected quality and close the dropdown menu
        self.selected_quality = selected_quality
        self.quality_menu_button.text = f"Quality: {selected_quality}"
        self.quality_menu.dismiss()

    def paste_text(self, *args):
        self.show_interstitial_ad()
        # Paste text from the clipboard into the URL input field
        clipboard_content = Clipboard.paste()
        if clipboard_content:
            self.url_input.text = clipboard_content

    def show_banner_ad(self, *args):
        self.ads = KivMob("ca-app-pub-3940256099942544~3347511713")
        self.ads.new_banner("ca-app-pub-4807505678699119/4029429670", top_pos=False)
        self.ads.request_banner()
        self.ads.show_banner()
        return MDLabel(text='Banner Ad Demo')

    def show_interstitial_ad(self, *args):
        self.ads = KivMob("ca-app-pub-3940256099942544~3347511713")
        self.ads.new_interstitial("ca-app-pub-4807505678699119/9407230507")
        self.ads.request_interstitial()
        return

    def Rewarded_Video(self,*args):
        self.ads = KivMob("ca-app-pub-3940256099942544~3347511713")
        self.ads.load_rewarded_ad("ca-app-pub-4807505678699119/1950632069")
        # Add any callback functionality to this class.
        self.ads.set_rewarded_ad_listener(RewardedListenerInterface())
        return 

    def show_error_dialog(self, error_message):
        # Display an error message
        error_dialog = MDDialog(
            title="Error",
            text=f"An error occurred: {error_message}",
            size_hint=(0.7, 0.3),
        )
        error_dialog.open()

if __name__ == "__main__":
    VideoDownloaderApp().run()
