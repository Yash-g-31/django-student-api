# dev_portal

Simple Django REST project (students API).

## What I added
- `.gitignore` — ignores virtualenvs, pyc, db files, editor folders, secrets.
- `requirements.txt` — minimal dependencies used by the project.

## Quick setup (Windows PowerShell)
Run these from the project root (where `manage.py` is):

```powershell
# create and activate virtualenv
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# create .env (if using MySQL provide DB_HOST, DB_USER, DB_PASS, DB_NAME)
# e.g. create a file named .env in the project root with keys like:
# DB_HOST=127.0.0.1
# DB_USER=root
# DB_PASS=yourpassword
# DB_NAME=student_db

# run migrations (if using sqlite or a running DB)
python manage.py migrate

# run the dev server bound to all interfaces (good for previews/port-forwarding)
python manage.py runserver 0.0.0.0:8000
```

Open `http://127.0.0.1:8000/test/` to verify a quick response and `http://127.0.0.1:8000/api/students/` for the API.

## How to push to GitHub (one-off from project root)
If you haven't created a remote repo yet, create it on GitHub (via web UI or `gh repo create`). Then run these PowerShell commands:

```powershell
# initialize git (skip if repo already initialized)
git init

# set a proper name/email if not set
git config user.name "Your Name"
git config user.email "you@example.com"

# add files, commit
git add .
git commit -m "Initial commit: dev_portal Django project"

# add remote (replace with your repo URL)
git remote add origin https://github.com/<your-username>/<repo-name>.git

# push
git branch -M main
git push -u origin main
```

If you prefer to use the GitHub CLI (`gh`) you can create a remote and push in one step:

```powershell
# create repo interactively and push
gh repo create <repo-name> --public --source=. --remote=origin --push
```

## Notes
- If you are using MySQL make sure `mysqlclient` can be installed (you may need Visual C++ Build Tools). For quick local dev you can use sqlite by adjusting `dev_portal/settings.py`.
- I left `requirements.txt` minimal; pin additional packages or versions as you stabilize the project.

If you'd like, I can:
- initialize git here and make the first commit for you, and/or
- create the remote repo on GitHub using `gh` (if you have it installed and want me to run commands), or
- add a CI workflow (GitHub Actions) to run tests on push.
