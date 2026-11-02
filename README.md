# Hello CI/CD - Beginner Project

A simple website with a complete GitHub Actions CI/CD pipeline. No VPS, FastAPI server, or Python packages required.

## Project files

- `site/index.html`: HTML/CSS/JS website
- `tests/test_site.py`: Python tests (CI)
- `.github/workflows/ci-cd.yml`: GitHub Actions pipeline (CI and CD)

## 1. Test on your computer

Install Python 3.11 or newer, open a terminal in this project folder, and run:

```bash
python -m unittest discover -s tests -v
```

Or on Windows, if you use the Python launcher:

```powershell
py -m unittest discover -s tests -v
```

To view the website locally, open `site/index.html` in your browser.

## 2. Upload to GitHub

Create a **public**, **empty** repository on GitHub named `hello-ci-cd` (do not initialize it with a README). In the terminal from the project root:

```bash
git init
git add .
git commit -m "My first CI/CD project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/hello-ci-cd.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username. You must be signed in to GitHub in your Git credential manager (or otherwise authenticate).

## 3. Enable GitHub Pages

In your GitHub repository, open **Settings → Pages**. Under **Build and deployment → Source**, select **GitHub Actions**. Open the **Actions** tab to see `CI - Test Website` and, after it passes, `CD - Deploy Website`.

Your website URL will normally be:

`https://YOUR_USERNAME.github.io/hello-ci-cd/`

GitHub Actions also displays the actual deployment URL, so use that if it differs.

## 4. See how CI blocks a broken deployment

Change `<h1>Hello CI/CD!</h1>` in `site/index.html` to `<h1>Wrong Heading</h1>`.

Commit and push. The heading test fails, so the deploy job does not run.

Change the text back, commit and push again. Now tests pass and deployment runs.

## 5. What happens automatically?

`push to main` → `test` → `deploy if tests pass` → `GitHub Pages website`.

On pull requests, tests run but deployment is skipped.

Note: GitHub Pages serves static files only. It will not run a FastAPI backend. To deploy FastAPI, you need a separate backend hosting platform or VPS.
