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

def generate_html_contribution_report(contributions, output_path="contribution_report.html"):
    # HTML row template for each contributor's data
    row_template = "<tr><td>{author}</td><td>{commits}</td><td>{lines_added}</td><td>{lines_removed}</td></tr>"
    
    # Generate HTML rows from the contribution data
    contribution_rows = [
        row_template.format(author=author, **data)
        for author, data in contributions.items()
    ]
    contribution_rows_html = "\n            ".join(contribution_rows)
    
    # Complete HTML template with a placeholder for the contribution rows
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Git Contribution Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ text-align: left; padding: 8px; border-bottom: 1px solid #ddd; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h2>Git Contribution Report</h2>
    <table>
        <thead>
            <tr>
                <th>Author</th>
                <th>Commits</th>
                <th>Lines Added</th>
                <th>Lines Removed</th>
            </tr>
        </thead>
        <tbody>
            {contribution_rows}
        </tbody>
    </table>
</body>
</html>"""
    
    # Insert the generated rows into the HTML template
    report_html = html_template.format(contribution_rows=contribution_rows_html)
    
    # Write the HTML content to the specified file
    with open(output_path, 'w') as file:
        file.write(report_html)
    
    print(f"Report generated: {output_path}")
