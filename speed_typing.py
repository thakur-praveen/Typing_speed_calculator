from time import *
import random as r
def mistake(parinput,userinput):
    error = 0
    for i in range(len(parinput)):
        try:
            if parinput[i] == userinput[i]:
                error = error +1
        except :
            error = error +1
        return error 
    
def speed_text(time_s, time_e, userinput):
    time_delay = time_e - time_s 
    time_R =  round(time_delay,2)
    speed = len(userinput)/ time_R
    return round(speed)
if __name__ == '__main__':
    while True:
        ck = input( "Ready to use yes/no: ")
        if ck == "yes":        
            text = ["what kinds of careers might be best for you is a hard thing to do. Your future may very well depend on the ways you go about finding the best job openings for you in the world of work. Some people will feel that there is one and only one job in the world for them. Hard thinking and a lot of hard work will help them find the one job that is best for them. Jobs are there for those with skills and a good work ethic. Many new young artists in the upper New England states are famous around the world as leaders in new American art. "]
            text1= r.choice(text)
            print("**** Typing Speed ****")
            print(text1)
            print()
            print()
            time_1 = time()
            textinput = input("Enter : ")
            time_2 = time()

            print("Speed :" ,speed_text(time_1, time_2, textinput),"W/sec")
            print("Error : " , mistake(text1,textinput))

        elif ck == "no":
            print("Thanks for using ")
            break

        else:
            print("Wrong input ")