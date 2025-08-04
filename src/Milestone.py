from src.Authentication import g ,token, auth

from typing import Optional


def get_milestone_list(repo_name: str) -> Optional[list]:
    """
    Get a list of open milestones for a repository by name.
    """
    try:
        repo = g.get_repo(repo_name)
        milestones = repo.get_milestones(state='open') if repo else None
        print(f"Open milestones for repository {repo_name}: {milestones}")
        return milestones
    except Exception as e:
        print(f"Error fetching milestones for repository {repo_name}: {e}")
        return None
    # Example usage of get_milestone_list
get_milestone_list("leenallafi/model-context-protocol")  # Replace with the desired repository name

def create_milestone(repo_name: str, title: str, description: Optional[str] = None) -> Optional[dict]:
    """
    Create a new milestone for a repository by name.
    """
    try:
        repo = g.get_repo(repo_name)
        milestone = repo.create_milestone(title=title, description=description) if repo else None
        print(f"Created milestone in repository {repo_name}: {milestone}")
        return milestone
    except Exception as e:
        print(f"Error creating milestone in repository {repo_name}: {e}")
        return None
# Example usage of create_milestone
#create_milestone("leenallafi/model-context-protocol", "New Milestone", "This is a new milestone description.")  # Replace with the desired repository name and milestone details


def get_milestone(repo_name: str, milestone_number: int) -> Optional[dict]:
    """
    Get a specific milestone for a repository by name and milestone number.
    """
    try:
        repo = g.get_repo(repo_name)
        milestone = repo.get_milestone(milestone_number) if repo else None
        print(f"Milestone {milestone_number} for repository {repo_name}: {milestone}")
        return milestone
    except Exception as e:
        print(f"Error fetching milestone {milestone_number} for repository {repo_name}: {e}")
        return None
# Example usage of get_milestone
get_milestone("leenallafi/model-context-protocol", 1)  # Replace with the desired repository name and milestone number
 

