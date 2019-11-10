import tkinter
import Backend

def main():
    window = tkinter.Tk()
    window.title("Readit")
    window.geometry('500x500')
    window.resizable(False, False)
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


