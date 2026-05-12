"""
Git repository management functions.
"""

import os

from dotenv import load_dotenv
from git import Repo


load_dotenv()

GIT_REPO_URL = os.getenv("GIT_REPO_URL")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GIT_BRANCH = os.getenv("GIT_BRANCH")


def git_commit_backup_changes(
    repo_path: str,
    commit_message: str,
) -> None:
    """
    Commit and push backup changes to GitHub.

    Args:
        repo_path (str):
            Local Git repository path.

        commit_message (str):
            Git commit message.

    Returns:
        None
    """

    repo = Repo(repo_path)

    #
    # ADD FILES
    #

    repo.git.add(all=True)

    #
    # COMMIT
    #

    if repo.is_dirty(untracked_files=True):

        repo.index.commit(commit_message)

        print(
            f"Git commit completed: "
            f"{commit_message}"
        )

    else:

        print("No Git changes detected.")

    #
    # CONFIGURE REMOTE
    #

    remote_url = (
        GIT_REPO_URL.replace(
            "https://",
            f"https://{GITHUB_TOKEN}@",
        )
    )

    if "origin" not in [
        remote.name for remote in repo.remotes
    ]:

        repo.create_remote(
            "origin",
            remote_url,
        )

    #
    # PUSH
    #

    origin = repo.remote(name="origin")

    origin.push(
        refspec=f"{GIT_BRANCH}:{GIT_BRANCH}"
    )

    print("Git push completed.")