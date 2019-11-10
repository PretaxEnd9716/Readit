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
    window.resizable(False, False)


    label = Label(window, text='Enter a reddit link: ').grid(row=0)
    url_entry = Entry(window)
    url_entry.grid(row=0, column=1)
    text = "hi"


    enter = Button(window, text="Read It!", width=10, command=lambda : process_info(url_entry)).grid(row=1, column=1)

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
