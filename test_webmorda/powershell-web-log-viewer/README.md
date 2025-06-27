# PowerShell Web Log Viewer

## Overview
The PowerShell Web Log Viewer is a simple web server application that allows users to view log files in a web browser. It serves log files stored in a specified directory and provides an easy way to access and read log contents without needing to open them directly on the file system.

## Features
- Start a lightweight web server using PowerShell.
- Serve `.txt` log files from a designated directory.
- Access log files through a web interface from any browser.

## Project Structure
```
powershell-web-log-viewer
├── src
│   ├── Start-WebServer.ps1       # Main script to start the web server
│   └── utils
│       └── FileHelpers.ps1        # Utility functions for file operations
├── service
│   └── Install-Service.ps1        # Script to install the web server as a Windows service
├── logs
│   └── README.md                  # Documentation about log files
├── config
│   └── settings.ps1               # Configuration settings for the web server
└── README.md                      # Project overview and usage instructions
```

## Setup Instructions
1. **Clone the Repository**
   Clone the repository to your local machine using Git or download it as a ZIP file.

2. **Configure Settings**
   Open the `config/settings.ps1` file and configure the necessary settings, such as the port number and the directory where your log files are stored.

3. **Install the Service**
   Run the `service/Install-Service.ps1` script to install the web server as a Windows service. This will allow the server to run in the background and start automatically on system boot.

4. **Start the Web Server**
   Execute the `src/Start-WebServer.ps1` script to start the web server. You can access the web interface by navigating to `http://localhost:<port>` in your web browser, replacing `<port>` with the port number you configured.

## Usage
Once the web server is running, you can view the contents of your log files by navigating to the appropriate URL in your web browser. The server will list all available log files in the specified directory, and you can click on any file to view its contents.

## Log File Format
Log files should be in plain text format (`.txt`). Ensure that the log files are placed in the directory specified in the `config/settings.ps1` file for them to be accessible via the web interface.

## License
This project is open-source and available for modification and distribution under the terms of the MIT License.