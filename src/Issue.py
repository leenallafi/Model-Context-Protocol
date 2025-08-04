from src.Authentication import g  # Assuming 'g' is our authenticated Github object
from typing import Optional

# Function to get the creation date of a specific issue
def get_issue_date(repo_name: str, issue_number: int) -> Optional[str]:
    """
    Get the creation date of a specific issue in a repository.
    
    :param repo_name: The name of the repository in the format 'owner/repo'.
    :param issue_number: The issue number to fetch.
    :return: The creation date of the issue as a string, or None if not found.
    """
    try:
        repo = g.get_repo(repo_name)
        issue = repo.get_issue(number=issue_number)
        return str(issue.created_at)  # Return as string for readability
    except Exception as e:
        print(f"Error getting issue date for {repo_name} issue #{issue_number}: {e}")
        return None

# Example usage
print(get_issue_date("leenallafi/model-context-protocol", 1))


def create_comment_on_issue(repo_name: str, issue_number: int, comment: str):
    """
    Create a comment on a specific issue in a repository.

    :param repo_name: The name of the repository in the format 'owner/repo'.
    :param issue_number: The issue number to comment on.
    :param comment: The comment text to add.
    """
    try:
        repo = g.get_repo(repo_name)
        issue = repo.get_issue(number=issue_number)
        issue.create_comment(comment)
        print(f"Comment created on {repo_name} issue #{issue_number}: {comment}")
    except Exception as e:
        print(f"Error creating comment on {repo_name} issue #{issue_number}: {e}")

# Example usage
create_comment_on_issue("leenallafi/model-context-protocol", 1, "This is    a test comment.")
# Function to create a new issue in a repository
def create_issue(repo_name: str, title: str):
    """
    Create a new issue in a repository.

    :param repo_name: The name of the repository in the format 'owner/repo'.
    :param title: The title of the issue to create.
    """
    try:
        repo = g.get_repo(repo_name)
        issue = repo.create_issue(title=title)
        print(f"Issue created in {repo_name}: {issue.title} (#{issue.number})")
    except Exception as e:
        print(f"Error creating issue in {repo_name}: {e}")
# Example usage
create_issue("leenallafi/model-context-protocol", "New Issue Title")

def create_issue_with_body(repo_name: str, title: str, body: str):
    """
    Create a new issue in a repository with a body.

    :param repo_name: The name of the repository in the format 'owner/repo'.
    :param title: The title of the issue to create.
    :param body: The body content of the issue.
    """
    try:
        repo = g.get_repo(repo_name)
        issue = repo.create_issue(title=title, body=body)
        print(f"Issue created in {repo_name}: {issue.title} (#{issue.number})")
    except Exception as e:
        print(f"Error creating issue in {repo_name}: {e}")
# Example usage
create_issue_with_body("leenallafi/model-context-protocol", "New Issue with Body", "This is the body of the new issue.")

def create_issue_with_labels(repo_name: str, title: str, labels: list):
    """
    Create a new issue in a repository with specified labels.

    :param repo_name: The name of the repository in the format 'owner/repo'.
    :param title: The title of the issue to create.
    :param labels: A list of label names to apply to the issue.
    """
    try:
        repo = g.get_repo(repo_name)
        label_objects = [repo.get_label(label) for label in labels]
        issue = repo.create_issue(title=title, labels=label_objects)
        print(f"Issue created in {repo_name}: {issue.title} (#{issue.number})")
    except Exception as e:
        print(f"Error creating issue in {repo_name}: {e}")
# Example usage
create_issue_with_labels("leenallafi/model-context-protocol", "New Issue with Labels", ["bug", "enhancement"])