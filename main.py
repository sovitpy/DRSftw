import pyautogui
import time

#Countdown Module Definition
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

#Main Block
spam_text = "#GhostOfTheMountains #OneSpiritOneDream"
interval = int(input("Enter time interval between each hashtag:\n"))
print("Sleeping for 10 seconds.. Point your cursor to the YouTube Chat Box")
countdown(10)
print("Starting the bot...\n\n")
n = 0
while True:
    n += 1
    pyautogui.write(spam_text,interval=0.25)
    time.sleep(1)
    pyautogui.press("enter")
    print(f"Sent!\nTotal hashtags sent: {n}")
    print("Sending again in:")
    countdown(interval)
    print("\n\n")