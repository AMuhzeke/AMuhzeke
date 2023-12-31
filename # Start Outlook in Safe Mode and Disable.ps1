# Start Outlook in Safe Mode and Disable Add-ins

# Define the Outlook executable path (modify if necessary)
$OutlookPath = "C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE"

try {
    # Check if the Outlook executable path exists
    if (Test-Path $OutlookPath) {
        # Build the command to start Outlook in safe mode
        $Command = "$OutlookPath /safe"

        # Start Outlook in safe mode
        Start-Process -FilePath $OutlookPath -ArgumentList "/safe" -NoNewWindow -Wait

        Write-Host "Outlook started in safe mode."
    } else {
        Write-Host "Outlook executable not found. Please update the OutlookPath variable with the correct path."
    }
} catch {
    Write-Host "An error occurred: $_"
}
