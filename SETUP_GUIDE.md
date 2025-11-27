# Setup Guide for Publishing

Complete guide to set up and publish the MkDocs Graph View.

## Prerequisites

1. **GitHub Account**: Create if you don't have one
2. **PyPI Account**: Sign up at https://pypi.org/account/register/
3. **Git**: Installed on your machine

## Step 1: Update Package Information

### Edit `pyproject.toml`

Replace placeholder information with your details:

```toml
[project]
name = "mkdocs-graph-view"
authors = [
    {name = "Your Name", email = "your.email@example.com"}  # ← Update this
]

[project.urls]
Homepage = "https://github.com/sawyerrensel/mkdocs-graph-view"  # ← Update
Documentation = "https://sawyerrensel.github.io/mkdocs-graph-view/"  # ← Update
Repository = "https://github.com/sawyerrensel/mkdocs-graph-view"  # ← Update
Issues = "https://github.com/sawyerrensel/mkdocs-graph-view/issues"  # ← Update
```

### Edit `LICENSE`

Replace `[Your Name]` with your name:

```
Copyright (c) 2025 Your Name  # ← Update this
```

### Edit `mkdocs.yml`

Update documentation site configuration:

```yaml
site_author: Your Name  # ← Update
site_url: https://sawyerrensel.github.io/mkdocs-graph-view/  # ← Update

repo_name: sawyerrensel/mkdocs-graph-view  # ← Update
repo_url: https://github.com/sawyerrensel/mkdocs-graph-view  # ← Update
```

### Edit Documentation Files

Search and replace in all `docs/*.md` files:
- `sawyerrensel` → your GitHub username
- `Your Name` → your actual name

## Step 2: Create GitHub Repository

1. **Go to GitHub**: https://github.com/new

2. **Create repository**:
   - Repository name: `mkdocs-graph-view`
   - Description: "Interactive graph visualizations for MkDocs"
   - Public repository
   - **Don't** initialize with README (we have one)

3. **Push your code**:

```bash
cd /home/sawyer/mkdocs-graph-view

# Initialize git
git init
git add .
git commit -m "Initial commit: MkDocs Graph View v0.1.0"

# Add remote and push
git branch -M main
git remote add origin https://github.com/sawyerrensel/mkdocs-graph-view.git
git push -u origin main
```

## Step 3: Set Up GitHub Pages

### Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Build and deployment":
   - Source: **GitHub Actions**
4. Save

### Verify Documentation Deployment

After pushing to main, the GitHub Action will automatically:
1. Build the documentation
2. Deploy to `gh-pages` branch
3. Make it available at: `https://sawyerrensel.github.io/mkdocs-graph-view/`

Check the **Actions** tab on GitHub to monitor progress.

## Step 4: Set Up PyPI Publishing

### Configure PyPI Trusted Publishing

1. **Go to PyPI**: https://pypi.org/manage/account/publishing/

2. **Add a new pending publisher**:
   - PyPI Project Name: `mkdocs-graph-view`
   - Owner: `sawyerrensel` (your GitHub username)
   - Repository name: `mkdocs-graph-view`
   - Workflow name: `publish.yml`
   - Environment name: `pypi`

3. **Save**

This enables trusted publishing (no API tokens needed!)

### Alternative: Using API Token (if preferred)

If you prefer using an API token:

1. **Generate PyPI API Token**:
   - Go to https://pypi.org/manage/account/token/
   - Create token for the project
   - Copy the token

2. **Add to GitHub Secrets**:
   - Go to repo → Settings → Secrets and variables → Actions
   - Create new secret: `PYPI_API_TOKEN`
   - Paste the token

3. **Update `.github/workflows/publish.yml`**:

```yaml
- name: Publish to PyPI
  uses: pypa/gh-action-pypi-publish@release/v1
  with:
    password: ${{ secrets.PYPI_API_TOKEN }}  # Add this line
```

## Step 5: Create Your First Release

### Test Build Locally First

