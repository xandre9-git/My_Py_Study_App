import time

def countdown(t):
      while t:
        mins, secs = divmod(t, 60) # divmod(x, y) x is numerator, y is denominator, this returns a tuple of quotient and remainder
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('Currently studying', subj, timer, end="\r")
        time.sleep(1)
        t -= 1
      print('Session complete.')

      


print('\nMy Py Study App Version 1.0') # print version of app
print('Developed by Xandre9') # me
print('') # spacer

# menu prompt
# create prompt that displays choices
print("--------------------------------------------------")
print("| 1. Start New Session                           |")
print("| 2. Review Prior Sessions                       |")                  
print("| 3. Exit                                        |")
print("--------------------------------------------------")
menu_prompt = input("\nPlease enter a number from above to continue: ")
menu_prompt = int(menu_prompt)

while True:
  if menu_prompt == 1:
    print("\nSubject Archive")

  # subjects studies should be listed by numbers and subject i.e.
  # 1. Python
  # 2. JavaScript

  subj = input('\nWhat will you study? Enter corresponding number of subject from archive or enter a new subject. (Enter "quit" to exit) \n') # query user for subject and duration (need to incorporate way to access prior study sessions to continue)
  if subj == "quit" : 
    print("Winners don't quit.")
    break
  else:
    print("\nTimer Type\n1. Countdown\n2. Stopwatch\n")
  time_query = input("Enter number of desired timing method: ")
  time_query = int(time_query)
  if time_query == 1:
    t = input('What is the duration of this session? Enter in minutes: ')
    t = int(t)
    countdown(t)
# t = t * 60
    
  
  elif menu_prompt == 2:
    print('\nOkay, review past sessions.')

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
print(session)
data = str(session)
study_data.write(data)

# at end of session prompt user to either (close program, view study archive, restart session)