import pyautogui
import time

time.sleep(5)
print("*"*60)
print("\t\tWhatsApp ChatBox")
print("*"*60)
Num_of_times = int(input("\nHow many times do u want sent msg:\t"))
msg = input("Enter msg:\t")
print("\n NOW ENJOY THE FUN...")

count = 0
while count<=Num_of_times:
    pyautogui.typewrite(f"{str(count)}. {msg}")
    pyautogui.press("enter")
    count+=1
    
  

