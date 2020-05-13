import os
import io
import re
import sys
import csv
import glob
import json
import time
import shutil
import random
from datetime import date
from sys import platform
from subprocess import call    
import docopt
import boto3
import matplotlib
import kivy
from kivy.config import Config 
Config.set('graphics', 'resizable', False) 
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
import kivy.core.window as window
from kivy.base import EventLoop
from kivy.cache import Cache
import matplotlib.pyplot as plt
import dateutil.parser as dparser
import matplotlib.dates as mdates
from matplotlib.pyplot import figure
from kivy.uix.spinner import Spinner

    
Window.size = (497, 157)
message = 'Drop Images or Folders Here'
root = os.getcwd()
destPath = root
dropPath = ''
NumberOfItems = 0
unsure = False
getbetter = False
interface = True
stats = ''
destination = (os.path.expanduser("~/Desktop/Organized"))
UnsortedImages = (root + '/UnsortedImages')
source = os.getcwd()
directory = (os.path.expanduser("~/Desktop/Organized/"))
times = []
times24 = []
x1 = []
y1 = []


#Resets Cache to Avoid Errors
def reset():
    
    if not EventLoop.event_listeners:
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}


def removeEmptyFolders(destination, removeRoot=True):
    if not os.path.isdir(destination):
        return
    files = os.listdir(destination)
    if len(files):
        for f in files:
            fullpath = os.path.join(destination, f)
            if os.path.isdir(fullpath):
                removeEmptyFolders(fullpath)	
    files = os.listdir(destination)
    if len(files) == 0:
        os.rmdir(destination)


