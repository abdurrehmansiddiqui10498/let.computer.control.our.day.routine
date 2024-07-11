#How to use a computer to tell what to do in the morning
Todo_list_Day = ["'Wakeup "," Brush your teeth'","Have breakfast"]# This is the day list
a = (input("What is the time"))#This will take input of time
while a != "Day list is done":#Condition + loop is set
 if a == "10:00":# if input = this time then
  print("")
 print(Todo_list_Day[0],Todo_list_Day[1],sep="and")#It will print the index 0 and 1
 print("")
 b = (input("Have you brushed your teeth?"))#Another question asked
 if b == "Yes" or b == "yes":#if it is either of these
   print("")
   print("Now",Todo_list_Day[2])#It will print index 2
 else:
   print("Go brush your teeth") #Otherwise
 print("")
 a = input("Now what is the time")# We have repeated the variable so we can change the input.If it is = the line below the loop will break
 if a == "Day list is done":
   print("Ok")
   
   