# Start-WebServer.ps1

# Define the port and log directory
$port = 8080
$logDirectory = "C:\path\to\your\logs"

# Function to handle HTTP requests
function Start-WebServer {
    param (
        [int]$port,
        [string]$logDirectory
    )

    # Create a listener for incoming HTTP requests
    $listener = [System.Net.HttpListener]::new()
    $listener.Prefixes.Add("http://*:$port/")
    $listener.Start()
    Write-Host "Listening on port $port..."

    while ($true) {
        # Wait for an incoming request
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response

        # Get the requested log file name from the URL
        $logFileName = $request.Url.AbsolutePath.TrimStart('/')
        $logFilePath = Join-Path -Path $logDirectory -ChildPath $logFileName

        if (Test-Path $logFilePath) {
            # Read the contents of the log file
            $logContents = Get-Content -Path $logFilePath -Raw
            $response.ContentType = "text/plain"
            $response.ContentLength64 = $logContents.Length
            $response.OutputStream.Write([System.Text.Encoding]::UTF8.GetBytes($logContents), 0, $logContents.Length)
        } else {
            # Return a 404 response if the log file does not exist
            $response.StatusCode = 404
            $response.StatusDescription = "File Not Found"
        }

        # Close the response
        $response.Close()
    }
}

# Start the web server
Start-WebServer -port $port -logDirectory $logDirectory