def RecognizeText():
    times = []
    times24 = []
    x1 = []
    y1 = []
    with open('credentials.csv', 'r') as creds:
            next(creds)
            reader = csv.reader(creds)
            for line in reader:
                access_key_id = line[2]
                secret_access_key = line[3]
                aws_region_name = 'us-east-1'
                client = boto3.client('rekognition', aws_access_key_id = access_key_id,
                 aws_secret_access_key = secret_access_key, region_name = aws_region_name)
    
    for filename in glob.glob(directory):
        cwd = os.getcwd()
        source_image = open(filename, 'rb')
        source_bytes = source_image.read()
        response = client.detect_text(Image={'Bytes': source_bytes})
        thisdict = response.get('TextDetections')
                    
        rightsplitWord = "', 'Type'"
        leftSplitWord = "MOLLTRIE"
        addString = ":00"
        res1 = str(response).partition(rightsplitWord)[0]
        res2 = res1[-8:]
        ampm = ''
        
        if 'am' in res2:
            ampm = 'AM'
            res = res2[ : 5] + addString + ampm
            times.append(res)
            print(res2)
        if 'pm' in res2:
            ampm = 'PM'
            res = res2[ : 5] + addString + ampm
            times.append(res)
            print(res2)
            
            
    def convert24(str1): 
        if str1[-2:] == "AM" and str1[:2] == "12": 
            return "00" + str1[2:-2]
        elif str1[-2:] == "AM": 
            return str1[:-2]
        elif str1[-2:] == "PM" and str1[:2] == "12": 
            return str1[:-2]
        else: 
            return str(int(str1[:2]) + 12) + str1[2:8] 
    
    for item in times:
        times24.append(convert24(item))
    
    
    def getHour(str1):
        return str1[:-6]


    hours = []
    hour1 = 0
    hour2 = 0
    hour3 = 0
    hour4 = 0
    hour5 = 0
    hour6 = 0
    hour7 = 0
    hour8 = 0
    hour9 = 0
    hour10 = 0
    hour11 = 0
    hour12 = 0#12pm
    hour13 = 0
    hour14 = 0
    hour15 = 0
    hour16 = 0
    hour17 = 0
    hour18 = 0
    hour19 = 0
    hour20 = 0
    hour21 = 0#9pm
    hour22 = 0
    hour23 = 0
    hour24 = 0#12am
    
    for item in times24:
        hours.append(getHour(item))

    for item in hours:
        if '01' in item:
            hour1 = hour1 + 1
            x1.append('1:00am')
            y1.append(hour1)
        if '02' in item:
            hour2 = hour2 + 1
            x1.append('2:00am')
            y1.append(hour2)
        if '03' in item:
            hour3 = hour3 + 1
            x1.append('3:00am')
            y1.append(hour3)
        if '04' in item:
            hour4 = hour4 + 1
            x1.append('4:00am')
            y1.append(hour4)
        if '05' in item:
            hour5 = hour5 + 1
            x1.append('5:00am')
            y1.append(hour5)
        if '06' in item:
            hour6 = hour6 + 1
            x1.append('6:00am')
            y1.append(hour6)
        if '07' in item:
            hour7 = hour7 + 1
            x1.append('7:00am')
            y1.append(hour7)
        if '08' in item:
            hour8 = hour8 + 1
            x1.append('8:00am')
            y1.append(hour8)
        if '09' in item:
            hour9 = hour9 + 1
            x1.append('9:00am')
            y1.append(hour9)
        if '10' in item:
            hour10 = hour10 + 1
            x1.append('10:00am')
            y1.append(hour10)
        if '11' in item:
            hour11 = hour11 + 1
            x1.append('11:00am')
            y1.append(hour11)
        if '12' in item:
            hour12 = hour12 + 1
            x1.append('12:00pm')
            y1.append(hour12)
        if '13' in item:
            hour13 = hour13 + 1
            x1.append('1:00pm')
            y1.append(hour13)
        if '14' in item:
            hour14 = hour14 + 1
            x1.append('2:00pm')
            y1.append(hour14)
        if '15' in item:
            hour15 = hour15 + 1
            x1.append('3:00pm')
            y1.append(hour15)
        if '16' in item:
            hour16 = hour16 + 1
            x1.append('4:00pm')
            y1.append(hour16)
        if '17' in item:
            hour17 = hour17 + 1
            x1.append('5:00pm')
            y1.append(hour17)
        if '18' in item:
            hour18 = hour18 + 1
            x1.append('6:00pm')
            y1.append(hour18)
        if '19' in item:
            hour19 = hour19 + 1
            x1.append('7:00pm')
            y1.append(hour19)
        if '20' in item:
            hour20 = hour20 + 1
            x1.append('8:00pm')
            y1.append(hour20)
        if '21' in item:
            hour21 = hour21 + 1
            x1.append('9:00pm')
            y1.append(hour21)
        if '22' in item:
            hour22 = hour22 + 1
            x1.append('10:00pm')
            y1.append(hour22)
        if '23' in item:
            hour23 = hour23 + 1
            x1.append('11:00pm')
            y1.append(hour23)
        if '00' in item:
            hour24 = hour24 + 1
            x1.append('12:00am')
            y1.append(hour24)

    try:
        plt.figure(num="GameCamAI")
        plt.rcParams["figure.figsize"] = (8,4)
        plt.bar(x1, y1, label = ("Total: "+str(legendCount)))
        plt.xlabel('Time') 
        plt.ylabel('Number of Animals') 
        plt.title('GameCamAI') 
        plt.legend() 
        plt.show()
    except IndexError:
        plt.bar(x1, y1)
        plt.xlabel('Time') 
        plt.ylabel('Number of Animals') 
        plt.title('The selected animal type is not graphable') 
        plt.show()
    
    

class Grapher(App):
    def on_stop(self):
        sys.exit()
        
        
    def build(self):
        self.title="GameCamAI"
        Window.size = (459, 100)
        box = BoxLayout()
        valuesPre = ("Hogs", "Deer", "Antelope", "Coyotes", "Squirrels",
         "Rabbits", "Skunks", "Racoons", "Opossums", "People", "Cows", "Vehicles")
        valuesPost = []
        
        for i in valuesPre:
            if os.path.exists(directory + i):
                valuesPost.append(i)
        if len(valuesPost) == 0:
            valuesPost = "Make sure the Organized folder is on your desktop"
        
        startBtn = Button(text='Start', font_size='15sp', size_hint=(.5, 1),
         background_normal='', background_color=[0,1,0,.45])
        dropDown = Spinner(text='Please Select an Animal', values=valuesPost, size_hint=(.5, None))
        box.add_widget(dropDown)
        box.add_widget(startBtn)
        startBtn.bind(on_release = self.callback)
        
        
        def show_selected_value(self, text):
            global directory
            global legendCount
            print(text)
            directory = (os.path.expanduser("~/Desktop/Organized/" + str(text) + '/*'))
            legendSpot = (os.path.expanduser("~/Desktop/Organized/" + str(text)))
            location = os.listdir(legendSpot)
            legendCount = len(location)
            print(directory)
            Window.size = (459, 100)


        dropDown.bind(on_release = self.windowSize, text=show_selected_value)
        return box
    
    
    def windowSize(self, *args):
        self.size_hint=(.5, 1)
        Window.size = (459, 325)


    def callback(self, *args):
        RecognizeText()


