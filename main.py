import customtkinter as bestz
from pytube import YouTube


# Set default theme color and appearance color
bestz.set_default_color_theme('dark-blue')
bestz.set_appearance_mode('system')


"""
Empty frames to design...not good practice 
"""
def empty_frame():
    empty = bestz.CTkFrame(master=root, width=600, height=50)
    empty.pack(fill='both')


"""
Frame Function For Title and Label
"""
def title_frame():
    global app_title_frame
    app_title_frame = bestz.CTkFrame(master=root, fg_color='#D30000', width=600)
    app_title_frame.pack(padx=10, ipady=20, fill='both')
    title()
    link()


def title():
    global app_title
    app_title = bestz.CTkLabel(master=app_title_frame, text='Bestz Youtube Downloader', font=('Helvetica', 20, 'bold'), width=50, height=20, text_color='#D9DDDC')
    app_title.pack(padx=10, pady=10)

def link():
    global youtube_link
    youtube_link = bestz.CTkEntry(master=app_title_frame, placeholder_text="Insert Link here...", text_color='black', placeholder_text_color='black', height=40, width=400, fg_color='white', border_width=0)
    youtube_link.pack(pady=10)


"""
Frame Function For Download Button
"""
def download_frame():
    global app_download_frame
    app_download_frame = bestz.CTkFrame(master=root, fg_color='#D9DDDC', height=200)
    app_download_frame.pack(padx=10, side='top', fill='both')
    download_widgets()
    button_click()

def button_click():
    button = bestz.CTkButton(master=app_download_frame, width=100, font=('Helvetica', 13, 'bold'), hover_color='red', fg_color="#D30000", text='Download', command=download_video)
    button.pack(pady=20)


def download_video():
    global downloaded
    try:
        link = youtube_link.get()
        yt_object = YouTube(link, on_progress_callback=download_progress)
        mp4_video =   yt_object.streams.get_highest_resolution()
        app_title.configure(text=yt_object.title)
        mp4_video.download()
        downloaded.configure(text='Downloaded')
    except Exception:
        downloaded.configure(text='Download Error', text_color='red')


def download_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = bytes_downloaded / total_size * 100
    prog_perc.configure(text=str(int(percentage)+ "%"))
    prog_perc.update()
    prog_bar.set(bytes_downloaded)
    prog_bar.update()

    

def download_widgets():
    global downloaded, prog_bar, prog_perc
    downloaded = bestz.CTkLabel(master=app_download_frame, text='No Downloads', font=('roboto', 12, 'bold'), width=50, text_color="black" )
    prog_perc = bestz.CTkLabel(master=app_download_frame, text="0%")
    prog_perc.pack()
    prog_bar = bestz.CTkProgressBar(master=app_download_frame, width=400, progress_color='#D30000')
    prog_bar.set(0)
    prog_bar.pack(padx=10, pady=10)
    downloaded.pack(pady=20)






if __name__=='__main__':
    root = bestz.CTk()

    root.title('BYD')
    root.iconbitmap('logo.ico')
    root.geometry('800x400')
    root.resizable(0, 0)
    

    # Call Functions
    empty_frame()
    title_frame()
    download_frame()
    
    
    root.mainloop()