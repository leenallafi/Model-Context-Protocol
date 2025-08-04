from src.Authentication import g


# Function to get the current authenticated user
def get_current_user():
    user = g.get_user()
    return print(f"Authenticated as: {user.login}")

# Call the function to display the current user
get_current_user()

# Function to get user by name
def get_user_by_name(username):
    user = g.get_user(username)
    return print(f"User found: {user.login}")

# Example usage of get_user_by_name
get_user_by_name("Leen")  # Replace "Leen" with the desired username

# Function to get organization by name
def get_organization_by_name(organization_name):
    org = g.get_organization(organization_name)
    return print(f"Organization found: {org.login}")

# Example usage of get_organization_by_name
get_organization_by_name("LH23-AI")  # Replace "LH23-AI" with the desired organization name

# Function to search repositories by language

def search_repositories_by_language(language):
    repos = g.search_repositories(query=f'language:{language}', sort='stars', order='desc')
    return print(f"Repositories found for language {language}: {[repo.name for repo in repos]}")

# Example usage of search_repositories_by_language
search_repositories_by_language("Python")  # Replace "Python" with the desired programming language
# Function to search repositories by issues

def search_repositories_by_issues():
    repos = g.search_repositories(query='good-first-issue', sort='stars', order='desc')
    return print(f"Repositories found with good first issue: {[repo.name for repo in repos]}")
# Example usage of search_repositories_by_issues
search_repositories_by_issues()  # This will search for repositories with 'good-first-