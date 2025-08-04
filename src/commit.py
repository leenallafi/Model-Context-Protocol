from src.Authentication import g ,token, auth
from typing import Optional
from github import Github
import os


# Function to create a commit status check
def create_commit_status_check(repo_name: str, branch_name: str, context: str) -> Optional[dict]:
    try:
        # Get repository
        repo = g.get_repo(repo_name)

        # Get the latest commit SHA from the branch
        branch = repo.get_branch(branch_name)
        sha = branch.commit.sha

        # Create the status
        status = repo.get_commit(sha=sha).create_status(
            state="pending",  # Can be 'error', 'failure', 'pending', or 'success'
            target_url="https://FooCI.com",  # Link to your CI/CD or logs
            description="FooCI is building",
            context=context  # Use the provided context
        )

        print(f"Status created for commit {sha} on {branch_name}: {status.state}")
        return status.raw_data

    except Exception as e:
        print(f"Error creating commit status check: {e}")
        return None

# Example usage
create_commit_status_check("leenallafi/model-context-protocol", "main", "ci/check-name")

def Get_commit_date(repo_name: str, branch_name: str) -> Optional[str]:
    try:
        # Get repository
        repo = g.get_repo(repo_name)

        # Get the latest commit from the branch
        branch = repo.get_branch(branch_name)
        commit_date = branch.commit.commit.author.date

        print(f"Latest commit date on {branch_name}: {commit_date}")
        return commit_date.isoformat()

    except Exception as e:
        print(f"Error getting commit date: {e}")
        return None
# Example usage
Get_commit_date("leenallafi/model-context-protocol", "main")