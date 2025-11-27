# MkDocs Graph View - Package Overview

Complete overview of the package structure and files.

## Directory Structure

```
mkdocs-graph-view/
├── .github/
│   └── workflows/
│       ├── docs.yml              # GitHub Actions: Deploy documentation
│       └── publish.yml           # GitHub Actions: Publish to PyPI
├── docs/                         # Documentation site
│   ├── index.md                  # Homepage
│   ├── getting-started/
│   │   ├── installation.md       # Installation guide
│   │   └── quick-start.md        # Quick start guide
│   ├── configuration/
│   │   ├── overview.md           # Configuration overview
│   │   ├── options.md            # All options reference
│   │   └── examples.md           # Configuration examples
│   ├── usage/
│   │   ├── basic.md              # Basic usage
│   │   ├── advanced.md           # Advanced features
│   │   └── best-practices.md     # Best practices
│   ├── contributing.md           # Contributing guide
│   └── changelog.md              # Version history
├── mkdocs_graph_plugin/          # Python package
│   ├── __init__.py               # Package initialization + version
│   ├── plugin.py                 # Main plugin logic
│   ├── config.py                 # Configuration schema
│   └── assets/
│       ├── javascripts/
│       │   └── graph.js          # D3.js visualization
│       └── stylesheets/
│           └── graph.css         # Graph styling
├── .gitignore                    # Git ignore patterns
├── LICENSE                       # GNU GPLv3 License
├── MANIFEST.in                   # Package manifest
├── mkdocs.yml                    # Documentation site config
├── pyproject.toml                # Package metadata & dependencies
├── README.md                     # Package README
├── setup.py                      # Setuptools compatibility
├── SETUP_GUIDE.md                # Publishing setup guide
└── PACKAGE_OVERVIEW.md           # This file
```

## Core Files

### Python Package (`mkdocs_graph_plugin/`)

**`__init__.py`**
- Exports `GraphPlugin` class
- Defines package version

**`plugin.py`** (183 lines)
- Main plugin implementation
- Extends `BasePlugin[GraphConfig]`
- Extracts links from HTML
- Generates `graph.json`
- Injects JavaScript configuration
- Copies assets to build directory

Key methods:
- `on_config()` - Adds D3.js and plugin assets
- `on_page_content()` - Extracts links, injects config
- `on_post_build()` - Generates graph.json, copies assets

**`config.py`** (48 lines)
- Configuration schema using `config_options.Config`
- 11 configurable options
- Type validation and defaults

**`assets/javascripts/graph.js`** (326 lines)
- D3.js force-directed graph implementation
- Mini graph and full graph views
- BFS algorithm for depth filtering
- Responsive layout handling
- Mobile/desktop detection
- Event handlers (click, hover, drag, zoom)

**`assets/stylesheets/graph.css`** (182 lines)
- Material theme CSS variables
- Graph element styling
- Responsive design
- Dark mode support
- Animations

### Configuration Files

**`pyproject.toml`**
- Modern Python package metadata (PEP 621)
- Dependencies: `mkdocs>=1.4.0`
- Entry point: `mkdocs.plugins.graph`
- Package data includes assets

**`mkdocs.yml`**
- Documentation site configuration
- Material theme setup
- Plugin enabled with depth=2
- Navigation structure

### Documentation

**`README.md`**
- Package overview
- Installation instructions
- Quick start
- Configuration examples
- Features list

**`docs/` directory**
- Comprehensive documentation site
- Getting started guides
- Configuration reference
- Usage examples
- Best practices
- Contributing guidelines

### GitHub Actions

**`.github/workflows/docs.yml`**
Triggers on:
- Push to `main` branch
- Pull requests to `main`

Actions:
1. Checkout code
2. Install dependencies
3. Build docs with `mkdocs build`
4. Deploy to GitHub Pages

**`.github/workflows/publish.yml`**
Triggers on:
- GitHub release published

Actions:
1. Build Python package
2. Publish to PyPI (trusted publishing)

## Files to Extract from mkdocs-material

You already have these files copied to the new package. They came from:

```
/home/sawyer/mkdocs-material/material/plugins/graph/
├── __init__.py          → mkdocs_graph_plugin/__init__.py
├── plugin.py            → mkdocs_graph_plugin/plugin.py
├── config.py            → mkdocs_graph_plugin/config.py
└── assets/
    ├── javascripts/
    │   └── graph.js     → mkdocs_graph_plugin/assets/javascripts/graph.js
    └── stylesheets/
        └── graph.css    → mkdocs_graph_plugin/assets/stylesheets/graph.css
```

## Package Entry Point

The package is registered as a MkDocs plugin via `pyproject.toml`:

```toml
[project.entry-points."mkdocs.plugins"]
graph = "mkdocs_graph_plugin.plugin:GraphPlugin"
```

This allows users to enable it in their `mkdocs.yml`:

```yaml
plugins:
  - graph
```

## Asset Handling

Assets are included in the package via:

1. **`pyproject.toml`**:
```toml
[tool.setuptools.package-data]
mkdocs_graph_plugin = ["assets/javascripts/*.js", "assets/stylesheets/*.css"]
```

2. **`MANIFEST.in`**:
```
recursive-include mkdocs_graph_plugin/assets *.js *.css
```

3. **`plugin.py`** copies assets during build:
```python
shutil.copy(
    os.path.join(assets_src, "javascripts", "graph.js"),
    os.path.join(config["site_dir"], "assets", "javascripts", "graph.js")
)
```

## Version Management

Version is defined in two places (keep in sync):

1. **`mkdocs_graph_plugin/__init__.py`**:
```python
__version__ = "0.1.0"
```

2. **`pyproject.toml`**:
```toml
version = "0.1.0"
```

## Dependencies

### Runtime
- `mkdocs>=1.4.0`

### Development
- `mkdocs-material` (for documentation)
- `build` (for building package)
- `twine` (for uploading to PyPI)

### Frontend
- D3.js v7 (loaded from CDN)

## Build Process

### Local Build
```bash
python -m build
```

Produces:
- `dist/mkdocs_graph_plugin-0.1.0.tar.gz` (source)
- `dist/mkdocs_graph_plugin-0.1.0-py3-none-any.whl` (wheel)

### Installation
```bash
pip install mkdocs-graph-view
```

Or from source:
```bash
pip install -e .
```

## Publishing Workflow

1. **Update version** in `__init__.py` and `pyproject.toml`
2. **Update** `docs/changelog.md`
3. **Commit and push** to GitHub
4. **Create release** on GitHub with tag `vX.Y.Z`
5. **GitHub Action** automatically publishes to PyPI

## Testing Locally

```bash
# Install in development mode
pip install -e .

# Test in documentation
cd docs
mkdocs serve

# Build documentation
mkdocs build

# Test package build
python -m build
twine check dist/*
```

## Key Features

### Backend (Python)
- Link extraction from HTML
- Graph data generation
- Link deduplication and weighting
- Tag support
- Configuration injection

### Frontend (JavaScript)
- D3.js force simulation
- BFS depth filtering
- Responsive layout
- Touch support
- Zoom and pan
- Hover effects
- Node highlighting

### Styling (CSS)
- Material theme integration
- Dark mode support
- Responsive design
- Smooth animations
- Accessible colors

## Browser Compatibility

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

GNU GPLv3 License - see LICENSE file

## Next Steps

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for complete publishing instructions.
