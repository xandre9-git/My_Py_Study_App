import time
import pickle
import sys, select, os
import math
from playsound import playsound

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
      while t == 0:
        print("Press enter to stop alarm.", end='\r')
        playsound('alarm.mp3')
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
          line = input()
          break

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
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]: # allows enter key to cease stopwatch
      line = input()
      break
    
 end = time.time() - 1
 elapsed = end - begin
 elapsed = int(elapsed)
 print('Session complete.')
 playsound('temple.mp3')
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

# dictionary value append function
def append_value(dict, key, value):
  if key in dict: # check if key is already in dict
    if not isinstance(dict[key], list): # if key is in dict but not a list.
      dict[key] = [dict[key]] # make list with key as element
      dict[key].append(value) # append value to dictionary's key
  else:
    dict[key] = value # if key not in dict, add key and value

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
    subj = input('\nWhat will you practice? Enter corresponding number of subject from archive or type in a new discipline. (Enter "quit" to exit) \n')    
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
      # t = t * 60
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

    else: # for new subjects
      session[subj] = t # set new session subject key with value as time
      subject_bank.append(subj)

    
    append_value(test_dict, subject_bank[len(subject_bank)-1], t)

    fhand = open('study_data.pickle', 'wb')
    pickle.dump(test_dict, fhand)
    fhand.close()
  
    # study session summary
    mins, secs = divmod(t, 60)
    session_duration = '{:02d}:{:02d}'.format(mins, secs)
    print('Your', subject_bank[len(subject_bank)-1], 'session duration:', session_duration)
  
  # review sessions
  elif menu_selection == 2:
    # header
    print("\nSubject Review")

    # numbered subject dictionary
    count = 0
    for k,v in test_dict.items():
      count += 1
      print(count,". ", k, sep="")

    # append key to list loop
    subj_list = list()
    for k, v in test_dict.items():
      subj_list.append(k)
    
    # append value to list loop
    time_list = list()
    for k, v in test_dict.items():
      time_list.append(v)
    
    subj = input('\nEnter number of subject for more details: ')
    subj = int(subj)
    subj = subj - 1
    print("\n",subj_list[subj],' selected.', sep="")

    # this will need to be changed to display dynamic amount of time studied (hours, minutes, and seconds)
    if type(time_list[subj]) is int:
      print('You have practiced', subj_list[subj], 'for a total of', time_list[subj], 'second(s).')
      # You have practiced s for a total of x hours, y minutes, and z seconds.
    else:
      print('You have practiced', subj_list[subj], 'for a total of', sum(time_list[subj]), 'second(s).')

    edit_prompt = input("\nWhat would you like to do with this data? \n\nCommand List:\n'del' to remove all data of selected subject\n'rtn' to return to main menu\n")

    # may program 'avg' option to calculate average length of study sessions.
    if edit_prompt == 'del':
      confirm_del = input("Please type 'yes' to confirm or 'no' to cancel: ")
      if confirm_del == 'no':
        print("Nothing was deleted.")
        # menu_prompt()    
      if confirm_del == 'yes':
        print(subj_list[subj], 'was deleted from the database.')
        del test_dict[subj_list[subj]]
        fhand = open('study_data.pickle', 'wb')
        pickle.dump(test_dict, fhand)
        fhand.close()

    if edit_prompt == 'rtn':
      print('Returning to main menu.')

  # exit program
  elif menu_selection == 3:
      print("Thank you for using my program.")
      exit()


  