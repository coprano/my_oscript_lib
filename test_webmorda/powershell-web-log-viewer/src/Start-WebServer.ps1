# Start-WebServer.ps1

# Define the port and log directory
$port = 8080
$logDirectory = "C:/Program files/agent/script_logs"

function Get-LogFilesHtml {
    param (
        [string]$logDirectory
    )
    $files = Get-ChildItem -Path $logDirectory -File | Sort-Object LastWriteTime -Descending
    $rows = foreach ($file in $files) {
        $name = [System.Web.HttpUtility]::UrlEncode($file.Name)
        "<tr><td><a href='/$name'>$($file.Name)</a></td><td>$($file.LastWriteTime)</td><td>$([Math]::Round($file.Length/1KB,2)) KB</td></tr>"
    }
    $html = @"
    <html>
    <head>
        <title>Log Files</title>
        <meta charset='utf-8'>
        <style>
            body { font-family: Arial; margin: 2em; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ccc; padding: 8px; }
            th { background: #eee; }
        </style>
    </head>
    <body>
        <h2>Log Files</h2>
        <table>
            <tr><th>File Name</th><th>Last Modified</th><th>Size</th></tr>
            $($rows -join "`n")
        </table>
    </body>
    </html>
"@
    return $html
}

function Start-WebServer {
    param (
        [int]$port,
        [string]$logDirectory
    )
    $listener = [System.Net.HttpListener]::new()
    $listener.Prefixes.Add("http://*:$port/")
    $listener.Start()
    Write-Host "Listening on port $port..."
    while ($true) {
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response
        $path = $request.Url.AbsolutePath.TrimStart('/')
        if ($path -eq '') {
            # Главная страница со списком файлов
            $html = Get-LogFilesHtml -logDirectory $logDirectory
            $bytes = [System.Text.Encoding]::UTF8.GetBytes($html)
            $response.ContentType = "text/html; charset=utf-8"
            $response.ContentLength64 = $bytes.Length
            $response.OutputStream.Write($bytes, 0, $bytes.Length)
        } else {
            $logFileName = [System.Web.HttpUtility]::UrlDecode($path)
            $logFilePath = Join-Path -Path $logDirectory -ChildPath $logFileName
            if (Test-Path $logFilePath) {
                $logContents = Get-Content -Path $logFilePath -Raw
                $bytes = [System.Text.Encoding]::UTF8.GetBytes($logContents)
                $response.ContentType = "text/plain; charset=utf-8"
                $response.ContentLength64 = $bytes.Length
                $response.OutputStream.Write($bytes, 0, $bytes.Length)
            } else {
                $response.StatusCode = 404
                $response.StatusDescription = "File Not Found"
            }
        }
        $response.Close()
    }
}

Start-WebServer -port $port -logDirectory $logDirectory
