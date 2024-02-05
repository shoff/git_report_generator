def generate_html_report(commit_logs, analysis_report, ai_insights, base_name):
    # Enhanced HTML template with updated styling
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Git Analysis Report {base_name}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
            color: #333;
        }}
        .container {{
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        .section {{
            margin-bottom: 40px;
        }}
        .section-title {{
            font-size: 28px;
            color: #007BFF;
            margin-bottom: 10px;
            border-bottom: 2px solid #007BFF;
            padding-bottom: 6px;
        }}
        .content {{
            font-size: 16px;
            line-height: 1.6;
            margin-top: 10px;
        }}
        /* Responsive typography */
        @media (max-width: 600px) {{
            .section-title {{
                font-size: 24px;
            }}
            .content {{
                font-size: 14px;
            }}
        }}
    </style>
    </head>
    <body>
    <div class="container">
        <div class="section">
            <div class="section-title">Git Log Summary</div>
            <div class="content">{git_logs}</div>
        </div>
        <div class="section">
            <div class="section-title">AI Analysis Insights</div>
            <div class="content">{ai_insights}</div>
        </div>
        <!-- Additional sections as needed -->
    </div>
    </body>
    </html>
    """
    
    # Insert actual content into the HTML template
    html_content = html_template.format(
                                        base_name=base_name if base_name is not None else "",
                                        git_logs=commit_logs.replace('\n', '<br>'),
                                        ai_insights=ai_insights.replace('\n', '<br>'))
    return html_content