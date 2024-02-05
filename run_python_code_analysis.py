import subprocess

def run_python_code_analysis(directory):
    result = subprocess.run(['flake8', directory], capture_output=True, text=True)
    if result.stdout:
        return "Code Analysis Report:\n" + result.stdout
    else:
        return "No issues found."
