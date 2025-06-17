from git import Repo, InvalidGitRepositoryError
import os

def git():
    try:
        if not os.path.exists(".git"):
            print("[INFO] Git repository not found. Skipping Git operations.")
            return  # Skip if not a Git repo

        repo = Repo()
        origin = repo.remotes.origin
        origin.fetch()
        # Only proceed if branch exists
        if config.UPSTREAM_BRANCH in origin.refs:
            repo.git.reset("--hard", f"origin/{config.UPSTREAM_BRANCH}")
        else:
            print(f"[WARNING] Branch {config.UPSTREAM_BRANCH} not found.")
    except InvalidGitRepositoryError:
        print("[ERROR] Invalid Git repository. Skipping Git operations.")
    except Exception as e:
        print(f"[ERROR] Git update failed: {e}")
