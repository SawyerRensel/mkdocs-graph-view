# Installation

## Requirements

- Python 3.8 or higher
- MkDocs 1.4.0 or higher
- Material for MkDocs 9.6.0 or higher (for [`show_tags`](../configuration/options.md#show_tags) functionality)

## Install from PyPI

The easiest way to install the plugin is from PyPI using pip:

```bash
pip install mkdocs-graph-view
```

## Install from Source

To install the latest development version from GitHub:

```bash
git clone https://github.com/sawyerrensel/mkdocs-graph-view.git
cd mkdocs-graph-view
pip install -e .
```

## Verify Installation

Check that the plugin is installed correctly:

```bash
python -c "import mkdocs_graph_plugin; print(mkdocs_graph_plugin.__version__)"
```

Or verify it appears in MkDocs plugins:

```bash
mkdocs --version
```

## Next Steps

Once installed, proceed to the [Quick Start](quick-start.md) guide to configure the plugin.
