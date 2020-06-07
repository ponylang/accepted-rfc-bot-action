#!/usr/bin/python3

import git,json,os,sys
from github import Github

ENDC   = '\033[0m'
ERROR  = '\033[31m'
INFO   = '\033[34m'
NOTICE = '\033[33m'

if not 'API_CREDENTIALS' in os.environ:
  print(ERROR + "API_CREDENTIALS needs to be set in env. Exiting." + ENDC)
  sys.exit(1)

# login
github = Github(os.environ['API_CREDENTIALS'])

# get json data for our event
event_data = json.load(open(os.environ['GITHUB_EVENT_PATH'], 'r'))

# grab info needed to find PR
sha = event_data['head_commit']['id']
repo_name = event_data['repository']['full_name']

# find associated PR (if any)
print(INFO + "Finding PR associated with " + sha + " in " + repo_name + ENDC)
query = "q=is:merged+sha:" + sha + "+repo:" + repo_name
print(INFO + "Query: " + query + ENDC)
results = github.search_issues(query='is:merged', sha=sha, repo=repo_name)

if results.totalCount == 0:
  print(NOTICE + "No merged PR associated with " + sha + ". Exiting.")
  sys.exit(0)

### NEED TO STORE PR URL

# find associated rfc text file
rfc_file = None
repo = github.get_repo(repo_name)
for commit in event_data['commits']:
    c = repo.get_commit(sha=commit['id'])
    for f in c.files:
      if f.filename.startswith('text/'):
        if f.filename.startswith('0000-'):
          rfc_file = f.filename

# if no rfc text file, exit
if rfc_file is None:
  print(NOTICE + "No RFC file found in commits. Exiting." + ENDC)
  sys.exit(0)

print(INFO + "Cloning repo." + ENDC)
clone_from = "https://" + os.environ['GITHUB_ACTOR'] + ":" + os.environ['API_CREDENTIALS'] + "@github.com/" + repo_name
git = git.Repo.clone_from(clone_from, '.').git

print(INFO + "Setting up git configuration." + ENDC)
git.config('--global', 'user.name', os.environ['INPUT_GIT_USER_NAME'])
git.config('--global', 'user.email', os.environ['INPUT_GIT_USER_EMAIL'])

# get rfc number (current max + 1)
# construct final rfc file name
# create issue on ponyc repo using what we know will be the file location
# store issue url for new issue
#

# mv file from 0000-blah to RFCNUMBER-blah
# rfc tool complete PR URL and ISSUE URL
# commit changes
# push

