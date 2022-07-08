
# -------------------------------------------- 
# Day 2 Challenges
# -------------------------------------------- 

message = "Welcome to Day 2.\nToday we are learning about conditionals.\nLet's practice writing some conditionals of our own!"
print(message)
# -------------------------------------------- 

print("------------------- Challenge 1 -------------------")
# Can you drive?
   # Prompt the user to enter their age.
   # Write conditional statements that print out whether you can drive in your city. 

print("Hi")
num=int(input())
if(num >= 17):{
print("Yes, you can")
}
else:{
print("No, you cant")
}

# -------------------------------------------- 

print("------------------- Challenge 2 -------------------") 

# Who placed first?
   # Write conditional statements that checks which is the highest and prints the highest score. 
   # Hint: Create three variables and assign them random scores. 

first = 100
second = 200
third = 300

if(first > second and first > third):{print(first)}
elif(second > first and second > third): print(second)
elif(third > first and third > second): print(third)










# -------------------------------------------- 

print("------------------- Challenge 3 -------------------")

# One of the most common parts of our daily routine is checking the weather. 
# Our outfit and accessories are dependent on the temperature and conditions outside. 
# ie. We're probably not going to wear shorts out when it's snowing...


# **** Challenge 3: Part 1 ****
# Write a conditional statement that checks the value of the weather variable 
# and prints out a weather report based on the current weather:
# Rainy: Bring an umbrella
# Sunny: Wear a hat and sunglasses
# Snowing: Wear gloves and a scarf 

# Here's a variable to get you started:
weather = "rainy"

if(weather == "rainy"):{
   print("Bring an umbrella")
}
elif(weather == "Sunny"):{
   print("Wear a hat and sunglasses")
}
elif(weather == "Snowing"):{
   print("ear gloves and a scarf ")
}


# Tip: Try changing the value of the weather variable to test your other conditions.

# **** Challenge 3: Part 2 ****
# Now that you've written conditions for specific weather forecasts, let's also add in temperature! 
# You can't dress accordingly if you only know that it's raining outside but not how cold it is!
# For example:
    # If it's raining and 60 degrees, you might want to bring your umbrella and wear a light jacket.
    # However, if it's raining and 30 degrees, you might want to break out a warmer jacket with your umbrella instead. 
    
   # Add to your conditional statements above and modify your weather reports to also take into account the temperature. 
   # Make sure to account for at least three different temperatures!
   # Hint: You will need another variable to keep track of the temperature.

weather = "Sunny"
temperature = 110

if(weather == "rainy" and temperature >= 60):{
   print("Bring your umbrella and wear a light jacket.")
}
elif(weather == "rainy" and temperature >= 40 and temperature < 60):{
   print("Break out a warmer jacket with your umbrella instead.")
}
elif(weather == "rainy" and temperature <= 40):{
   print("Bring an umbrella and jecket under 40")
}


elif(weather == "Sunny" and temperature >= 90):{
   print("Wear a hat and sunglasses more 90")
}
elif(weather == "Sunny" and temperature >= 60 and temperature < 90):{
   print("Wear a hat and sunglasses under 90")
}
elif(weather == "Sunny" and temperature <= 60):{
   print("Wear a hat and sunglasses under 60")
}

elif(weather == "Snowing" and temperature >= 50):{
   print("ear gloves and a scarf more 50")
}
elif(weather == "Snowing" and temperature >= 40 and temperature < 50):{
   print("ear gloves and a scarf under 50")
}
elif(weather == "Snowing" and temperature <= 20):{
   print("ear gloves and a scarf under 20")
}


# -------------------------------------------- 

print("------------------- Challenge 4 -------------------")

# Prompt the user to enter the day of the week (1-7 representing Monday - Sunday)
# Write a set of conditionals that will take a number from 1 to 7 
# and print out the corresponding day of the week. 
# Make sure to add a statement that accounts for any numbers out of range! 





print("day")
day = int(input())

# mon = 1
# tue = 2
# wed = 3
# thu = 4
# fri = 5
# sur = 6
# sun = 7

# if(day > 7 and day <1):{print("wrong day")}
# else:{
#    switcher = {
#         mon: print("mon"),
#         tue: print("tue"),
#         wed: print("wed"),
#         thu: print("thu"),
#         fri: print("fri"),
#         sur: print("sur"),
#         sun: print("sun"),
#       #   if(day > 7 and day <1):{print("wrong day")}
#     }
# }

if(day > 7 or day <1):{print("wrong day")}
elif(day == 1):{print("mon")}
elif(day == 2):{print("tue")}
elif(day == 3):{print("wed")}
elif(day == 4):{print("thu")}
elif(day == 5):{print("fri")}
elif(day == 6):{print("sat")}
elif(day == 7):{print("sun")}




# -------------------------------------------- 

print("------------------- Challenge 5 -------------------")

# A leap year is a calendar year that contains an additional day added 
# to keep the calendar year synchronized with the astronomical year or seasonal year.
# To calculate if a specific year is/was a leap year, you can follow the following steps:
     # 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
     # 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
     # 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
     # 4. The year is a leap year (it has 366 days).
     # 5. The year is not a leap year (it has 365 days).

# Those are a lot of conditions...
# Your challenge is to translate the steps above into conditionals which will evaluate if the 
# year stored in a variable is/was a leap year.

print("Input year")
year = int(input())

step_1 = year%4 == 0
step_2 = year%100 == 0
step_2_1 = year%100 != 0
step_3 = year%400 == 0
if(step_3 and step_2 and step_1):{print("366")}
elif(step_2_1):{print("366 too")}
else:{print("not")}




