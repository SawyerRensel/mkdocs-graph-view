# Configuration Overview

The Graph Plugin offers extensive configuration options to customize the appearance, behavior, and performance of your documentation graphs.

## Configuration Categories

### Graph Depth
Controls how many levels of connections to display in the mini graph view.

### Physics Simulation
Controls the force-directed layout behavior: node repulsion, centering, and link distances.

### Visual Settings
Controls the appearance: scale, font sizes, and tag display.

### Interaction
Controls user interactions: dragging, zooming, and hover effects.

## Configuration File Location

All configuration goes in your `mkdocs.yml` file under the `graph` plugin section:

```yaml
plugins:
  - graph-view:
      # Your configuration here
      local_graph_depth: 2
      repel_force: 1.0
      # ... more options
```

## Default Values

If you don't specify an option, these defaults are used:

```yaml
plugins:
  - graph-view:
      enabled: true
      local_graph_depth: 1
      global_graph: true
      repel_force: 1.0
      center_force: 0.2
      link_distance: 50
      scale: 1.1
      font_size: 10
      show_tags: false
      enable_drag: true
      enable_zoom: true
      focus_on_hover: true
```

## Configuration Approach

### Start Simple
Begin with defaults and only customize what you need:

```yaml
plugins:
  - graph-view
```

### Iterate Based on Results
Build your docs and adjust based on what you see:

```yaml
plugins:
  - graph-view:
      local_graph_depth: 2  # First adjustment
```

### Fine-tune for Your Site
Customize based on your documentation size and structure:

```yaml
plugins:
  - graph-view:
      local_graph_depth: 2
      repel_force: 0.8
      link_distance: 40
      focus_on_hover: true
```

## Common Adjustments

### Too Many Nodes?
Reduce `local_graph_depth`:
```yaml
local_graph_depth: 1
```

### Nodes Too Close Together?
Increase `repel_force` and `link_distance`:
```yaml
repel_force: 1.2
link_distance: 60
```

### Labels Too Small?
Increase `font_size`:
```yaml
font_size: 12
```

### Performance Issues?
Disable `focus_on_hover` and reduce depth:
```yaml
local_graph_depth: 1
focus_on_hover: false
```

## Next Steps

- View the complete [Options Reference](options.md)
- Browse [Configuration Examples](examples.md) for different scenarios
- Learn [Best Practices](../usage/best-practices.md) for optimal configuration
