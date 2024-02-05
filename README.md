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
The script can be customized using command-line arguments to specify the Git repository, the directory to analyze, the directory to store the report, and the base solution directory.

Here is an example of how to use command-line arguments:
```
Here is an example of how to use command-line arguments:
```

Replace `<repository_path>` with the path of the Git repository you want to analyze.
Replace `<repo_directory>` with the directory you want to analyze.
Replace `<report_directory>` with the directory where you want to store the report.
Replace `<base_name>` with the base solution directory.

If you don't provide these arguments, the script will use the current working directory `(os.getcwd())` as the default value for `repository_path`, `repo_directory`, and `base_name`, and it will store the reports in a "`reports`" subdirectory in the current working directory for `report_directory`.


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