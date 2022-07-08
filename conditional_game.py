import random
from secrets import choice

# -------------------------------------------- 

	# You've just learned about variables, conditionals.
	# Just from knowing those two topics, you can do so much!
	
	# Let's try to make a simple program that responds to the user.
	# We're going to recreate the Magic 8 Ball!!!
			
			# Never heard of it? That's ok!

					# You got this!

  # -------------------------------------------- 

	# How a Magic 8 Ball Works:

	# The user asks a question and vigoriously shakes the ball. 
	# Then the ball will respond with one of twenty responses, chosen at random. 

	# That's pretty simple right?

 # -------------------------------------------- 

	# Part 1: 
	# Print instructions on the screen and 
	# prompt the user to ask a question

	

  # --------------------------------------------

answer_0 = "As I see it, yes."
answer_1 = "It is certain."
answer_2 = "It is decidedly so."
answer_3 = "Without a doubt."
answer_4 = "Yes - definitely."
answer_5 = "You may rely on it."
answer_6 = "Most likely."
answer_7 = "Outlook good."
answer_8 = "Yes."
answer_9 = "Signs point to yes."
answer_10 = "Reply hazy, try again."
answer_11 = "Ask again later."
answer_12 = "Better not tell you now."
answer_13 = "Cannot predict now."
answer_14 = "Concentrate and ask again."
answer_15 = "Don't count on it."
answer_16 = "My reply is no."
answer_17 = "My sources say no."
answer_18 = "Outlook not so good."
answer_19 = "Very doubtful."

cells = [answer_0, answer_1, answer_2, answer_3, answer_4, answer_5, 
answer_6, answer_7, answer_8, answer_10, answer_11, answer_12, answer_13, answer_14, answer_15,
answer_16, answer_17, answer_18, answer_18, answer_19]

print("Ask a question")
question = input()

# random.choice(cells) = answer

answer = choice(cells)
print(answer)
# -------------------------------------------- 

	# Part 2: Next, we need to randomly select a response from 20 options.

	# Randomly select a number from 0 - 19 
	# Use that to select from the following responses:
		# 0 - It is certain.
		# 1 - It is decidedly so.
		# 2 - Without a doubt.
		# 3 - Yes - definitely.
		# 4 - You may rely on it.
		# 5 - As I see it, yes.
		# 6 - Most likely.
		# 7 - Outlook good.
		# 8 - Yes.
		# 9 - Signs point to yes.
		# 10 - Reply hazy, try again.
		# 11 - Ask again later.
		# 12 - Better not tell you now.
		# 13 - Cannot predict now.
		# 14 - Concentrate and ask again.
		# 15 - Don't count on it.
		# 16 - My reply is no.
		# 17 - My sources say no.
		# 18 - Outlook not so good.
		# 19 - Very doubtful.

	# Look up random.rand_int to see how you can use it to select a random number.

  # -------------------------------------------- 








# -------------------------------------------- 

	# Part 3: Customize it!

	# Select your own theme and use case and modify your code!
	
# -------------------------------------------- 

















