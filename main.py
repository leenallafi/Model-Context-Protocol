import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import modules/functions from src
from src.Authentication import g, token, auth
from src.Repository import create_file_in_repository, update_file_in_repository
from src.pullrequest import create_pull_request, get_pull_requests_by_query, add_and_modify_pull_request_comment
from src.branch import (
    get_list_of_branches, get_branch, get_branch_protection
)
from src.commit import Get_commit_date
from src.Issue import create_comment_on_issue, create_issue_with_body
from src.Milestone import get_milestone

# Validate GitHub Authentication
if not g or not token or not auth:
    raise ValueError("GitHub authentication not properly initialized.")

# access repository
repo = g.get_repo("leenallafi/model-context-protocol")
print(f"Repository: {repo.full_name}")

# print list of branches
print("Branches:", [b.name for b in repo.get_branches()])

# create a new file in the repository
create_file_in_repository(repo, "new_file.txt", "Hello, World!", "main")

# Update the file created above
update_file_in_repository(repo, "new_file.txt", "Updated content", "main")

# get list of branches and branch info
print("Branches List:", get_list_of_branches(repo))
print("Main Branch Info:", get_branch(repo, "main"))
print("Main Branch Protection:", get_branch_protection(repo, "main"))

# --- Example: Get commit date ---
Get_commit_date(repo, "main")

# Comment on Issue
create_comment_on_issue(repo, 1, "This is a test comment.")
# Create an issue with body
create_issue_with_body(repo, "New Issue with Body", "This is the body of the new issue.")

# Milestone Example
get_milestone(repo, 1)


