from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp

# engine = pp.init()
#
# voices = engine.getProperty('voices')
# print(voices)
# engine.setProperty('voice', voices[1].id)
# def speak(word):
#     engine.say(word)
#     engine.runAndWait()

bot = ChatBot("Ron Obvious")
convo = [
    'hello',
    'hi there !',
    'my name is ChatterBot '
    'what is your name ?',
    'how are you ?',
    "i'm fine",
    "hey how can help you ?",
    'hey what is favarate thing in word',
    'bahut bahut abhar aapka jo mere se baat kiye.',
    'I am doing great there days',
    'thank you ',
    'In which city you live',
    'I live in lucknow',
    'In which language you talk',
    'I mostly talk in english',
    'what do you this time ? ',
    'i am doing talk to honest man ',
    'your  are honest man ',
    'who are you boy or girl ?',
    # 'bahen chode tuje pata nahi chal raha me aahi kya kar raha hoga... tu sala chutiya ho gaya he  ',
    # 'bol bahenchod kon si gali sunega ...'
]

trainer = ListTrainer(bot)
trainer.train(convo)
# # ans = bot.get_response("what is your name?")
# # print(ans)
# print("Talk to Bot")
# name = ''
# while True:
#     query = input(name + ' : ')
#     if(query == 'exit'):
#         break
#     ans = bot.get_response(query)
#     if(query == 'krishna'):
#         name = 'krishna'
#     print("bot : ", ans)

root = Tk()
root.title("CHATBOT")
root.geometry('600x650')
img = PhotoImage(file="image/images.png")
photoLabel = Label(root, image=img).pack(pady=5)


def spaces(n, str):
    temp = ''
    n = n - len(str)
    for i in range(n):
        temp = temp + ' '
    return temp + str




def ask_bot():
    query = tField.get()
    ans_from_bot = bot.get_response(query)
    q = spaces(120, query)
    msg.insert(END,  q)
    msg.insert(END, str(ans_from_bot))

    # speak(ans_from_bot)
    tField.delete(0, END)
    msg.yview(END)

frame = Frame(root)
sc = Scrollbar(frame)
msg = Listbox(frame, width=80, height=20, fg='green',  yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msg.pack(side=LEFT, fill=BOTH)
frame.pack()
sc.config(command=msg.yview)

#  textfield
tField=Entry(root, font=("Vardana", 15))
tField.pack(fill=X, pady=10)
btn = Button(root, text='Ask from Bot', font=("Vardana", 10,), command=ask_bot)
btn.pack()
# creating a function
def enter_function(event):
    btn.invoke()
# going to bind main windows with enter key.....
root.bind('<Return>', enter_function)
root.mainloop()
