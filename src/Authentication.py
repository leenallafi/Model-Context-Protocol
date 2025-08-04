from github import Auth, Github, GithubIntegration
from dotenv import load_dotenv
import os   

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
if not token:
    raise ValueError("GITHUB_TOKEN environment variable not set")

auth = Auth.Token(token)
g = Github(auth=auth)

user = g.get_user()
print(f"Authenticated as: {user.login}")
