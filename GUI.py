from tkinter import *
from Backend import *

def button_pressed(url):
    link = url
    title, body, author = get_data(link, create_reddit_object())
    comments = get_comments(link)
    combined_str = master_string(title, body, author, comments)
    print(combined_str)
    tts = gTTS(text=combined_str, lang='en')
    tts.save("test.mp3")
    playsound("test.mp3")


def main():
    window = Tk()
    window.title("Readit")
    window.geometry('600x400')
    window.resizable(False, False)

    Label(window, text='Enter a reddit link: ').grid(row=0)
    url_entry = Entry(window)
    url_entry.grid(row=0, column=1)


    enter = Button(window, text="Read It!", width=10, command=button_pressed(url_entry.get())).grid(row=1, column=1)

    #enter.bind('<Button-1>', lambda a : button_pressed(a))



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


