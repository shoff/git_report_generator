import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_insight(commit_logs, analysis_report):
    prompt = f"Let's delve into the insights gleaned from our recent developments. Below, you'll find a concise summary of the pivotal changes captured in our Git commit logs, alongside a comprehensive analysis of our code's current state. These findings not only reflect our progress but also spotlight areas ripe for improvement. Please review: Git Commit Logs: {commit_logs} Code Analysis Report: {analysis_report} Your expertise and feedback are invaluable as we refine our approach and forge ahead. Outline what each commiter has commited to the project."
    # prompt = f"Summarize the following Git commit logs and code analysis report:\n\n{commit_logs}\n\n{analysis_report}"
    response = openai.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

