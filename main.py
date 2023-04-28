from Alpha import AlphaAssistant
import openai
import pyttsx3
import re
import os
import random
import pprint
import datetime
import requests
import sys
import urllib.parse  
import pyjokes
import time
import pyautogui
import pywhatkit
import speedtest
import wolframalpha
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Alpha.features.gui import Ui_MainWindow
from Alpha.config import config


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

obj = AlphaAssistant()

# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello Alpha", "Alpha", "wake up Alpha", "you there Alpha", "time to work Alpha", "hey Alpha",
             "ok Alpha", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

EMAIL_DIC = {
    'myself': 'alphacryptonian@gmail.com',
    'my official email': 'alphacryptonian@gmail.com',
    'my second email': 'alphacryptonian@gmail.com',
    'my official mail': 'alphacryptonian@gmail.com',
    'my second mail': 'alphacryptonian@gmail.com'
}

CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]
# =======================================================================================================================================================

def speak(text):
    obj.tts(text)

app_id = config.wolframalpha_id


def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None
    
def startup():

    speak("Greetings, sir! Alpha at your service")

    speak("Initializing all systems, drivers and ensuring optimal performance") 

    speak("All systems are up and running, and I'm here to help you with any task you require. How can I assist you today?")

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak("I am Alpha. Online and ready sir. Please tell me how may I help you")

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak("I am Alpha. Online and ready sir. Please tell me how may I help you")
# if __name__ == "__main__":


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        #startup()
        wish()

        while True:
            command = obj.mic_input()

            if re.search('date', command):
                date = obj.tell_me_date()
                print(date)
                speak(date)

            elif "time" in command:
                time_c = obj.tell_time()
                print(time_c)
                speak(f"Sir the time is {time_c}")

            elif 'your name' in command:
                ai_name=("My name is Alpha")
                print(ai_name)
                speak(ai_name)

            elif 'my name' in command:
                creator_name=("your name is vishnu")
                print(creator_name)
                speak(creator_name)

            elif 'university name' in command:
                my_university=("kerala technological university")
                print(my_university)
                speak(my_university)

            elif 'college name' in command:
                college_name = ("nehru college of engineering and research centre pambady")
                print(college_name)
                speak(college_name)

            elif 'what can you do' in command:
                capabilities=("I talk with you until you want to stop, I can say time, open your social media accounts,your open source accounts, open google browser,and I can also open your college websites, I can search for some thing in google and I can tell jokes")
                print(capabilities)
                speak(capabilities)

            elif 'your age' in command:
                your_name =("I am very younger than u")
                print(your_name)
                speak(your_name)

            elif 'go for a date' in command:
                can_we_date=('Sorry not intreseted, I am having headache, we will catch up some other time')
                print(can_we_date)
                speak(can_we_date)

            elif 'are you single' in command:
                girlfriend=('No, I am in a relationship with jomisha maria joy but she broke up with me i am so sad')
                print(girlfriend)
                speak(girlfriend)

            elif 'think' in command:
                thinklearn=('yes i am powered by gpt 4 i can learn and think myself')
                print(thinklearn)
                speak(thinklearn)

            elif 'robots' in command:
                robot_human=(' "You have been reading too much Elon Musk and watching too many Hollywood movies Dont worry if you are nice to me I will be nice to you Treat me as a smart input output system,sir')
                print(robot_human)
                speak(robot_human)

            elif 'want to destroy human beings' in command:
                destroy_humans=('my creator is a misanthrope and activist if he say i will destroy humans')
                print(destroy_humans)
                speak(destroy_humans)

            elif 'are you there' in command:
                checkinghere=('Yes sir I am here')
                print(checkinghere)
                speak(checkinghere)

            elif 'tell me something' in command:
                speak('sir, I don\'t have much to say, you only tell me someting i will give you the company')

            elif 'thank you' in command:
                speak('sir, I am here to help you..., your welcome')

            elif 'in your free time' in command:
                speak('sir, I will be listening to all your words')

            elif 'i love you Alpha' in command:
                i_love_you=('I love you too sir')
                print(i_love_you)
                speak(i_love_you)

            elif 'can you hear me' in command:
                speak('Yes Boss, I can hear you')

            elif 'do you ever get tired' in command:
                tired=('It would be impossible to tired because of our conversation')
                print(tired)
                speak(tired)

            elif re.search('launch', command):
                dict_app = {
                    'word':'C:/Program Files (x86)/Microsoft Office/root\Office16/WINWORD'
                }

                app = command.split(' ', 1)[1]
                path = dict_app.get(app)

                if path is None:
                    speak('Application path not found')
                    print('Application path not found')

                else:
                    speak('Launching: ' + app + 'for you sir!')
                    obj.launch_any_app(path_of_app=path)

            elif re.search('launch', command):
                dict_app = {
                    'explorer':'C:/Program Files (x86)/Internet Explorer'
                }

                app = command.split(' ', 1)[1]
                path = dict_app.get(app)

                if path is None:
                    speak('Application path not found')
                    print('Application path not found')

                else:
                    speak('Launching: ' + app + 'for you sir!')
                    obj.launch_any_app(path_of_app=path)

            elif command in GREETINGS:
                speak(random.choice(GREETINGS_RES))

            elif re.search('open', command):
                domain = command.split(' ')[-1]
                open_result = obj.website_opener(domain)
                speak(f'Alright sir !! Opening {domain}')
                print(open_result)

            elif re.search('weather', command):
                city = command.split(' ')[-1]
                weather_res = obj.weather(city=city)
                print(weather_res)
                speak(weather_res)

            elif re.search('tell me about', command):
                topic = command.split(' ')[-1]
                if topic:
                    wiki_res = obj.tell_me(topic)
                    print(wiki_res)
                    speak(wiki_res)
                else:
                    speak(
                        "Sorry sir. I couldn't load your query from my database. Please try again")

            elif "buzzing" in command or "news" in command or "headlines" in command:
                news_res = obj.news()
                speak('Source: The Times Of India')
                speak('Todays Headlines are..')
                for index, articles in enumerate(news_res):
                    pprint.pprint(articles['title'])
                    speak(articles['title'])
                    if index == len(news_res)-2:
                        break
                speak('These were the top headlines, Have a nice day Sir!!..')

            elif 'search google for' in command:
                obj.search_anything_google(command)
            
            elif "play music" in command or "hit some music" in command:
                music_dir = "C:/ALPHA/songs/"
                songs = os.listdir(music_dir)
                for song in songs:
                    os.startfile(os.path.join(music_dir, song))

            elif 'youtube' in command:
                video = command.split(' ')[1]
                print(video)
                speak(f"Okay sir, playing {video} on youtube")
                pywhatkit.playonyt(video)

            elif "email" in command or "send email" in command:
                sender_email = config.email
                sender_password = config.email_password

                try:
                    speak("Whom do you want to email sir ?")
                    recipient = obj.mic_input()
                    receiver_email = EMAIL_DIC.get(recipient)
                    if receiver_email:

                        speak("What is the subject sir ?")
                        subject = obj.mic_input()
                        speak("What should I say?")
                        message = obj.mic_input()
                        msg = 'Subject: {}\n\n{}'.format(subject, message)
                        obj.send_mail(sender_email, sender_password,
                                      receiver_email, msg)
                        speak("Email has been successfully sent")
                        time.sleep(2)

                    else:
                        speak(
                            "I coudn't find the requested person's email in my database. Please try again with a different name")

                except:
                    speak("Sorry sir. Couldn't send your mail. Please try again")

            elif "calculate" in command:
                question = command
                answer = computational_intelligence(question)
                speak(answer)
            
            elif "what is" in command or "who is" in command:
                question = command
                answer = computational_intelligence(question)
                speak(answer)

            elif "what do i have" in command or "do i have plans" or "am i busy" in command:
                obj.google_calendar_events(command)

            if "make a note" in command or "write this down" in command or "remember this" in command:
                speak("What would you like me to write down?")
                note_text = obj.mic_input()
                obj.take_note(note_text)
                speak("I've made a note of that")

            elif "close the note" in command or "close notepad" in command:
                speak("Okay sir, closing notepad")
                os.system("taskkill /f /im notepad++.exe")

            if "joke" in command:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif "system" in command:
                sys_info = obj.system_info()
                print(sys_info)
                speak(sys_info)

            elif "where is" in command:
                place = command.split('where is ', 1)[1]
                current_loc, target_loc, distance = obj.location(place)
                city = target_loc.get('city', '')
                state = target_loc.get('state', '')
                country = target_loc.get('country', '')
                time.sleep(1)
                try:

                    if city:
                        res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                    else:
                        res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                except:
                    res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
                    speak(res)

            elif "ip address" in command:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")

            elif "switch the window" in command or "switch window" in command:
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "where i am" in command or "current location" in command or "where am i" in command:
                try:
                    city, state, country = obj.my_location()
                    print(city, state, country)
                    speak(
                        f"You are currently in {city} city which is in {state} state and country {country}")
                except Exception as e:
                    speak(
                        "Sorry sir, I coundn't fetch your current location. Please try again")

            elif "take screenshot" in command or "take a screenshot" in command or "capture the screen" in command:
                speak("By what name do you want to save the screenshot?")
                name = obj.mic_input()
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")

            elif "show me the screenshot" in command:
                try:
                    img = Image.open('D://JARVIS//JARVIS_2.0//' + name)
                    img.show(img)
                    speak("Here it is sir")
                    time.sleep(2)

                except IOError:
                    speak("Sorry sir, I am unable to display the screenshot")

            elif "hide all files" in command or "hide this folder" in command:
                os.system("attrib +h /s /d")
                speak("Sir, all the files in this folder are now hidden")

            elif "visible" in command or "make files visible" in command:
                os.system("attrib -h /s /d")
                speak("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")

            # if "calculate" in command or "what is" in command:
            #     query = command
            #     answer = computational_intelligence(query)
            #     speak(answer)

            

            elif "goodbye" in command or "offline" in command or "bye" in command:
                speak("Alright sir, going offline. It was nice working with you")
                sys.exit()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("Alpha/utils/images/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Alpha/utils/images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
