
![Alt text](<2023-08-31 09_57_39-Command Prompt.png>)

Greetings
--------------------

Beryl delivers your PE (exe or dll) straight to the victim in form of a game or a no gui 



persistance feature:
---------------------
it use the task schedualer to make a the PE run at logon ,also the PE will run with the highest privilege available at each startup(SYSTEM or Nt/AUthority System)

ps: tried this with an AgentTesla trojan PE and it worked fine

tested on windows 10 and 11

Setup:

pip install -r requirements.txt 

Python Beryl.py

usage: Beryl.py [-h] 
------------

-d DIRECTORY_PATH (in the HOME env of the user)

-url "URL" (url to install your PE)

-n OUTPUT_NAME 

[-g {Snake,FlapyBird,Turtle,RaceCar}] (GUI)

-dll "function" (name of function to run with the dll file)

-uac makes Beryl run as Uac by default (if UAC and  user  doesn t execute as admin payload won t be injected won't run)

To Do :
---------------

add some obfuscation , shellcode support ...

DISCLAIMER :
--------------

ME The author takes NO responsibility and/or liability for how you choose to use any of the tools/source code/any files provided. ME The author and anyone affiliated with will not be liable for any losses and/or damages in connection with use of Beryl. By using Beryl or any files included, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again Beryl is for EDUCATION and/or RESEARCH purposes ONLY.