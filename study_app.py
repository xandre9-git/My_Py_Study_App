import time
import pickle
from study_data import py_study_data
from subject_list import py_subj_list

# countdown function
# counts down time of session
def countdown(t):
      while t:
        mins, secs = divmod(t, 60) # divmod(x, y) x is numerator, y is denominator, this returns a tuple of quotient and remainder
        timer = '{:02d}:{:02d}'.format(mins, secs) # {:d} is a formatting character, treat argument as an integer with two digits, d stands for decimal integer, (base 10)
        print('Session in progress: ', timer, end="\r") # \r is carriage return, print function by default has end=\n, can be changed.
        time.sleep(1) # sleep method suspends execution for specified time in seconds
        t -= 1 # with each loop decrease t by 1
      print('\nSession complete.')

# menu prompt function
# create prompt that displays choices
def menu_prompt():
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

# start of program   
print('\nMy Py Study App Version 1.0') # print version of app
print('Developed by Xandre9') # me
print('') # spacer

# default sequence is created with while loop
while True:
  menu_selection = menu_prompt() # run menu screen selection
  if menu_selection == 1: # option 1
    print("\nSubject Archive")

    # placeholder_dict = {1: 'Python', 2: 'JavaScript', 3: 'HTML & CSS'} # current dictionary (need to program a LIST that can be updated in this section)
    # subject_archive = open('subject_list.txt', 'r')
    # for line in subject_archive:
    #   print(line)

    # for k,v in placeholder_dict.items():
    #   print(k,'.', ' ', v,sep="") # print numbered list of archive
    pickle_in = open("study_data.pickle", 'rb')
    test_dict = pickle.load(pickle_in)

    count = 0
    for k,v in test_dict.items():
      count += 1
      print(count,". ", k, sep="")
  
    subj = input('\nWhat will you study? Enter corresponding number of subject from archive or type in a new subject. (Enter "quit" to exit) \n')    
    if subj == "quit" : 
      print("Winners don't quit.")
      quit()
    else:
      try:
        subj = int(subj) # if number of prior sesssion is selected, convert to integer
        current_val = get_val(subj, py_study_data) # uses integer key value of placeholder_dict, gets its value from respective dictionary, and stores in  new var

        subj = subj - 1 # convert selection to index counting
      except:
        subj = subj
        # print(subj)

      print("\nTimer Type\n1. Countdown\n2. Stopwatch\n") # displays timer selection
    time_query = input("Enter number of desired timing method: ")
    time_query = int(time_query)
    if time_query == 1:
      t = input('What is the duration of this session? Enter in minutes: ')
      t = int(t)
      # t = t * 60
      countdown(t)
    elif time_query == 2: 
      print("Feature not currently implemented. Please restart selections.\n")
      continue
    
  elif menu_selection == 2:
    print('\nOkay, review past sessions.')
    print("This will eventually use function that opens up prior study sessions")
    exit()

  elif menu_selection == 3:
      print("Thank you for using my program.")
      exit()

# study bank
# to be opened if #2 from above is selected

  # study_data = open('study_data.txt', 'a') # opens study data text file which will be used to store subject and duration of session
  # subject_list = open('subject_list.txt', 'a') # opens subject list file which will be used to store only subject

# plan is to open database of study sessions with subject and duration studied (in hours:mins)
# need to program numbered or text menu option to offer selections (start session, bank, stats,)
# print("Study Bank\n") 
# print(read_data.read()) # displays subjects studied
# countdown vs stopwatch
# implement option to either have stopwatch or countdown session
# a pause/resume feature needs to be implemented

  # current session subject and duration dictionary
  session = dict() # create dictionary for current session
  subject_bank = list() # create list for current subject studied
 
  if isinstance(subj, (int, float)) == True: 
    session[py_subj_list[subj]] = t # store subject as key and time of session as its value
    # print(session)
    subject_bank.append(py_subj_list[subj])
    # print('py study data', py_study_data)
    # subj =+ 1
    # print('subj #', subj)
    # study_val = get_val(subj, py_study_data)
    # print('study val', study_val)
    # subject_bank.append(study_val)
    # print(subject_bank, 'new entry')
  else: 
    session[subj] = t
    subject_bank.append(subj)
  # print(session)

  # store in dict as new entry, if it already exists, add to it. (get method)
  # print(py_study_data)

  # from study_app export py_study_data
  py_study_data.update(session)

  fhand = open('study_data.pickle', 'wb')
  pickle.dump(py_study_data, fhand)
  fhand.close()

  print(py_study_data)
  session_data = str(session) # convert dictionary into string
  # study_data.write(session_data) # write dictionary with subject and duration into study_data.txt (What if the subject already exists? How to add to existing subject and duration)
  # study_data.close()

  # current session subject list
  subject_entry = str(subject_bank)
  # subject_list.write(subject_entry)
  # subject_list.close()
  
  # study session summary
  print('You studied', subject_bank[len(subject_bank)-1], 'for', t, 'minute(s).')
  