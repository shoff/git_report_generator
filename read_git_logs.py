import git
from textblob import TextBlob

def analyze_commit_message_sentiment(commit_message):
    analysis = TextBlob(commit_message)
    return {
        "polarity": analysis.sentiment.polarity,
        "subjectivity": analysis.sentiment.subjectivity
    }

def read_git_logs(repo_path):
    repo = git.Repo(repo_path)
    commits = []
    for commit in repo.iter_commits():
        sentiment = analyze_commit_message_sentiment(commit.message)
        commit_info = (
            f'Commit: {commit.hexsha}\n'
            f'Author: {commit.author.name}\n'
            f'Date: {commit.authored_datetime}\n'
            f'Message: {commit.message}\n'
            f'Sentiment: Polarity={sentiment["polarity"]}, Subjectivity={sentiment["subjectivity"]}\n'
            + '-' * 40
        )
        commits.append(commit_info)
    return '\n'.join(commits)

def analyze_contributions(repo_path):
    repo = git.Repo(repo_path)
    contributions = {}

    for commit in repo.iter_commits():
        author = commit.author.name
        if author not in contributions:
            contributions[author] = {'commits': 0, 'lines_added': 0, 'lines_removed': 0}

        contributions[author]['commits'] += 1

        # Calculate lines added/removed using diffs
        try:
            # Check if the commit has parents to diff against; if not, treat as initial commit
            if commit.parents:
                diff = commit.diff(commit.parents[0], create_patch=True)
            else:
                diff = commit.diff(None, create_patch=True)
                
            for d in diff:
                contributions[author]['lines_added'] += d.stats['insertions']
                contributions[author]['lines_removed'] += d.stats['deletions']
        except Exception as e:
            print(f"Error processing commit {commit.hexsha}: {e}")

    return contributions
