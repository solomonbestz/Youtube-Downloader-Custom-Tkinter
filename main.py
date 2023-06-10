import customtkinter as bestz
from pytube import YouTube


# Set default theme color and appearance color
bestz.set_default_color_theme('dark-blue')
bestz.set_appearance_mode('dark')


"""
Empty frames to design...not good practice 
"""



"""
Frame Function For Title and Label
"""
def title_frame():
    global app_title_frame
    app_title_frame = bestz.CTkFrame(master=root, fg_color='orange', width=600)
    app_title_frame.pack(padx=10, ipady=20, fill='both')
    title()
    link()


def title():
    app_title = bestz.CTkLabel(master=app_title_frame, text='Insert Youtube Link', font=('Helvetica', 20, 'bold'), width=50, height=20,text_color='green')
    app_title.pack(padx=10, pady=10)

def link():
    global app_link
    app_link = bestz.CTkEntry(master=app_title_frame, placeholder_text="Insert Link here...", text_color='black', placeholder_text_color='black', height=40, width=400, fg_color='white', border_width=0)
    app_link.pack(pady=10)


"""
Frame Function For Download Button
"""
def download_frame():
    global app_download_frame
    app_download_frame = bestz.CTkFrame(master=root, fg_color='green', height=200)
    app_download_frame.pack(padx=10, side='top', fill='both')
    button_click()

def button_click():
    button = bestz.CTkButton(master=app_download_frame, text='Download', command=download_video)
    button.pack(pady=20)


def download_video():
    print(app_link.get())



if __name__=='__main__':
    root = bestz.CTk()

    root.title('BYD')
    root.geometry('800x600')
    root.resizable(0, 0)
    

    # Call Functions
    title_frame()
    download_frame()
    
    root.mainloop()