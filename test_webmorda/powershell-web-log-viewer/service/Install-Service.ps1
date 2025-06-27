# Install-Service.ps1

# This script installs the web server script as a Windows service.

$serviceName = "PowerShellWebLogViewer"
$serviceDisplayName = "PowerShell Web Log Viewer Service"
$serviceDescription = "A service that runs a PowerShell web server to serve log files."

# Path to the web server script
$webServerScriptPath = "C:\path\to\your\powershell-web-log-viewer\src\Start-WebServer.ps1"

# Check if the service already exists
if (Get-Service -Name $serviceName -ErrorAction SilentlyContinue) {
    Write-Host "Service '$serviceName' already exists. Exiting."
    exit
}

# Create the service
New-Service -Name $serviceName -DisplayName $serviceDisplayName -Description $serviceDescription -BinaryPathName "powershell.exe -NoProfile -ExecutionPolicy Bypass -File `"$webServerScriptPath`"" -StartupType Automatic

# Start the service
Start-Service -Name $serviceName

Write-Host "Service '$serviceDisplayName' installed and started successfully."