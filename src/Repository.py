from src.Authentication import g
from src.Authentication import auth
from typing import Optional
from src.Authentication import token

 # Function to get repository topics by name
def get_repository_topics(repo_name: str) -> Optional[list[str]]:
    """
    Get the topics for a repository by name.
    """
    try:
        repo = g.get_repo(repo_name)
        topics = repo.get_topics() if repo else None
        print(f"Topics for repository {repo_name}: {topics}")
    except Exception as e:
        print(f"Error fetching topics for repository {repo_name}: {e}")
        return None
# Example usage of get_repository_topics
get_repository_topics("PyGithub/PyGithub") # Replace "PyGithub/PyGithub" with the desired repository name

# Function to get repository stars by name
def get_repository_stars(repo_name: str) -> Optional[int]:
    """
    Get the star count for a repository by name.
    """
    try:
        repo = g.get_repo(repo_name)
        stars = repo.stargazers_count if repo else None
        print(f"Stars for repository {repo_name}: {stars}")
    except Exception as e:
        print(f"Error fetching stars for repository {repo_name}: {e}")
        return None

# Example usage of get_repository_stars
get_repository_stars("PyGithub/PyGithub") # Replace "PyGithub/PyGithub" with the desired repository name


def get_open_issues(repo_name: str) -> Optional[list[str]]:
    """
    Get a list of open issues for a repository by name.
    """
    try:
        repo = g.get_repo(repo_name)
        issues = repo.get_issues(state="open") if repo else None
        issue_titles = [issue.title for issue in issues] if issues else []
        print(f"Open issues for repository {repo_name}: {issue_titles}")
    except Exception as e:
        print(f"Error fetching open issues for repository {repo_name}: {e}")
        return None

# Example usage of get_open_issues
#get_open_issues("PyGithub/PyGithub") # Replace "PyGithub/PyGithub" with the desired repository name



# Function to create a new file in a repository
def create_file_in_repository(repo_name: str, file_path: str, content: str, branch: str) -> Optional[str]:
    """
    Create a new file in the repository.
    Returns the file URL if successful, otherwise None.
    """
    try:
        repo = g.get_repo(repo_name)

        # Check if file already exists
        existing_files = [f.path for f in repo.get_contents("")]
        if file_path in existing_files:
            print(f"File '{file_path}' already exists in {repo_name}")
            return None

        # Create new file
        result = repo.create_file(file_path, "Create new file", content, branch=branch)
        print(f"File created in repository {repo_name}: {file_path}")
        return result["content"].html_url

    except Exception as e:
        print(f"Error creating file in repository {repo_name}: {e}")
        return None

# Example usage of create_file_in_repository
create_file_in_repository("leenallafi/model-context-protocol", "new_file.txt", "Hello, World!", "main")

# Function to update an existing file in a repository
def update_file_in_repository(repo_name: str, file_path: str, content: str, branch: str) -> Optional[str]:
    """
    Update an existing file in the repository.
    Returns the file URL if successful, otherwise None.
    """
    try:
        repo = g.get_repo(repo_name)

        # Check if file exists
        existing_files = [f.path for f in repo.get_contents("")]
        if file_path not in existing_files:
            print(f"File '{file_path}' does not exist in {repo_name}")
            return None

        # Update existing file
        contents = repo.get_contents(file_path, ref=branch)
        result = repo.update_file(contents.path, "Update file", content,  contents.sha, branch=branch)
        print(f"File updated in repository {repo_name}: {file_path}")
        return result["content"].html_url

    except Exception as e:
        print(f"Error updating file in repository {repo_name}: {e}")
        return None
    
# Example usage of update_file_in_repository
update_file_in_repository("leenallafi/model-context-protocol", "new_file.txt", "Updated content", "main")

# Function to delete a file in a repository
def delete_file_in_repository(repo_name: str, file_path: str, branch: str) -> Optional[str]:
    """
    Delete a file in the repository.
    Returns the file URL if successful, otherwise None.
    """
    try:
        repo = g.get_repo(repo_name)

        # Check if file exists
        existing_files = [f.path for f in repo.get_contents("")]
        if file_path not in existing_files:
            print(f"File '{file_path}' does not exist in {repo_name}")
            return None

        # Delete file
        contents = repo.get_contents(file_path, ref=branch)
        result = repo.delete_file(contents.path, "Delete file", contents.sha, branch=branch)
        print(f"File deleted in repository {repo_name}: {file_path}")
        return result["content"]

    except Exception as e:
        print(f"Error deleting file in repository {repo_name}: {e}")
        return None

# Example usage of delete_file_in_repository
delete_file_in_repository("leenallafi/model-context-protocol", "new_file.txt", "main")
