# Quick Start

Get up and running with the Graph Plugin in minutes.

## Basic Setup

1. **Add the plugin to `mkdocs.yml`**:

```yaml
plugins:
  - search
  - graph-view
```

!!! tip
    The `search` plugin is included with MkDocs. Always include it when adding other plugins.

2. **Build your documentation**:

```bash
mkdocs serve
```

3. **View the graph**:

Navigate to any page in your documentation. You'll see:
- A mini graph in the sidebar showing connected pages
- An expand button to view the full graph
- The current page highlighted in the graph

## Your First Configuration

Let's customize the graph appearance:

```yaml
plugins:
  - search
  - graph-view:
      local_graph_depth: 2      # Show 2 levels of connections
      repel_force: 1.0           # Spacing between nodes
      link_distance: 50          # Link length
      font_size: 10              # Label size
```

Save and reload. You'll notice:
- More connected pages visible (depth: 2)
- Nodes are well-spaced
- Labels are easy to read

## Common Patterns

### Minimal Configuration

For most documentation sites:

```yaml
plugins:
  - graph-view
```

### Knowledge Base

For wikis and interconnected documentation:

```yaml
plugins:
  - tags
  - graph-view:
      local_graph_depth: 2
      show_tags: true
      focus_on_hover: true
```

### Large Documentation

For sites with 100+ pages:

```yaml
plugins:
  - graph-view:
      local_graph_depth: 1
      repel_force: 0.8
      focus_on_hover: false
```

## Understanding the Graph

### Mini Graph (Sidebar)
- Shows the current page and its connections
- Depth controlled by `local_graph_depth`
- Automatically hides on mobile (moves to bottom of content)

### Full Graph (Overlay)
- Click the expand button to open
- Shows all pages in your documentation
- Pan by dragging, zoom with scroll wheel
- Click nodes to navigate

### Node Colors
- **Blue (Primary)**: Current page
- **Gray**: Other pages
- **Orange (Accent)**: Hovered page

## Next Steps

- Learn about all [configuration options](../configuration/overview.md)
- See [configuration examples](../configuration/examples.md) for different use cases
- Read [best practices](../usage/best-practices.md) for optimal performance
