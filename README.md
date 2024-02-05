# Git Analysis Application

## Overview
This application provides tools for analyzing Git repositories, including reading Git logs, generating insights, analyzing Python code, and generating HTML reports.

## Features
- **Read Git Logs**: Parses Git log data for further analysis.
- **Generate Insights**: Processes data to generate insights about the Git repository.
- **Analyze Python Code**: Runs analysis on Python code to assess quality, complexity, or other metrics.
- **Generate HTML Report**: Summarizes the insights and analysis results into an HTML report.

## TODO
- **CSharp Code Analysis**: Add support for analyzing C# code.

## Requirements
To run this application, you need Python 3.x and the packages listed in `requirements.txt`.

## Setup
1. Clone the repository or download the source code.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the `main.py` script:
```
python main.py
```
Adjust the script or use command-line arguments (if implemented) to specify the Git repository or log files to analyze.

## Files Description
- `generate_html_report.py`: Generates HTML reports from data.
- `generate_insight.py`: Generates insights from the analyzed data.
- `main.py`: The main entry point for the application.
- `read_git_logs.py`: Reads and processes Git log data.
- `run_python_code_analysis.py`: Analyzes Python code.
- `requirements.txt`: Lists the project dependencies.

## Contribution
Feel free to contribute to the project by submitting pull requests or reporting issues.

## License
Specify the license under which this application is released, e.g., MIT, GPL, etc.