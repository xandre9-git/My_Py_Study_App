import time

# countdown function
def countdown(t):
      while t:
        mins, secs = divmod(t, 60) # divmod(x, y) x is numerator, y is denominator, this returns a tuple of quotient and remainder
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('Session in progress: ', timer, end="\r")
        time.sleep(1)
        t -= 1
      print('\nSession complete.')

# header   
print('\nMy Py Study App Version 1.0') # print version of app
print('Developed by Xandre9') # me
print('') # spacer

# menu prompt
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


while True:
  menu_selection = menu_prompt()


  if menu_selection == 1:
    print("\nSubject Archive")

  # subjects studies should be lisquit

    subj = input('\nWhat will you study? Enter corresponding number of subject from archive or enter a new subject. (Enter "quit" to exit) \n') # query user for subject and duration (need to incorporate way to access prior study sessions to continue)
    if subj == "quit" : 
      print("Winners don't quit.")
      quit
    else:
      print("\nTimer Type\n1. Countdown\n2. Stopwatch\n")
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
  session[subj] = t
  # print(session.get(subj))
  print('You studied', subj, 'for', session.get(subj), 'minute(s).')
  data = str(session)
  study_data.write(data)



# at end of session prompt user to either (close program, view study archive, restart session)