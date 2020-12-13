# User greeting

print("Welcome to the Love Calculator!")

# Ask for the names

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Convert them to lowercase

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

# Initialize letters' counter

true_counter = 0
love_counter = 0

# Evaluate first name

t_letter = lower_case_name1.count("t")
r_letter = lower_case_name1.count("r")
u_letter = lower_case_name1.count("u")
e_letter = lower_case_name1.count("e")

if t_letter == True:
  true_counter += t_letter
if r_letter == True:
  true_counter += r_letter
if u_letter == True:
  true_counter += u_letter
if e_letter == True:
  true_counter += e_letter

l_letter = lower_case_name1.count("l") 
o_letter = lower_case_name1.count("o")
v_letter = lower_case_name1.count("v")
e_letter = lower_case_name1.count("e")

if l_letter == True:
  love_counter += l_letter
if o_letter == True:
  love_counter += o_letter
if v_letter == True:
  love_counter += v_letter
if e_letter == True:
  love_counter += e_letter

# Evaluate second name

t_letter = lower_case_name2.count("t")
r_letter = lower_case_name2.count("r")
u_letter = lower_case_name2.count("u")
e_letter = lower_case_name2.count("e")

if t_letter == True:
  true_counter += t_letter
if r_letter == True:
  true_counter += r_letter
if u_letter == True:
  true_counter += u_letter
if e_letter == True:
  true_counter += e_letter

l_letter = lower_case_name2.count("l") 
o_letter = lower_case_name2.count("o")
v_letter = lower_case_name2.count("v")
e_letter = lower_case_name2.count("e")

if l_letter == True:
  love_counter += l_letter
if o_letter == True:
  love_counter += o_letter
if v_letter == True:
  love_counter += v_letter
if e_letter == True:
  love_counter += e_letter

# Convert both scores to strings then to integers to concatenate them

final_score = str(true_counter) + str(love_counter)
int_score = int(final_score)

if int_score < 10 or int_score > 90:
  print(f"Your final score is {int_score}. You go together like coke and mentos.")
elif int_score >= 40 and int_score <= 50:
  print(f"Your score is {int_score}, you are alright together.")
else:
  print(f"Your score is {int_score}.")