$logFile = "C:\SRSBot\watcher_log.txt"
Add-Content -Path $logFile -Value "Watcher started at $(Get-Date)"

while ($true) {
    try {
        if (Test-Path "C:\SRSBot\trigger.txt") {
            Add-Content -Path $logFile -Value "trigger.txt detected at $(Get-Date)"
             Remove-Item "C:\SRSBot\trigger.txt"
             Add-Content -Path $logFile -Value "trigger.txt removed at $(Get-Date)"

             Start-Sleep -Seconds 1

            # Start listener.bat
            Start-Process -FilePath "cmd.exe" -ArgumentList "/c C:\SRSBot\listener.bat"
            Add-Content -Path $logFile -Value "listener.bat triggered at $(Get-Date)"
        }
    } catch {
        Add-Content -Path $logFile -Value "Error: $_"
    }
    Start-Sleep -Seconds 20
}
