from tkinter import *
from Backend import *

def button_pressed(text):
    print(text)

def process_info(url):
    try:
        link = url.get()
        title, body, author = get_data(link, create_reddit_object())
        comments = get_comments(link)
        combined_str = master_string(title, body, author, comments)
        print(combined_str)
        tts = gTTS(text=combined_str, lang='en')
        tts.save("test.mp3")
        playsound("test.mp3")
    except:
        print("ERROR: Invalid Link!")

def main():
    #fontType = font=("Times New Roman", 12, "bold")
    window = Tk()
    window.title("Readit beta v0.1")
    window.geometry('600x400')
    mycolor = '#fa8366'
    window.configure(background=mycolor)
    window.resizable(False, False)

    secondlabel = Label(window, text='Readit beta v0.1', bg=mycolor).grid(row=1)
    window.grid_rowconfigure(3, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(3, weight=1)

    label = Label(window, text='Enter a reddit link: ', bg=mycolor).grid(row=1)

    url_entry = Entry(window, width=50)
    url_entry.grid(row=1, column=2)
    text = "hi"


    enter = Button(window, text="Read It!", width=10, command=lambda : process_info(url_entry)).grid(row=2, column=2)

    window.mainloop()





    '''link = input("Enter in a Reddit post link: ")
    title, body, author = get_data(link, create_reddit_object())
    comments = get_comments(link)
    combined_str = master_string(title, body, author, comments)
    print(combined_str)
    tts = gTTS(text=combined_str, lang='en')
    tts.save("test.mp3")
    playsound("test.mp3")


    #say_post(combined_str)

    #print(get_data(link, create_reddit_object()))
    #print(get_comments(link))
    
'''
main()