def Graph():
    reset()
    Grapher().run()


def GO():
    root = os.getcwd()
    with open('credentials.csv', 'r') as creds:
            next(creds)
            reader = csv.reader(creds)
            for line in reader:
                access_key_id = line[2]
                secret_access_key = line[3]
                aws_region_name = 'us-east-1'
                client = boto3.client('rekognition', aws_access_key_id = access_key_id,
                 aws_secret_access_key = secret_access_key, region_name = aws_region_name)


    def datacheck():
        if unsure == True:
            print("")
            print(filename)
            print(response)
            print("")
        else:
            pass


    def failedClassification():
        if getbetter == True:
            print("")
            print(filename)
            print(response)
            print("")
        else:
            pass


    buckpath = (os.path.expanduser("~/Desktop/Organized/Bucks"))
    doepath = (os.path.expanduser("~/Desktop/Organized/Does"))
    humanpath = (os.path.expanduser("~/Desktop/Organized/People"))
    clownpath = (os.path.expanduser("~/Desktop/Organized/Clowns"))
    deerpath = (os.path.expanduser("~/Desktop/Organized/Deer"))
    coyotepath = (os.path.expanduser("~/Desktop/Organized/Coyote"))
    blackbuckpath = (os.path.expanduser("~/Desktop/Organized/Deer"))
    cowpath = (os.path.expanduser("~/Desktop/Organized/Cows"))
    hogpath = (os.path.expanduser("~/Desktop/Organized/Hogs"))
    birdpath = (os.path.expanduser("~/Desktop/Organized/Birds"))
    squirrelpath = (os.path.expanduser("~/Desktop/Organized/Squirrels"))
    rabbitpath = (os.path.expanduser("~/Desktop/Organized/Rabbits"))
    skunkpath = (os.path.expanduser("~/Desktop/Organized/Skunks"))
    racoonpath = (os.path.expanduser("~/Desktop/Organized/Racoons"))
    opossumpath = (os.path.expanduser("~/Desktop/Organized/Opossums"))
    animalpath = (os.path.expanduser("~/Desktop/Organized/Miscellaneous Animals"))
    vehiclepath = (os.path.expanduser("~/Desktop/Organized/Vehicles"))
    ImIgnorantPath = (os.path.expanduser("~/Desktop/Organized/Unknown"))

    buckcounter = int(0)
    doecounter = int (0)
    humancounter = int(0)
    clowncounter = int(0)
    deercounter = int(0)
    blackbuckcounter = int(0)
    hogcounter = int(0)
    coyotecounter = int(0)
    cowcounter = int(0)
    birdcounter = int(0)
    squirrelcounter = int(0)
    rabbitcounter = int(0)
    skunkcounter = int(0)
    racooncounter = int(0)
    opossumcounter = int(0)
    animalcounter = int(0)
    vehiclecounter = int(0)
    unknowncounter = int(0)
    totalcounter = int(0)

    supportedAnimals = str("Hog" "Deer" "Antelope" "Coyote" "Squirrel"
     "Rabbit" "Skunk" "Racoon" "Opossum" "Person" "Cattle" "Cow" "Vehicle")
    notdeer = str("Hog" "Pig")

    source = os.getcwd()
    directory = source + "/UnsortedImages/*"
    image_list = []
    start = time.time()
    for filename in glob.glob(directory):
        cwd = os.getcwd()
        img = open(filename)
        image_list.append(img)
        img.close()
        for image in image_list:
            try:
                with open (filename, 'rb') as source_image:
                    source_bytes = source_image.read()
                    response = client.detect_labels(Image={'Bytes': source_bytes}, MaxLabels=150)
                    thisdict = json.dumps(response)
                if "Deer" in thisdict:
                    if "Antelope" in thisdict:
                        if "Antlers" in thisdict:
                            try:
                                if not os.path.exists(deerpath):
                                    os.mkdir(deerpath)
                                shutil.copy(filename, deerpath)
                                os.remove(filename)
                                datacheck()
                                deercounter = int(deercounter + 1)
                                print ("Saved Deer Image:", deercounter)
                            except FileNotFoundError:
                                pass
                        else:
                            pass
                if "Deer" in thisdict:
                    try:
                        if not os.path.exists(deerpath):
                            os.mkdir(deerpath)
                        shutil.copy(filename, deerpath)
                        os.remove(filename)
                        datacheck()
                        deercounter = int(deercounter + 1)
                        print ("Saved Deer Image:", deercounter)
                    except FileNotFoundError:
                        pass

                if "Hog" in thisdict:
                    try:
                        if not os.path.exists(hogpath):
                            os.mkdir(hogpath)
                        shutil.copy(filename, hogpath)
                        os.remove(filename)
                        datacheck()
                        hogcounter = int(hogcounter + 1)
                        print("Saved Hog Image:" , hogcounter)
                    except FileNotFoundError:
                        pass

                if "Coyote" in thisdict:
                    try:
                        if not os.path.exists(coyotepath):
                            os.mkdir(coyotepath)
                        shutil.copy(filename, coyotepath)
                        datacheck()
                        os.remove(filename)
                        coyotecounter = coyotecounter + 1
                        print ("Saved Coyote Image:", coyotecounter)
                    except FileNotFoundError:
                        pass

                if "Vehicle" in thisdict:
                    try:
                        if not os.path.exists(vehiclepath):
                            os.mkdir(vehiclepath)
                        shutil.copy(filename, vehiclepath)
                        datacheck()
                        os.remove(filename)
                        vehiclecounter = int(vehiclecounter + 1)
                        print("Saved Vehicle Image:" , vehiclecounter)
                    except FileNotFoundError:
                        pass
                if "Truck" in thisdict:
                    try:
                        if not os.path.exists(vehiclepath):
                            os.mkdir(vehiclepath)
                        shutil.copy(filename, vehiclepath)
                        datacheck()
                        os.remove(filename)
                        vehiclecounter = int(vehiclecounter + 1)
                        print("Saved Vehicle Image:" , vehiclecounter)
                    except FileNotFoundError:
                        pass
                if "Bulldozer" in thisdict:
                    try:
                        if not os.path.exists(vehiclepath):
                            os.mkdir(vehiclepath)
                        shutil.copy(filename, vehiclepath)
                        datacheck()
                        os.remove(filename)
                        vehiclecounter = int(vehiclecounter + 1)
                        print("Saved Vehicle Image:" , vehiclecounter)
                    except FileNotFoundError:
                        pass

                if "Bull" in thisdict:
                    try:
                        if not os.path.exists(cowpath):
                            os.mkdir(cowpath)
                        shutil.copy(filename, cowpath)
                        os.remove(filename)
                        cowcounter = int(cowcounter + 1)
                        datacheck()
                        print ("Saved Cow Image:", cowcounter)
                    except FileNotFoundError:
                        pass
                if "Cattle" in thisdict:
                    try:
                        if not os.path.exists(cowpath):
                            os.mkdir(cowpath)
                        shutil.copy(filename, cowpath)
                        os.remove(filename)
                        cowcounter = int(cowcounter + 1)
                        datacheck()
                        print ("Saved Cow Image:", cowcounter)
                    except FileNotFoundError:
                        pass
                if "Angus" in thisdict:
                    try:
                        if not os.path.exists(cowpath):
                            os.mkdir(cowpath)
                        shutil.copy(filename, cowpath)
                        os.remove(filename)
                        cowcounter = int(cowcounter + 1)
                        datacheck()
                        print ("Saved Cow Image:", cowcounter)
                    except FileNotFoundError:
                        pass
                if "Buffalo" in thisdict:
                    try:
                        if not os.path.exists(cowpath):
                            os.mkdir(cowpath)
                        shutil.copy(filename, cowpath)
                        os.remove(filename)
                        cowcounter = int(cowcounter + 1)
                        datacheck()
                        print ("Saved Cow Image:", cowcounter)
                    except FileNotFoundError:
                        pass
                if "Cow" in thisdict:
                    try:
                        if not os.path.exists(cowpath):
                            os.mkdir(cowpath)
                        shutil.copy(filename, cowpath)
                        os.remove(filename)
                        cowcounter = int(cowcounter + 1)
                        datacheck()
                        print ("Saved Cow Image:", cowcounter)
                    except FileNotFoundError:
                        pass

                if "Antelope" in thisdict:
                    try:
                        if "deer" in thisdict:
                            pass
                        else:
                            if not os.path.exists(deerpath):
                                os.mkdir(deerpath)
                            shutil.copy(filename, deerpath)
                            os.remove(filename)
                            deercounter = int(deercounter + 1)
                            print("Saved Deer Image:" , deercounter)
                            datacheck()
                    except FileNotFoundError:
                        pass

                if "Bird" in thisdict:
                    try:
                        if not os.path.exists(birdpath):
                            os.mkdir(birdpath)
                        shutil.copy(filename, birdpath)
                        os.remove(filename)
                        birdcounter = int(birdcounter + 1)
                        datacheck()
                        print("Saved Bird Image:" , birdcounter)
                    except FileNotFoundError:
                        pass
                
                if "Squirrel" in thisdict:
                    try:
                        if not os.path.exists(squirrelpath):
                            os.mkdir(squirrelpath)
                        shutil.copy(filename, squirrelpath)
                        os.remove(filename)
                        squirrelcounter = int(squirrelcounter + 1)
                        datacheck()
                        print("Saved Squirrel Image:" , squirrelcounter)
                    except FileNotFoundError:
                        pass
                        
                if "Skunk" in thisdict:
                    try:
                        if not os.path.exists(skunkpath):
                            os.mkdir(skunkpath)
                        shutil.copy(filename, skunkpath)
                        os.remove(filename)
                        skunkcounter = int(skunkcounter + 1)
                        datacheck()
                        print("Saved Skunk Image:" , skunkcounter)
                    except FileNotFoundError:
                        pass
                        
                if "Racoon" in thisdict:
                    try:
                        if not os.path.exists(racoonpath):
                            os.mkdir(racoonpath)
                        shutil.copy(filename, racoonpath)
                        os.remove(filename)
                        racooncounter = int(racooncounter + 1)
                        datacheck()
                        print("Saved Racoon Image:" , racooncounter)
                    except FileNotFoundError:
                        pass
                        
                if "Oppossum" in thisdict:
                    try:
                        if not os.path.exists(opossumpath):
                            os.mkdir(opposumpath)
                        shutil.copy(filename, opossumpath)
                        os.remove(filename)
                        opossumcounter = int(opossumcounter + 1)
                        datacheck()
                        print("Saved Opposum Image:" , opossumcounter)
                    except FileNotFoundError:
                        pass
                if "Possum" in thisdict:
                    try:
                        if not os.path.exists(opossumpath):
                            os.mkdir(opossumpath)
                        shutil.copy(filename, opossumpath)
                        os.remove(filename)
                        opossumcounter = int(opossumcounter + 1)
                        datacheck()
                        print("Saved Opposum Image:" , opossumcounter)
                    except FileNotFoundError:
                        pass

                if "Rabbit" in thisdict:
                    try:
                        if not os.path.exists(rabbitpath):
                            os.mkdir(rabbitpath)
                        shutil.copy(filename, rabbitpath)
                        os.remove(filename)
                        rabbitcounter = int(rabbitcounter + 1)
                        datacheck()
                        print("Saved Rabbit Image:" , rabbitcounter)
                    except FileNotFoundError:
                        pass
                if "Bunny" in thisdict:
                    try:
                        if not os.path.exists(rabbitpath):
                            os.mkdir(rabbitpath)
                        shutil.copy(filename, rabbitpath)
                        os.remove(filename)
                        rabbitcounter = int(rabbitcounter + 1)
                        datacheck()
                        print("Saved Rabbit Image:" , rabbitcounter)
                    except FileNotFoundError:
                        pass
                
                if "Person" in thisdict:
                    try:
                        if not os.path.exists(humanpath):
                            os.mkdir(humanpath)
                        shutil.copy(filename, humanpath)
                        os.remove(filename)
                        humancounter = int(humancounter + 1)
                        datacheck()
                        print("Saved Person Image:" , humancounter)
                    except FileNotFoundError:
                        pass
                if "Hiking" in thisdict:
                    try:
                        if not os.path.exists(humanpath):
                            os.mkdir(humanpath)
                        shutil.copy(filename, humanpath)
                        os.remove(filename)
                        humancounter = int(humancounter + 1)
                        datacheck()
                        print("Saved Person Image:" , humancounter)
                    except FileNotFoundError:
                        pass

                ##UNKNOWN ANIMALS##
                if supportedAnimals not in thisdict:
                    if "Animal" in thisdict:
                        try:
                            if not os.path.exists(animalpath):
                                os.mkdir(animalpath)
                            shutil.copy(filename, animalpath)
                            os.remove(filename)
                            animalcounter = int(animalcounter + 1)
                            datacheck()
                            failedClassification()
                            print ("Saved Animal Image:", animalcounter)
                        except FileNotFoundError:
                            break
                    if "Mammal" in thisdict:
                        try:
                            if not os.path.exists(animalpath):
                                os.mkdir(animalpath)
                            shutil.copy(filename, animalpath)
                            os.remove(filename)
                            animalcounter = int(animalcounter + 1)
                            datacheck()
                            print ("Saved Animal Image:", animalcounter)
                        except FileNotFoundError:
                            break

                if supportedAnimals not in thisdict:
                    try:
                        if not os.path.exists(ImIgnorantPath):
                            os.mkdir(ImIgnorantPath)
                        shutil.copy(filename, ImIgnorantPath)
                        os.remove(filename)
                        unknowncounter = int(unknowncounter + 1)
                        datacheck()
                        failedClassification()
                        print ("Saved Unknown Image:", unknowncounter)
                    except FileNotFoundError:
                        pass
            except FileNotFoundError:
                pass

    totalcounter = (deercounter + blackbuckcounter + hogcounter + coyotecounter +
     cowcounter + birdcounter + animalcounter + vehiclecounter + humancounter + 
      unknowncounter + clowncounter + squirrelcounter + rabbitcounter +
       skunkcounter + racooncounter + opossumcounter)

    #CONSOLE OUTPUT
    if interface == False:
        if totalcounter == 0:
            print ("No images to sort.")
        else:
            print("")
            print("Types Captured:")
            if doecounter != 0:
                print("Does:", doecounter)
            if buckcounter != 0:
                print("Bucks:", buckcounter)
            if deercounter != 0:
                print("Deer:", deercounter)
            if blackbuckcounter != 0:
                print("Blackbuck:", blackbuckcounter)
            if hogcounter != 0:
                print("Hogs:", hogcounter)
            if coyotecounter != 0:
                print("Coyotes:", coyotecounter)
            if cowcounter != 0:
                print("Cows:", cowcounter)
            if birdcounter != 0:
                print("Birds:", birdcounter)
            if squirrelcounter != 0:
                print("Squirrels:", squirrelcounter)
            if rabbitcounter != 0:
                print("Rabbits:", rabbitcounter)
            if skunkcounter != 0:
                print("Skunks:", skunkcounter)
            if racooncounter != 0:
                print("Racoons:", racooncounter)
            if opossumcounter != 0:
                print("Opossums:", opossumcounter)
            if animalcounter != 0:
                print("Animals:", animalcounter)
            if vehiclecounter != 0:
                print("Vehicles:", vehiclecounter)
            if humancounter != 0:
                print("People:", humancounter)
            if unknowncounter != 0:
                print("Unknown:", unknowncounter)
            if clowncounter != 0:
                print("Clowns:", clowncounter)

    #INTERFACE OUTPUT
    if interface == True:
        end = time.time()
        elapsed = end - start
        elapsed = int(elapsed)
        results1 = "GameCamAI sorted " + str(totalcounter) + " images in " + str(elapsed) + " seconds"
        results = str(results1)

        deerstats = 'Deer: ' + str(deercounter)
        hogstats = 'Hogs: ' + str(hogcounter)
        coyotestats = 'Coyotes: ' + str(coyotecounter)
        vehiclestats = 'Vehicles: ' + str(vehiclecounter)
        peoplestats = 'People: ' + str(humancounter)
        cowstats = "Cows: " + str(cowcounter)
        birdstats = "Birds: " + str(birdcounter)
        squirrelstats = "Squirrels: " + str(squirrelcounter)
        rabbitstats = "Rabbits: " + str(rabbitcounter)
        skunkstats = "Skunks: " + str(skunkcounter)
        racoonstats = "Racoons: " + str(racooncounter)
        opossumstats = "Opossums: " + str(opossumcounter)
        miscstats = "Miscellaneous: " + str(animalcounter)
        deerstats = (str(deerstats))
        hogstats = (str(hogstats))
        coyotestats = (str(coyotestats))
        vehiclestats = (str(vehiclestats))
        peoplestats = (str(peoplestats))
        cowstats = (str(cowstats))
        birdstats = (str(birdstats))
        squirrelstats = (str(squirrelstats))
        rabbitstats = (str(rabbitstats))
        skunkstats = (str(skunkstats))
        racoonstats = (str(racoonstats))
        opossumstats = (str(opossumstats))
        miscstats = (str(miscstats))

        #Results UI
        class GameCamAI(App):
            Window.size = (477, 459)
            #def on_stop(self):
                #sys.exit()

            def build(self):
                grid = GridLayout(cols=1)
                resultslbl = Label(text=results, font_size='20sp',halign="left", valign="middle")
                newlinelbl1 = Label(text=' ', font_size='15sp')
                newlinelbl2 = Label(text=' ', font_size='15sp')
                newlinelbl3 = Label(text=' ', font_size='15sp')
                newlinelbl4 = Label(text=' ', font_size='100sp')

                nosortlbl = Label(text='No images to sort...', font_size='18sp')

                messagelbl = Label(text='Types Captured: ', font_size='18sp')
                deerlbl = Label(text=deerstats, font_size='15sp')
                hoglbl = Label(text=hogstats, font_size='15sp')
                coyotelbl = Label(text=coyotestats, font_size='15sp')
                cowlbl = Label(text=cowstats, font_size='15sp')
                birdlbl = Label(text=birdstats, font_size='15sp')
                squirrellbl = Label(text=squirrelstats, font_size='15sp')
                rabbitlbl = Label(text=rabbitstats, font_size='15sp')
                skunklbl = Label(text=skunkstats, font_size='15sp')
                racoonlbl = Label(text=racoonstats, font_size='15sp')
                opossumlbl = Label(text=opossumstats, font_size='15sp')
                misclbl = Label(text=miscstats, font_size='15sp')
                vehiclelbl = Label(text=vehiclestats, font_size='15sp')
                peoplelbl = Label(text=peoplestats, font_size='15sp')
                graphBtn = Button(text='Graph Activity Times (Moulltrie Only)',
                font_size='14sp', size_hint=(.5, 1.9), background_normal='', background_color=[0,1,0,.45])
                graphBtn.bind(on_release = self.callback)
                
                if totalcounter == 0:
                    grid.add_widget(nosortlbl)
                    Window.size = (497, 157)
                    return grid

                if totalcounter != 0:
                    grid.add_widget(newlinelbl1)
                    grid.add_widget(resultslbl)
                    grid.add_widget(newlinelbl2)
                    grid.add_widget(messagelbl)
                    grid.add_widget(newlinelbl4)
                if deercounter != 0:
                    grid.add_widget(deerlbl)
                if hogcounter != 0:
                    grid.add_widget(hoglbl)
                if coyotecounter != 0:
                    grid.add_widget(coyotelbl)
                if birdcounter != 0:
                    grid.add_widget(birdlbl)
                if squirrelcounter != 0:
                    grid.add_widget(squirrellbl)
                if rabbitcounter != 0:
                    grid.add_widget(rabbitlbl)
                if skunkcounter != 0:
                    grid.add_widget(skunklbl)
                if racooncounter != 0:
                    grid.add_widget(racoonlbl)
                if opossumcounter != 0:
                    grid.add_widget(opossumlbl)
                if animalcounter != 0:
                    grid.add_widget(misclbl)
                if cowcounter != 0:
                    grid.add_widget(cowlbl)
                if vehiclecounter != 0:
                    grid.add_widget(vehiclelbl)
                if humancounter != 0:
                    grid.add_widget(peoplelbl)
                grid.add_widget(newlinelbl3)
                grid.add_widget(graphBtn)
                removeEmptyFolders(destination)
                return grid
                
        
            def callback(self, *args):
                App.get_running_app().stop()
                Graph()


        GameCamAI().run()


