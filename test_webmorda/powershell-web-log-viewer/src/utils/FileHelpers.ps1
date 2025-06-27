function Get-LogFileContents {
    param (
        [string]$logDirectory
    )

    if (-Not (Test-Path $logDirectory)) {
        throw "The specified log directory does not exist: $logDirectory"
    }

    $logFiles = Get-ChildItem -Path $logDirectory -Filter *.txt

    if ($logFiles.Count -eq 0) {
        return "No log files found in the specified directory."
    }

    $logContents = @()

    foreach ($logFile in $logFiles) {
        $content = Get-Content -Path $logFile.FullName -ErrorAction Stop
        $logContents += @{
            FileName = $logFile.Name
            Content  = $content
        }
    }

    return $logContents
}

function Get-LogFileNames {
    param (
        [string]$logDirectory
    )

    if (-Not (Test-Path $logDirectory)) {
        throw "The specified log directory does not exist: $logDirectory"
    }

    $logFiles = Get-ChildItem -Path $logDirectory -Filter *.txt

    return $logFiles.Name
}