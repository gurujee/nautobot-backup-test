"""
Git repository management functions.
"""

from git import Repo


def git_commit_backup_changes(
    repo_path: str,
    commit_message: str,
) -> None:
    """
    Commit backup file changes into Git repository.

    Args:
        repo_path (str):
            Local Git repository path.

        commit_message (str):
            Git commit message.

    Returns:
        None
    """

    repo = Repo(repo_path)

    repo.git.add(all=True)

    if repo.is_dirty(untracked_files=True):

        repo.index.commit(commit_message)

        print(
            f"Git commit completed: "
            f"{commit_message}"
        )

    else:

        print("No Git changes detected.")