#Logic for Drag & Drop
class DropFile(Button):
    def __init__(self, **kwargs):
        super(DropFile, self).__init__(**kwargs)
        app = App.get_running_app()
        app.drops.append(self.on_dropfile)


    def on_dropfile(self, widget, filename):
        if self.collide_point(*Window.mouse_pos):
            global NumberOfItems
            global dropPath
            dropPath = filename.decode('utf-8')
            root = os.getcwd()
            destPath = (root + "/UnsortedImages")

            if os.path.isdir(str(dropPath)):
                dropPath1 = dropPath + '/*'
                dropPath = (glob.glob(str(dropPath1)))
                for file in dropPath:
                    NumberOfItems += 1
                    filename = (str(destPath) + "/Image " + str(NumberOfItems) + ".JPG")
                    shutil.copy(file, filename)

            else:
                dropPath = dropPath.splitlines()
                for i in dropPath:
                    NumberOfItems += 1
                    filename = (str(destPath) + "/Image " + str(NumberOfItems) + ".JPG")
                    shutil.copy(i, filename)

            while NumberOfItems == len(dropPath):
                App.get_running_app().stop()
                GameCamAI().run()


#Drag & Drop Screen
class GameCamBot(App):

    def build(self):
        self.title = "GameCamAI"
        self.drops = []
        Window.bind(on_dropfile=self.handledrops)
        box = BoxLayout()
        dropzone = DropFile(text=(message), font_size='15sp', size_hint=(.8, 1),
         background_normal='', background_color=[0,0,0,1])
        box.add_widget(dropzone)
        return box


    def handledrops(self, *args):
        for func in self.drops:
            func(*args)


