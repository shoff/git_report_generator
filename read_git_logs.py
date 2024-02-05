import git

def read_git_logs(repo_path):
    repo = git.Repo(repo_path)
    commits = []
    for commit in repo.iter_commits():
        commit_info = f'Commit: {commit.hexsha}\nAuthor: {commit.author.name}\nDate: {commit.authored_datetime}\nMessage: {commit.message}\n' + '-' * 40
        commits.append(commit_info)
    return '\n'.join(commits)
