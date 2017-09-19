#!/usr/bin/env python3
import speech_recognition as sr
import re as re 
import operator as op
import pyttsx
from num2words import num2words
import math
import sys



maxval_Limit=1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#############################
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            return "not number"
            sys.exit()

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current
######################################



engine = pyttsx.init()




# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
    print("Say your operator,function,number : one at a Time")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    
    audioString = r.recognize_google(audio)
    print("G : I Think You said - " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Uhh .. Couldnt understand what you said - ")
    engine.say("Uhh .. Couldnt understand what you said - ")
    engine.runAndWait()

except sr.RequestError as e:
    print("Results not available from API {}".format(e))
    engine.say("Results not available from API {}")
    exit()

audioString = audioString+" "

matchplus = re.search(r'(\w+|\d+)\s(times|log|log\sof|sectorial|pictorial|tectorial|victorial|factorial|fact\sof|Factorial|factorial\sof|\d+|plus|multiply|multiplied\sby|cross|into|in\sto|in\stwo|in\s2|\+|\*|x|X|minus|-|\/|divide|divided\sby|\^|to\sthe\spower|raised\s\w+\sthe\spower|2\sthe\spower|2\sthe\spower|raised\sto)\s(\w+|\d+|)',audioString)

operators = {'+': op.add, '-': op.sub, '*': op.mul, '/':op.truediv, 'plus': op.add, 'multiply': op.mul, 'mutliplied by': op.mul}

if matchplus:
    print("Found you", matchplus.group())
    operator = matchplus.group(2)
    number1 = re.search(r'\d+',matchplus.group(1))
    matchcase = 0
    if number1==None:
        if matchplus.group(1) == "to":
            number1 = 2
        elif matchplus.group(1) == "hundred":
            number1 = 100
        else:
            number1 = text2int(matchplus.group(1))
            if(number1 == "not number"):
                matchcase = 1            
        print ("First number is {}".format(number1)) 
    else:
        number1 = int(number1.group(0)) 
        print ("First number is {}".format(number1))
    
    if matchcase==1 :  
        number2 = re.search(r'\d+',matchplus.group(2))
        if number2==None:
            if matchplus.group(2) =="to":
                number2 = 2
            else :
                number2 = text2int(matchplus.group(2))
            print("Operand number is {}".format(number2))
        else:
            number2 = int(number2.group(0))
            print("Operand number is {}".format(number2)) 
        operator = matchplus.group(1)    
        if operator =="factorial" or operator =="fact of" or operator =="Factorial" or operator =="factorial of" or operator =="tectorial" or operator =="victorial" or operator =="pictorial" or operator =="sectorial":
            result = math.factorial(number2)
            print("operator is factorial cat -- {}".format(operator))
            print(result)
            if(result<maxval_Limit):
                wordresult = num2words(result)
                print (wordresult)
                wordbreak = re.sub(r'-',r' ',wordresult)
                engine.say(wordbreak)
                engine.runAndWait() 
            else :
                engine.say("Uhh. I don't know how to put it. The number is quite big to be converted to words, and so I can't speak it. I hope you understand. But yeah you can still read the answer from screen.")
                engine.runAndWait()
        elif operator =="log" or operator=="log of" or operator=="log to" or operator =="logoff" or operator =="LOC" or operator =="logo":
            result = math.log10(number2)
            print("operator is Log Base 10 cat -- {}".format(operator))
            print(result)
            wordresult = num2words(result)
            print (wordresult)
            wordbreak = re.sub(r'-',r' ',wordresult)
            engine.say(wordbreak)
            engine.runAndWait()

        elif operator =="Sin" or operator=="Sine" or operator=="sin" or operator =="sine" or operator =="signed":
            result = math.sin(number2)
            print("operator is Sine cat -- {}".format(operator))
            print(result)
            wordresult = num2words(result)
            print (wordresult)
            wordbreak = re.sub(r'-',r' ',wordresult)
            engine.say(wordbreak)
            engine.runAndWait()

        elif operator =="cos" or operator=="cosine" or operator=="Cosine" or operator=="Cos" or operator=="cause" or operator=="Cause":
            result = math.sin(number2)
            print("operator is Sine cat -- {}".format(operator))
            print(result)
            wordresult = num2words(result)
            print (wordresult)
            wordbreak = re.sub(r'-',r' ',wordresult)
            engine.say(wordbreak)
            engine.runAndWait()
    
    
    else:
        
        number2 = re.search(r'\d+',matchplus.group(3))
        if number2==None:
            if matchplus.group(3) =="to":
                number2 = 2
            elif matchplus.group(3) == "hundred":
                number2 = 100
            else :
                number2 = text2int(matchplus.group(3))
            print("Second number is {}".format(number2))
        else:
            number2 = int(number2.group(0))
            print("Second number is {}".format(number2)) 
    
    
    
        if operator=='plus' or operator=='+': 
            print("operator is plus cat -- " + operator)
            print (number1 + number2)
            result = number1+number2
            wordresult = num2words(result)
            print (wordresult)
            wordbreak = re.sub(r'-',r' ',wordresult)
            engine.say(wordbreak)
            engine.runAndWait()
    
        elif operator=="times" or operator=="multiply" or operator=="multiplied by" or operator=="*" or operator=="x" or operator=="X" or operator=="cross" or operator=="into" or operator=="in two" or operator=="in to" or operator=="in 2":    
            print("operator is mul cat{} --" + operator)
            print(number1 * number2)
            result = number1*number2
            wordresult = num2words(result)
            print (wordresult)
            wordbreak = re.sub(r'-',r' ',wordresult)
            engine.say(wordbreak)
            engine.runAndWait()
    
        elif operator=="minus" or operator=="-" :    
            print("operator is minus cat{} --" + operator)
            print(number1 - number2)
            result = number1-number2
            wordresult = num2words(result)
            print (wordresult)
            wordbreak = re.sub(r'-',r' ',wordresult)
            engine.say(wordbreak)
            engine.runAndWait()
    
        elif operator=="/" or operator=="divide" or operator=="divided by":    
            print("operator is Divide cat{} --" + operator)
            if number2 == 0 :
                print ("Uhh.. Come on, are you serious. You really wanna divide by 0, its infinite")
                engine.say("Uhh.. Come on, are you serious. You really wanna divide by 0, its infinite")
                engine.runAndWait()
            else:
                print(number1 / number2)
                result = number1/number2
                wordresult = num2words(result)
                print (wordresult)
                wordbreak = re.sub(r'-',r' ',wordresult)
                engine.say(wordbreak)
                engine.runAndWait()
    
        elif operator=="^" or "to the power" or "raised to the power" or "2 the power"  or "2 the power" or "raised to": 
            print("operator is power cat{} --" + operator)
            result = number1**number2
            print (result)
            wordresult = num2words(result)
            print (wordresult)
            wordbreak = re.sub(r'-',r' ',wordresult)
            engine.say(wordbreak)
            engine.runAndWait()

    


else:
    print("Ohh... I Didnt find you")
    engine.say("Ohh... I Didnt find you")
    engine.runAndWait()