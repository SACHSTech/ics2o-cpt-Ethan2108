""" 
-------------------------------------------------------------------------------
Name: main.py

Purpose: To make a quiz about the content that we learned in this computer studies class

Author: Au.E

Date: 01/13/2021
-------------------------------------------------------------------------------
"""

# Define the score as 0 
score = 0

# Welcome the user to the quiz
print("***Welcome to the online computer studies quiz!*** ")
print("This quiz will have content from all the units of the course.")

#Asks if the user is ready to begin the quiz
question = input("Are you ready to start the quiz? ")
answer = "yes"
if question == answer:
  print("Let's start! Good luck!")

elif question == ("no"):
  print("Come back when you are ready!")
  print("Goodbye")
  print("*********END*********")

else: 
  print("INVALID ANSWER")

# Begins the quiz if the user is ready, and question 1 appears
if question == answer:
  print ("Question 1 - What are the 4 parts of the information processing cycle in order?")
  print ("a - Input, Process, Output, and Storage")
  print ("b - Process, Storage, Output, Reput")
  print ("c - Storage, Downloads, Input, Output")
  print ("d - None of the above")
  question_one = input("Enter your answer: ")
  answer_one = "a"

if question_one == answer_one:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is a.")

print ("Question 2 - How many bits are in 1 byte?")
print ("a - 1")
print ("b - 8")
print ("c - 69")
print ("d - 666911420")
question_two = input("Enter your answer: ")
answer_two = "b"

if question_two == answer_two:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is b.")

print ("Question 3 - What is the symbol for a Petabyte?")
print ("a - PB")
print ("b - pB")
print ("c - petabyte")
print ("d - There is no symbol")
question_three = input("Enter your answer: ")
answer_three = "a"

if question_three == answer_three:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is a.")

print ("Question 4 - What devices are measured by DPI?")
print ("a - Stoves, ovens, and air fryers")
print ("b - Speakers and microphones")
print ("c - Mice and printers")
print ("d - Keyboards")
question_four = input("Enter your answer: ")
answer_four = "c"

if question_four == answer_four:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is c.")

print ("Question 5 - What devices are measured by PPI?")
print ("a - There is nothing called PPI")
print ("b - Clocks and watches")
print ("c - LED Lights")
print ("d - Monitors, cameras, and smartphone screens")
question_five = input("Enter your answer: ")
answer_five = "d"

if question_five == answer_five:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is d.")

print ("Question 6 - How many megabytes are in a gigabyte?")
print ("a - 1")
print ("b - 8")
print ("c - 1024")
print ("d - 666911420")
question_six = input("Enter your answer: ")
answer_six = "c"

if question_six == answer_six:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is c.")

print ("Question 7 - Does a megabyte contain 1 million bytes or 1,048,576 bytes?")
print ("a - 1 million bytes, hence the mega in megabyte")
print ("b - 1,048,576 bytes")
question_seven = input("Enter your answer: ")
answer_seven = "b"

if question_seven == answer_seven:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is b.")

print ("Question 8 - How is processing speed often measured?")
print ("a - KB")
print ("b - MHz and GHz")
print ("c - Kg")
print ("d - Degrees celsius")
question_eight = input("Enter your answer: ")
answer_eight = "b"

if question_eight == answer_eight:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is b.")

print ("Question 9 - How is data transfer measured?")
print ("a - MB/s, MBps, GB/s, and GBps")
print ("b - A data transferring machine")
print ("c - A computer")
print ("d - A thermometer")
question_nine = input("Enter your answer: ")
answer_nine = "a"

if question_nine == answer_nine:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is a.")

print ("Question 10 - What is the role of a CPU in a computer?")
print ("a - A CPU performs basic controlling, logic, arithmetic, and input/output operations.")
print ("b - A CPU powers the computer.")
print ("c - A CPU is a display for the computer.")
print ("d - None of the above")
question_ten = input("Enter your answer: ")
answer_ten = "a"

if question_ten == answer_ten:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is a.")

print ("Question 11 - What is the role of a motherboard?")
print ("a - A motherboard outputs audio.")
print ("b - A motherboard holds the computer together.")
print ("c - A motherboard is a computer's mother.")
print ("d - A motherboard serves as a connection between the various different parts of a computer system.")
question_eleven = input("Enter your answer: ")
answer_eleven = "d"

if question_eleven == answer_eleven:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is d.")

print ("Question 12 - How is the power supply to a computer measured?")
print ("a - Height")
print ("b - Wattage")
print ("c - Speed")
print ("d - Length")
question_twelve = input("Enter your answer: ")
answer_twelve = "b"

if question_twelve == answer_twelve:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is b.")

print ("Question 13 - What are some examples of peripheral components?")
print ("a - peripheral components")
print ("b - CPU, GPU, Motherboard")
print ("c - Mouse, Keyboard, Headphones, Webcam")
print ("d - Charger, HDMI cable, USB cable")
question_thirteen = input("Enter your answer: ")
answer_thirteen = "c"

if question_thirteen == answer_thirteen:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is c.")

