import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_insight(commit_logs, analysis_report):
    prompt = f"Summarize the following Git commit logs and code analysis report:\n\n{commit_logs}\n\n{analysis_report}"
    response = openai.ChatCompletion.create(
        model="gpt-4-0125-preview",  # Adjust the model as necessary. Note: "gpt-4-0125-preview" might not be directly available in the updated API, so using "gpt-3.5-turbo" as a placeholder.
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=2048,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].message.content
