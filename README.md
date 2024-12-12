# Session Monitor

## Overview
Session Manager is a system designed to manage and process user session logs efficiently. It integrates Python and Go to handle log data extraction, cleanup, and manipulation while generating meaningful outputs. The project utilizes system commands, file operations, and JSON serialization for seamless data processing.

## Features
- **Log User Activity**: Captures user session logs using the `last` command.
- **MAC Address Integration**: Associates each log with a unique MAC address identifier.
- **Data Cleanup**: Leverages a Go script for processing raw log data into a structured format.
- **JSON Conversion**: Parses processed data and converts it into JSON for easy consumption.
- **Automated Workflow**: Ensures smooth execution through integrated scripts and directory setup.

## Project Structure
```
SessionMonitor/
|-- applications/
   |-- probably look here 👀
|-- clientApp/
   |-- very many files 😏
|-- serverApp/
   |-- very many files again 😂
```

## Prerequisites
1. Python 3.x
2. Go programming language
3. `getmac` Python library: Install with `pip install getmac`
4. `pyinstaller` Python library: Install with `pip install pyinstaller` ps: for developers

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/onyango-granton/sessionMonitor.git
   cd SessionMonitor
   ```
2. Ensure the required dependencies are installed.

## Client Usage
1. Run the main Python script to start the session management process:
   ```bash
   cd applications
   unzip clientApp.zip
   cd clientApp
   ./clientMain
   ```
## Server Usage
1. Run the main Python script to start the session management process:
   ```bash
   cd applications
   unzip serverApp.zip
   cd serverApp
   ./serverMain
   ```

### Output
The final JSON output includes:
- The MAC address of the device.
- User session data from the cleaned log file.

## Example Output
```json
{
    "00:1A:2B:3C:4D:5E": "<processed log data>"
}
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "<commit message>"`.
4. Push to the branch: `git push origin feature-name`.
5. Create a pull request.

## License
This project is licensed under the [MIT](LICENSE) License. See the LICENSE file for details.

## Acknowledgments
- The `getmac` Python library for MAC address retrieval.
- System utilities like `last` for session logging.
- The Go programming language for efficient data manipulation.
