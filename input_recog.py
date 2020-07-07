from nltk.chat.util import Chat
from datetime import *
import fdate
import wikipediaapi
import text_to_speech as speech
from gtts import gTTS
import playsound
import os

pairs = {
               "hi": " hey there",
               "hey": "hola",
               "is this fun": "this is indeed fun",
               "where do you live": "in legion but soon i'll move to cloud",
               "who created you": "the three musketeers",
               "what is your name": "definately not siri",
        }

def dt():
    today=date.today()
    return today.strftime("todays date is %B %d %Y")

def tim():
    now = datetime.now()
    if now.hour >= 12:
        meridian = 'pm'
    else:
        meridian = 'am'
    return ' '.join([str(now.hour),str(now.minute),meridian])

def wiki():
    search=input("What do you want to search for:")
    wiki=wikipediaapi.Wikipedia('en')
    page_py=wiki.page(search)
    if page_py.exists():
        text=page_py.summary
        text=text.replace('.','\n ')
        lines=[]
        for l in text.splitlines():
            lines.append(l)
        
        tlines=[]

        for i in range(5):
            tlines.append(lines[i])
        return '.'.join(tlines)
    else:
        return "i am not sure what you want to search for"
    
    
def reply(inp):

    if ("what" in inp or "what's" in inp) and "date" in inp:
        return dt()
    elif ("what" in inp or "what's" in inp) and "time" in inp:
        return tim()
    elif "search" in inp and "wikipedia" in inp:
        return wiki()

    else:
        temp=[]
        for x,y in pairs.items():
            temp=list(x.split(' '))
            if temp == inp:
                return y
    




inp='a'
num=1
while inp != 'quit':
    inp=input("How can I help you?")
    inp_lis=list(inp.split(' '))
    spk=reply(inp_lis)
    if inp != 'quit':
        tts=gTTS(text = spk, lang ='en')
        file1=str("temp" + str(num) + ".mp3")
        tts.save(file1)
        playsound.playsound(file1,True)
        os.remove(f"temp{num}.mp3")
        num+=1
        
   # os.remove("temp.mp3")

    
    
    
    
        

    
