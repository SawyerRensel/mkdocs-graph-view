# MkDocs Graph View

Create beautiful, interactive graph visualizations of your documentation structure.

<div class="grid cards" markdown>

-   :material-graph:{ .lg .middle } __Interactive Graphs__

    ---

    Visualize page connections with force-directed network graphs powered by D3.js

-   :material-cellphone-link:{ .lg .middle } __Responsive Design__

    ---

    Automatically adapts to mobile and desktop layouts for optimal viewing

-   :material-tune:{ .lg .middle } __Highly Configurable__

    ---

    Customize physics simulation, visual appearance, and user interactions

-   :material-theme-light-dark:{ .lg .middle } __Theme Integration__

    ---

    Seamlessly integrates with Material for MkDocs light and dark themes

</div>

## Overview

The MkDocs Graph Plugin adds interactive network graph visualizations to your MkDocs documentation, inspired by [Quartz](https://github.com/jackyzha0/quartz). It helps readers understand the structure and relationships between pages in your documentation.

### Features

- **Mini Graph View**: Shows connected pages in the sidebar
- **Full Graph View**: Expandable overlay with the entire documentation graph
- **Smart Filtering**: BFS-based depth filtering for performance
- **Tag Support**: Display page tags in graph labels
- **Touch Friendly**: Full mobile and touch device support
- **Customizable Physics**: Control node repulsion, centering, and link distances

## Quick Example

![Graph View Example](https://via.placeholder.com/800x400?text=Graph+View+Screenshot)

## Installation

Install using pip:

```bash
pip install mkdocs-graph-view
```

Add to your `mkdocs.yml`:

```yaml
plugins:
  - search
  - graph
```

That's it! Your documentation now has interactive graph visualizations.

## How It Works

1. **Link Extraction**: The plugin scans all pages and extracts internal links
2. **Graph Building**: Creates a network graph data structure
3. **Smart Filtering**: Uses BFS to find connected pages within configured depth
4. **Visualization**: Renders interactive graphs using D3.js force simulation
5. **Responsive Layout**: Automatically positions graphs based on viewport size

## Live Demo

Navigate to any page in this documentation to see the graph plugin in action:

- Check the sidebar for the mini graph view
- Click the expand button to open the full graph overlay
- Hover over nodes to highlight connections
- Click on nodes to navigate to pages

## Next Steps

<div class="grid cards" markdown>

-   [Installation Guide →](getting-started/installation.md)
-   [Configuration Options →](configuration/overview.md)
-   [Usage Examples →](usage/basic.md)
-   [Contributing →](contributing.md)

</div>