print ("Question 14 - Which operating systems are mainly used on mobile devices?")
print ("a - Iphone 420 OS, Samsung OS, Huawei OS, and Lenovo OS")
print ("b - Windows")
print ("c - Android and iOS")
print ("d - Chrome OS")
question_fourteen = input("Enter your answer: ")
answer_fourteen = "c"

if question_fourteen == answer_fourteen:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is c.")

print ("Question 15 - Which operating systems are mainly used on computers?")
print ("a - Android and iOS")
print ("b - Macbook Pro OS")
print ("c - Google Chromecast OS")
print ("d - Chrome OS, Linux, Mac OS, and Windows")
question_fifteen = input("Enter your answer: ")
answer_fifteen = "d"

if question_fifteen == answer_fifteen:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is d.")

print ("Question 16 - What is a Trojan Horse?")
print ("a - A horse named Trojan")
print ("b - A horse born in the city of Trojan")
print ("c - Malware that steals information")
print ("d - Malware that is written with the purpose of discovering your financial information, taking over your computer’s system resources, and in larger systems creating a “denial-of-service attack” - an attempt to make a machine or network resource unavailable to those attempting to reach it. ")
question_sixteen = input("Enter your answer: ")
answer_sixteen = "d"

if question_sixteen == answer_sixteen:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is d.")

print ("Question 17 - What is adware?")
print ("a - Malware that collects information from your browsing and displays ads on the computer based on that information")
print ("b - Malware that deletes files on the computer")
print ("c - An ad on a computer")
print ("d - All of the above")
question_seventeen = input("Enter your answer: ")
answer_seventeen = "a"

if question_seventeen == answer_seventeen:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is a.")

print ("Question 18 - What are some examples of computer viruses?")
print ("a - COVID-19")
print ("b - CryptoLocker, ILOVEYOU, MyDoom")
print ("c - SARS")
print ("d - Ransomvirus")
question_eighteen = input("Enter your answer: ")
answer_eighteen = "b"

if question_eighteen == answer_eighteen:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is b.")

print ("Question 19 - How can we prevent malware/viruses from harming our computers?")
print ("a - Treat them like how we to be treated, so they will be nice")
print ("b - Tease them and hurt their feelings, so that they won't come back to cause harm")
print ("c - Install anti-virus/anti-malware applications and be careful about what we download")
print ("d - Secure your computer in a safe to ensure nothing can harm it")
question_nineteen = input("Enter your answer: ")
answer_nineteen = "c"

if question_nineteen == answer_nineteen:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is c.")

print ("Question 20 - How can we name variables with best practices?")
print ("a - Type them like a normal sentence")
print ("b - Use underscores to separate words in a variable name")
print ("c - Avoid using digits to start variable names")
print ("d - Both B and C")
question_twenty = input("Enter your answer: ")
answer_twenty = "d"

if question_twenty == answer_twenty:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is d.")

print ("Question 21 - How can we use computers more sustainably in an environmentally friendly manner?")
print ("a - Lower the display brightness, and turn it off when it is not being used to avoid wasting electricity")
print ("b - Give money to the environment to be environmentally friendly, offsetting the energy we used by leaving it on all day")
print ("c - All of the above")
print ("d - None of the above")
question_twenty_one = input("Enter your answer: ")
answer_twenty_one = "a"

if question_twenty_one == answer_twenty_one:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is a.")

# Tells the user that the Fill in the Blanks section is starting
print ("FILL IN THE BLANKS")
print ("**************************************************")
print ("Question 22 - What will this code output?")
print ("x = 10 while x > 0: print(x) x = x - 3")
question_twenty_two = input("Enter your answer: ")
answer_twenty_two = "10, 7, 4, 1"

if question_twenty_two == answer_twenty_two:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is [10, 7, 4, 1.]")

print ("Question 23 - What condition will tell me to sleep if my alarm did not go off (alarm = False) and I’m tired (tired = True)?")
question_twenty_three = input("Enter your answer: ")
answer_twenty_three = "if not alarm and tired: sleep"

if question_twenty_three == answer_twenty_three:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is [if not alarm and tired: sleep.]")

print ("Question 24 - What will this equation output?")
print ("12 % 4")
question_twenty_four = input("Enter your answer: ")
answer_twenty_four = "0"

if question_twenty_four == answer_twenty_four:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is 0.")

print ("Question 25 - What will this program print?")
print ("for i in range(10): print hi")
question_twenty_five = input("Enter your answer: ")
answer_twenty_five = "hi hi hi hi hi hi hi hi hi hi"

if question_twenty_five == answer_twenty_five:
  print ("Good job! You got the correct answer!")
  score += 1

else:
  print ("You got the wrong answer.")
  print ("The correct answer is hi hi hi hi hi hi hi hi hi hi.")

# Calculates the user's final score and gives feedback
print ("You got", str(score), "out of 25!") 

if score < 13:
  print ("You need to study more. You did very bad on the quiz.")

elif score > 23:
  print ("You did amazing! Good job!")

else:
  print ("You could have done better.")

final_score = score * 4
print ("You got", final_score, "percent!")
print ("*****END*****")