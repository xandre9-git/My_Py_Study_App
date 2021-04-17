import time
import pickle
import sys, select, os
import math

# countdown function
# counts down time of session
def countdown(t):
      while t:
        mins, secs = divmod(t, 60) # divmod(x, y) x is numerator, y is denominator, this returns a tuple of quotient and remainder
        timer = '{:02d}:{:02d}'.format(mins, secs) # {:d} is a formatting character, treat argument as an integer with two digits, d stands for decimal integer, (base 10)
        print('Session in progress:', timer, end="\r") # \r is carriage return, print function by default has end=\n, can be changed.
        time.sleep(1) # sleep method suspends execution for specified time in seconds
        t -= 1 # with each loop decrease t by 1
      print('\nSession complete.')

# stopwatch function
def stopwatch():
 start = input("Press enter to start the stopwatch and enter again to stop.")
 begin = time.time() # begin stopwatch
 count = 0 # init counter
 while True:
    # os.system('cls' if os.name == 'nt' else 'clear') # allows listening for enter key press
    mins, secs = divmod(count, 60) # quotient and remainder
    stopwatch = '{:02d}:{:02d}'.format(mins, secs) # stopwatch time format
    print('Session in progress:', stopwatch, end='\r')
    time.sleep(1)
    count += 1    
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
      line = input()
      break
    
 end = time.time() - 1
 elapsed = end - begin
 elapsed = int(elapsed)
 print('Session complete.')
 return elapsed

# menu prompt function
# create prompt that displays choices
def menu_prompt():
  print('')
  print("                       Menu                       ")
  print("--------------------------------------------------")
  print("| 1. Start New Session                           |")
  print("| 2. Review Prior Sessions                       |")                  
  print("| 3. Exit                                        |")
  print("--------------------------------------------------")
  menu_prompt = input("\nPlease enter a number from above to continue: ")
  menu_prompt = int(menu_prompt)
  return menu_prompt

# key selector function for values in dictionary
def get_key(val, dict):
  for key, value in dict.items(): # for each key and value in items of dictionary...
    if val == value: # if val arg matches value
      return key # return its key

  return "key doesn't exist" # if no key matches value print this

# value selector function for keys in dictionary
def get_val(k, dict):
  for key, value in dict.items(): # for each key and value in dictionary
    if k == key: # if argument matches key
      return value # print its value

  return "value doesn't exist" # otherwise print this

# load prior session data from pickle
pickle_in = open("study_data.pickle", 'rb') # opens pickle file in read binary mode
test_dict = pickle.load(pickle_in) # loads pickle data into new dictionary var

# start of program   
print('\nMy Py Study App Version 1.0') # print version of app
print('Developed by Xandre9') # me

# default sequence is created with while loop
while True:
  menu_selection = menu_prompt() # run menu screen selection
  if menu_selection == 1: # option 1
    print("\nSubject Archive")

    # # load prior session data from pickle
    # pickle_in = open("study_data.pickle", 'rb') # opens pickle file in read binary mode
    # test_dict = pickle.load(pickle_in) # loads pickle data into new dictionary var

    # numbered subject dictionary
    count = 0
    for k,v in test_dict.items():
      count += 1
      print(count,". ", k, sep="") # sep="" removes the space
    
    # key to list loop
    subj_list = list()
    for k, v in test_dict.items():
      subj_list.append(k)
  
    # user query
    subj = input('\nWhat will you study? Enter corresponding number of subject from archive or type in a new subject. (Enter "quit" to exit) \n')    
    if subj == "quit" : 
      print("Winners don't quit.")
      quit()
    else:
      try:
        subj = int(subj) # if number of prior sesssion is selected, convert to integer
        subj = subj - 1 # convert selection to index counting
        print(subj_list[subj], 'selected.')
      # if entry is new subject...  
      except:
        subj = subj
        print('Starting new', subj, 'session.')

      # Timer type
      print("\nTimer Type\n1. Countdown\n2. Stopwatch\n") # displays timer selection

    # countdown selected
    # need to implement play/pause feature
    
    time_query = input("Enter number of desired timing method: ")
    time_query = int(time_query)
    if time_query == 1:
      print('Countdown timer selected.')
      t = input('What is the duration of this session? Enter in minutes: ')
      t = int(t)
      t = t * 60
      countdown(t)

    # stopwatch selected
    # need to implement play/pause feature
    elif time_query == 2: 
      print('Stopwatch timer selected.')
      t = stopwatch()

      # current session subject and duration dictionary
    session = dict() # create dictionary for current session
    subject_bank = list() # create list for current subject studied
 
    if isinstance(subj, (int, float)) == True: 
      session[subj_list[subj]] = t # store subject as key and time of session as its value
      subject_bank.append(subj_list[subj])

    else: 
      session[subj] = t
      subject_bank.append(subj)

    test_dict.update(session)

    fhand = open('study_data.pickle', 'wb')
    pickle.dump(test_dict, fhand)
    fhand.close()
  
    # study session summary
    mins, secs = divmod(t, 60)
    session_duration = '{:02d}:{:02d}'.format(mins, secs)
    print('Your', subject_bank[len(subject_bank)-1], 'session duration:', session_duration)
  
  # plan is to open database of study sessions with subject and duration studied (in hours:mins)
  # allow delete function
  elif menu_selection == 2:
    # header
    print("\nSubject Review")

    # numbered subject dictionary
    count = 0
    for k,v in test_dict.items():
      count += 1
      print(count,". ", k, " - ", v, sep="")

    # key to list loop
    subj_list = list()
    for k, v in test_dict.items():
      subj_list.append(k)
    
    time_list = list()
    for k, v in test_dict.items():
      time_list.append(v)
    
    subj = input('Enter number of subject for more details and options: ')
    subj = int(subj)
    subj = subj - 1
    print(subj_list[subj],'selected.')
    print('You have studied', subj_list[subj], 'for a total of', time_list[subj])
    
    # prompt user if they would like to delete data.')

  # exit program
  elif menu_selection == 3:
      print("Thank you for using my program.")
      exit()


  