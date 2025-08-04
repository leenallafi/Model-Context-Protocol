from typing import Optional
from src.Authentication import g ,token, auth

import time
# Function to create a branch if it does not exist and add a file to it
def create_branch_if_not_exists(repo, branch_name: str, base_branch: str = "main") -> None:
    """
    Create a branch if it does not exist.
    """
    try:
        repo.get_branch(branch_name)
        print(f"Branch '{branch_name}' already exists.")
    except Exception:
        base_ref = repo.get_git_ref(f"heads/{base_branch}")
        repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=base_ref.object.sha)
        print(f"Created new branch '{branch_name}' from '{base_branch}'.")
# Function to add a file to a branch or update it if it already exists
def add_file_to_branch(repo, branch_name: str, file_path: str, content: str) -> None:
    """
    Add a new file or update an existing file on the specified branch.
    """
    try:
        contents = repo.get_contents(file_path, ref=branch_name)
        repo.update_file(
            path=contents.path,
            message=f"Update {file_path}",
            content=content,
            sha=contents.sha,
            branch=branch_name
        )
        print(f"Updated file '{file_path}' on branch '{branch_name}'.")
    except Exception:
        repo.create_file(
            path=file_path,
            message=f"Add {file_path}",
            content=content,
            branch=branch_name
        )
        print(f"Added file '{file_path}' to branch '{branch_name}'.")
# Function to create a Pull Request from a unique branch
def create_pull_request(
    repo_name: str,
    title: str,
    body: str,
    base: str = "main",
    feature_prefix: str = "feature-branch"
) -> Optional[dict]:
    """
    Create a Pull Request from a unique branch to avoid duplicate PR errors.
    """
    try:
        repo = g.get_repo(repo_name)

        # Generate a unique branch name with timestamp
        timestamp = int(time.time())
        head = f"{feature_prefix}-{timestamp}"

        create_branch_if_not_exists(repo, head, base)
        add_file_to_branch(repo, head, "new_file_in_feature.txt", "This is a test file for the PR.")
        pr = repo.create_pull(base=base, head=head, title=title, body=body)
        print(f"Created Pull Request: {pr.title} (#{pr.number}) - {pr.html_url}")
        return pr
    except Exception as e:
        print(f"Error creating Pull Request in repository {repo_name}: {e}")
        return None
# Function to get pull requests by query
def get_pull_requests_by_query(repo_name: str) -> None:
    """
    List all open Pull Requests targeting the main branch.
    """
    try:
        repo = g.get_repo(repo_name)
        print(f"Pull requests in {repo_name}:")
        pulls = repo.get_pulls(state='open', sort='created', base='main')
        for pr in pulls:
            print(f"#{pr.number} - {pr.title} ({pr.html_url})")
    except Exception as e:
        print(f"Error fetching pull requests for {repo_name}: {e}")

# Function to add or modify a comment on a pull request

def add_and_modify_pull_request_comment(repo_name: str, pull_number: int, comment_body: str, unique_marker: str) -> None:
    """
    Add a new comment or update existing comment on a pull request identified by unique_marker.

    :param repo_name: Repository full name 'owner/repo'.
    :param pull_number: Pull request number.
    :param comment_body: The body text to add/update.
    :param unique_marker: A unique string to identify the comment (e.g. '## Automated Comment').
    """
    try:
        repo = g.get_repo(repo_name)
        pr = repo.get_pull(pull_number)
        comments = pr.get_issue_comments()

        comment_to_update = None
        for comment in comments:
            if unique_marker in comment.body:
                comment_to_update = comment
                break

        if comment_to_update:
            comment_to_update.edit(comment_body)
            print(f"Updated comment on PR #{pull_number}.")
        else:
            pr.create_issue_comment(comment_body)
            print(f"Added new comment to PR #{pull_number}.")

    except Exception as e:
        print(f"Error managing comments on PR #{pull_number} in {repo_name}: {e}")

repo = "leenallafi/model-context-protocol"

pr = create_pull_request(
    repo,
    "New Pull Request",
    "This PR adds a test file to demonstrate automatic PR creation with unique branch."
)

if pr:
    add_and_modify_pull_request_comment(
        repo_name=repo,
        pull_number=pr.number,
        comment_body="## Automated Comment\nThis is an automated comment on this PR.",
        unique_marker="## Automated Comment"
    )

get_pull_requests_by_query(repo)

