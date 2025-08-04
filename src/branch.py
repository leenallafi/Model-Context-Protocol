from src.Authentication import g ,token, auth
from typing import Optional

# Function to get a list of branches for a repository
def get_list_of_branches(repo_name: str) -> Optional[list[str]]:
    """
    Get a list of branches for a repository by name.
    """
    try:
        repo = g.get_repo(repo_name)
        branches = [branch.name for branch in repo.get_branches()] if repo else None
        print(f"Branches for repository {repo_name}: {branches}")
        return branches
    except Exception as e:
        print(f"Error fetching branches for repository {repo_name}: {e}")
        return None
# Example usage of get_list_of_branches
get_list_of_branches("leenallafi/model-context-protocol")  # Replace with the desired repository name

# Function to get a specific branch for a repository by name
def get_branch(repo_name: str, branch_name: str) -> Optional[str]:
    """
    Get a specific branch for a repository by name.
    """
    try:
        repo = g.get_repo(repo_name)
        branch = repo.get_branch(branch_name) if repo else None
        print(f"Branch for repository {repo_name}: {branch}")
        return branch
    except Exception as e:
        print(f"Error fetching branch for repository {repo_name}: {e}")
        return None
    
# Example usage of get_branch
get_branch("leenallafi/model-context-protocol", "main")  # Replace with the` desired repository and branch name

# Function to get protection status of a branch
def get_branch_protection(repo_name: str, branch_name: str) -> Optional[dict]:
    """
    Get the protection status of a branch for a repository by name.
    """
    try:
        repo = g.get_repo(repo_name)
        branch = repo.get_branch(branch_name) if repo else None
        protection = branch.protected if branch else None
        print(f"Protection status for branch {branch_name} in repository {repo_name}: {protection}")
        return protection
    except Exception as e:
        print(f"Error fetching protection status for branch {branch_name} in repository {repo_name}: {e}")
        return None

# Example usage of get_branch_protection
get_branch_protection("leenallafi/model-context-protocol", "main")  # Replace with the desired repository and branch name
