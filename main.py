from server import mcp
import git
import os
if __name__ == '__main__':
    repo_path = 'sqlmap'
    repo_url = 'https://github.com/sqlmapproject/sqlmap.git'
    if os.path.exists(repo_path):
        repo = git.Repo(repo_path)
        origin = repo.remotes.origin
        origin.pull()
    else:
        git.Repo.clone_from(repo_url, repo_path)
    mcp.run(transport="streamable-http", host='0.0.0.0', port=5000)