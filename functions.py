# -------------------------------------------- 

	# You've just learned about functions.
	# Functions are reusable pieces of code that make your code more modular.
	
	# If you are writing the same bit of code over and over, you are doing more work that you have to.
	# Use functions to simplify your code and decrease the amount of work you're doing. 

	# Any time you start thinking 'this is tedious', you can probably write a function for that task.

# -------------------------------------------- 


# -------------------------------------------- 
  # Challenge 1: Let's try to write some basic functions.
# -------------------------------------------- 

print("------------------- Challenge 1 -------------------")

# **** Challenge 1: Problem 1 ****
# Write a function called print_message() that prints any message you want.

def print_message():
      print("message")


# **** Challenge 1: Problem 2 ****
# Write a function called print_five_messages() that calls print_message() five times.

def print_five_messages():print_message(),print_message(),print_message(),print_message(),print_message()



# **** Challenge 1: Problem 3 ****
# Write a function called get_user_input() that asks the user if they'd like to print your message
# once or five times. Then call one of the two functions above based on what the user decides.

def get_user_input():
	print("How many times(once or five)")
	call_times = str(input())
	if (call_times == "once" or call_times == "1"):{print_message()}
	elif (call_times == "five" or call_times == "5"):{print_five_messages()}
	else:{print("wrong")}
# **** Challenge 1: Problem 4 ****
# Write a function called print_greeting() that prints a greeting message to the user.

def print_greeting():
    	print("Hello")

# **** Challenge 1: Problem 5 ****
# Write a function called print_closing() that prints a goodbye message to the user.

def print_closing():
    	print("Goodbye")

# **** Challenge 1: Problem 6 ****
# Write a function called run() that greets the user, asks them for input, and sends a goodbye message.
# Remember! Use the functions that you've already made. Don't hardcode anything!

def run():print_greeting(),get_user_input(),print_closing()

# -------------------------------------------- 

# Challenge 2: Functions are also able to take input and return output. 
				# The value(s) you pass to it are called parameters.
run()
# -------------------------------------------- 

print("------------------- Challenge 2 -------------------")

# **** Challenge 2: Problem 1 ****

# Write a function called sum_double that takes two number paramters and returns their sum.
# However, if the two values are the same, the funciton will return double their sum.

	# Examples:
		# sum_double(1, 2) → 3
		# sum_double(3, 2) → 5
		# sum_double(2, 2) → 8

# -------------------------------------------- 

def sum_double():
    print("Please enter first num for sum")
    num_1 = int(input())
    print("The second number")
    num_2 = int(input())
    num_3 = num_1 + num_2
    print(num_3)
sum_double()
    	

# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 2 ****

# Write a function called makes_10 that takes two numbers, a and b, and returns true if one of them is 10 or if their sum is 10.

	# Examples:
		# makes_10(9, 10) → True
		# makes_10(9, 9) → False
		# makes_10(1, 9) → True

# -------------------------------------------- 
def makes_10():
    print("Please enter first number:")
    num_1 = int(input())
    print("The second number")
    num_2 = int(input())
    if(num_1 == 10 or num_2 == 10):{print("True")}
    elif((num_1 + num_2) == 10):{print("True")}
    else:{print("False")}
makes_10()
		
# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 3 ****

# Write a function that will return the time our alarm is set to go off.

# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean
# indicating if we are on vacation, return a string in the form "7:00" indicating
# when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on
# the weekend it should be "10:00". However, if we are on vacation -- then on weekdays
# it should be "10:00" and weekends it should be "off".
	# Examples:
		# alarm_clock(1, False) → "7:00"
		# alarm_clock(6, True) → "off"
		# alarm_clock(0, False) → "10:00"

# -------------------------------------------- 

#7:00 weekday False
#10:00 weekday True, weekend False
#off weekend True


# print("Print day of week(0=Sun, 1=Mon, 2=Tue, ...6=Sat)")

def alarm_time():
    bool_indicating = False	
    print("Print day of week(0=Sun, 1=Mon, 2=Tue, ...6=Sat)")
    alarm_day = int(input())
    print("Should it work(True or False")
    bool_res = str(input())
    if (bool_res == "True"):bool_indicating = True
    elif (bool_res == "False"):bool_indicating = False
    if ((alarm_day == 1 or alarm_day == 2 or alarm_day == 3 or alarm_day == 4 or alarm_day == 5) and bool_indicating == False):{print("7:00")}
    elif(((alarm_day == 1 or alarm_day == 2 or alarm_day == 3 or alarm_day == 4 or alarm_day == 5) and bool_indicating == True) or ((alarm_day == 0 or alarm_day == 6) and bool_indicating == False)):{print("10:00")}
    elif((alarm_day == 0 or alarm_day == 6) and bool_indicating == True):{print("off")}
    else:{print("wrong")}

alarm_time()
# answ_tru = ["True" or "T" or "Tr" or "Tru" or "t" or "true"]
# answ_fal = ["False", "F", "Fal", "false","f"]

# answ_tru = "True"
# answ_fal = "False"

# def alarm_clock():

#     print("Hi, input your day(0,1,2,3,4,5,6)")
#     answ_day = int(input())
#     print("Should it work(True or False")
#     answ_bool = str(input())
#     def answDay():
#         if(answ_day > 6 or answ_day <0):{print("wrong day")}
#         elif(answ_day == 0):{print("mon")}
#         elif(answ_day == 1):{print("tue")}
#         elif(answ_day == 2):{print("wed")}
#         elif(answ_day == 3):{print("thu")}
#         elif(answ_day == 4):{print("fri")}
#         elif(answ_day == 5):{print("sat")}
#         elif(answ_day == 6):{print("sun")}
#         else:{print("Wrong day")}
    
#     def answBool():
#         if(answ_bool == answ_tru):{print("True")}
#         elif(answ_bool == answ_fal):{print("False")}
#         else:{print("Wrong input (True or False)")}

#     answBool()
#     answDay()
#     if ((answDay() == "sat" or answDay == "sun") and answBool == "True"):{print("off")}
#     elif((answDay() == "tue" or answDay == "wed" or answDay == "thu" or answDay == "fri" or answDay == "mon") and answBool == "False"):{print("7:00")}
#     else:{print("10:00")}
	 


# alarm_clock()

# # if (answBool == "sat" or "mon"):{}

# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 4 ****

# Write a function that will tell you if you received a speeding ticket.
# You are driving a little too fast, and a police officer stops you. 

# To compute the result, encoded as a number value: 
	# 0=no ticket
	# 1=small ticket
	# 2=big ticket
# If speed is 60 or less, the result is 0. 
# If speed is between 61 and 80 inclusive, the result is 1. 
# If speed is 81 or more, the result is 2.

# -------------------------------------------- 

def ticket_test():
    print("Please enter your speed")
    input_speed = int(input())
    if(input_speed <= 60):{print("no ticket")}
    elif(input_speed <80 or input_speed > 61):{print("small ticket")}
    elif(input_speed >=80):{print("big ticket")}
    else:{print("Wrong speed")}

ticket_test()





# Make sure to test your code! Write a few function calls to make sure your code works!
