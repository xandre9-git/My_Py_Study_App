import time

# countdown function
# countsdown time of session
def countdown(t):
      while t:
        mins, secs = divmod(t, 60) # divmod(x, y) x is numerator, y is denominator, this returns a tuple of quotient and remainder
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('Session in progress: ', timer, end="\r")
        time.sleep(1)
        t -= 1
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
  for key, value in dict.items():
    if val == value:
      return key

  return "key doesn't exist"

# value selector function for keys in dictionary
def get_val(k, dict):
  for key, value in dict.items():
    if k == key:
      return value

  return "value doesn't exist"

# start of program   
print('\nMy Py Study App Version 1.0') # print version of app
print('Developed by Xandre9') # me
print('') # spacer

while True:
  menu_selection = menu_prompt() # run menu screen selection
  if menu_selection == 1:
    print("\nSubject Archive")
    placeholder_dict = {1: 'Python', 2: 'JavaScript', 3: 'HTML & CSS'}

    for k,v in placeholder_dict.items():
      print(k,'.', ' ', v,sep="") # print numbered list of archive
  
    subj = input('\nWhat will you study? Enter corresponding number of subject from archive or type in a new subject. (Enter "quit" to exit) \n')    
    if subj == "quit" : 
      print("Winners don't quit.")
      quit()
    else:
      subj = int(subj) # if number of prior sesssion is selected, convert to integer
      current_val = get_val(subj, placeholder_dict) # uses integer key value of placeholder_dict, gets its value from respective dictionary, and stores in  new var
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

  study_data = open('study_data.txt', 'wt') # plan is to open database of study sessions with subject and duration studied (in hours:mins)

# need to program numbered or text menu option to offer selections (start session, bank, stats,)

# print("Study Bank\n") 
# print(read_data.read()) # displays subjects studied

# countdown vs stopwatch

# implement option to either have stopwatch or countdown session

# a pause/resume feature needs to be implemented

  session = dict()
  session[current_val] = t
  # print(session.get(subj))
  print('You studied', current_val, 'for', session.get(subj), 'minute(s).')
  data = str(session)
  study_data.write(data)



# at end of session prompt user to either (close program, view study archive, restart session)


placeholder_dict = {1: 'Python', 2: 'JavaScript', 3: 'HTML & CSS'}

for k,v in placeholder_dict.items():
  print(k,'.', ' ', v,sep="")

subj = input('\nWhat will you study? Enter corresponding number of subject from archive or type in a new subject. (Enter "quit" to exit) \n')
subj = int(subj)
print(placeholder_dict[subj])

if placeholder_dict[subj] == placeholder_dict.keys() : print('Never give up.')