```bash
cd /home/sawyer/mkdocs-graph-view

# Install build tools
pip install build twine

# Build the package
python -m build

# Check the distribution
twine check dist/*

# (Optional) Test upload to TestPyPI
twine upload --repository testpypi dist/*
```

### Create GitHub Release

1. **Go to repository** → **Releases** → **Create a new release**

2. **Create new tag**: `v0.1.0`

3. **Release title**: `v0.1.0 - Initial Release`

4. **Description**:
```markdown
## First Release of MkDocs Graph View 🎉

### Features
- Interactive graph visualizations
- Mini graph in sidebar
- Full graph overlay
- Highly configurable
- Mobile responsive
- Dark mode support

### Installation
pip install mkdocs-graph-view
```

5. **Click** "Publish release"

### Automatic Publishing

The GitHub Action will automatically:
1. Build the package
2. Upload to PyPI
3. Make it available for installation

Check:
- **GitHub Actions** tab for build status
- **PyPI** at https://pypi.org/project/mkdocs-graph-view/

## Step 6: Verify Everything Works

### Test Installation

```bash
# Create new virtual environment
python -m venv test-env
source test-env/bin/activate

# Install from PyPI
pip install mkdocs-graph-view

# Verify
python -c "import mkdocs_graph_plugin; print(mkdocs_graph_plugin.__version__)"
```

### Test Documentation

Visit: `https://sawyerrensel.github.io/mkdocs-graph-view/`

### Test in Real Project

Create a test MkDocs project:

```bash
mkdir test-mkdocs
cd test-mkdocs
pip install mkdocs-material mkdocs-graph-view

# Create mkdocs.yml
cat > mkdocs.yml << 'EOF'
site_name: Test Site
plugins:
  - search
  - graph
EOF

# Create some docs
mkdir docs
echo "# Home" > docs/index.md
echo "[Page 2](page2.md)" >> docs/index.md
echo "# Page 2" > docs/page2.md
echo "[Home](index.md)" >> docs/page2.md

# Serve
mkdocs serve
```

Open http://127.0.0.1:8000 and verify the graph appears!

## Step 7: Future Releases

### Update Version

1. **Edit `mkdocs_graph_plugin/__init__.py`**:
```python
__version__ = "0.2.0"  # Increment version
```

2. **Edit `pyproject.toml`**:
```toml
version = "0.2.0"  # Match version
```

3. **Update `docs/changelog.md`** with changes

### Create Release

1. Commit changes
2. Create new tag: `git tag v0.2.0`
3. Push: `git push && git push --tags`
4. Create GitHub Release
5. GitHub Action automatically publishes to PyPI

## Troubleshooting

### Documentation Not Deploying

Check:
- GitHub Actions tab for errors
- Pages settings are correct
- Workflow has write permissions

### PyPI Publishing Fails

Check:
- Version number isn't already on PyPI
- Trusted publishing is configured
- GitHub Action has proper permissions

### Package Not Installing

Check:
- `MANIFEST.in` includes all assets
- `pyproject.toml` package-data is correct
- Build and upload succeeded

## Maintenance Tips

### Keep Dependencies Updated

```bash
pip install --upgrade mkdocs mkdocs-material
```

### Monitor Issues

Respond to GitHub issues regularly.

### Update Documentation

Keep docs in sync with code changes.

### Test Before Releasing

Always test locally before creating a release.

## Getting Help

- GitHub Issues: File bugs or ask questions
- PyPI Help: https://pypi.org/help/
- GitHub Actions Docs: https://docs.github.com/en/actions

## Checklist

Before publishing:

- [ ] Updated all `sawyerrensel` placeholders
- [ ] Updated all `Your Name` placeholders
- [ ] Updated email addresses
- [ ] Created GitHub repository
- [ ] Enabled GitHub Pages
- [ ] Configured PyPI trusted publishing
- [ ] Tested build locally
- [ ] Created first release
- [ ] Verified installation works
- [ ] Verified documentation deploys
- [ ] Tested in real MkDocs project

Congratulations! Your plugin is now published! 🎉
