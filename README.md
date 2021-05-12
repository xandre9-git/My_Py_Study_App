My Py Study App Version 1.0
Release Date: 4/20/2021
Developed by Xandre9
---------------------------

Thank you for trying out my first Python project. This program is simply a study session tracker.

This app features a stopwatch and countdown timer to track your study sessions.
The countdown timer allows the input of desired minutes and begin counting down. The stopwatch option allows user to run an active timer with the pressing of the 'enter' key to start. A subsequent press of the enter key will cease the stopwatch. Both timer methods play a bell sound upon ending and record the alloted time of session to an external file for later retrieval.

New sessions can be created and later on accessed in the review section. This section allows a more detailed analysis of prior study sessions and provides the option of removing entries.


Requirements
--------------
Must install playsound module for sound to work: 'pip install playsound'
https://pypi.org/project/playsound/


Known Bugs 
-----------------
-Countdown timer will only accept integer values for input.

If you find any additional bugs please notify me.

Troubleshooting
----------------
Sound Not Playing
-If you have issues getting sound to play in terminal, this could assist.
1. in terminal type 'sudo nano /etc/modprobe.d/default.conf'
2. add a line with following code: 'options snd_hda_intel index=1'
3. save file, exit and reboot

Credits
--------

Temple sound file
Mike Koenig
https://soundbible.com/1531-Temple-Bell.html

Alarm