#Start Button Screen
class GameCamAI(App):
    
    def build(self):
        box = BoxLayout()
        startBtn = Button(text='Start', font_size='15sp', size_hint=(.2, 1),
         background_normal='', background_color=[0,1,0,.45])
        box.add_widget(startBtn)
        startBtn.bind(on_release = self.callback)
        return box


    def callback(self, *args):
        try:
            os.mkdir(destination)
            print ("Organized Folder Created!")
        except FileExistsError:
            pass
        if platform == "darwin":
            call(["open", destination])
        if platform == "win32":
            os.startfile(destination)
        App.get_running_app().stop()
        GO()


##Clears 'Unsorted Images' Folder on every run
for filename in os.listdir(UnsortedImages):
    file_path = os.path.join(UnsortedImages, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except:
        pass



dsFile = ".DS_Store"
destination = (os.path.expanduser("~/Desktop/Organized"))
try:
    os.mkdir(destination)
    print ("Organized Folder Created!")
    print("")
except:
    pass



storage = (os.path.expanduser("~/Desktop/Storage"))
storagePoo = (storage+"/"+dsFile)
organizedPoo = (destination+"/"+dsFile)


def createtodayPath():
    if os.path.isfile(storagePoo):
        os.remove(storagePoo)
    today = date.today()
    today = today.strftime("%b-%d-%Y")
    endNumberPre = os.listdir(storage)
    endNumber = (len(endNumberPre) + 1)
    todayPath = (storage + "/" + str(today) + "-" + str(endNumber))
    todayPath = str(todayPath)
    os.mkdir(todayPath)
    if os.path.isdir(destination) and os.path.isdir(todayPath) :
        # Iterate over all the files in source directory
        for filePath in glob.glob(destination + '/*'):
            shutil.move(filePath, todayPath);
            
            
emptyCheck = os.listdir(destination)
if len(emptyCheck) != 0:
    print(len(emptyCheck))
    if not os.path.isdir(storage):
        os.mkdir(storage)
    createtodayPath()

else:
    print("Organized folder empty")
    

    







def main():
    reset()
    GameCamBot().run()
    
    
if __name__ == '__main__':
    main()