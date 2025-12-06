# Options Reference

Complete reference for all configuration options.

## Plugin Control

### `enabled`

- **Type**: `bool`
- **Default**: `true`
- **Description**: Enable or disable the plugin entirely

```yaml
plugins:
  - graph-view:
      enabled: true
```

## Graph Depth

### `local_graph_depth`

- **Type**: `int`
- **Default**: `1`
- **Range**: 1-5 (recommended)
- **Description**: Number of connection levels to show in the mini graph

The plugin uses BFS (Breadth-First Search) to find pages within this depth from the current page.

**Examples**:
- `1`: Shows only directly connected pages
- `2`: Shows connected pages and their connections
- `3`: Shows 3 levels deep (can get large quickly)

```yaml
plugins:
  - graph-view:
      local_graph_depth: 2
```

!!! warning
    Values above 3 can result in very large graphs on interconnected documentation sites.

### `global_graph`

- **Type**: `bool`
- **Default**: `true`
- **Description**: Enable the full-screen graph overlay

```yaml
plugins:
  - graph-view:
      global_graph: true
```

## Physics Simulation

These options control the D3.js force-directed layout.

### `repel_force`

- **Type**: `float`
- **Default**: `1.0`
- **Range**: 0.5-2.0 (recommended)
- **Description**: Controls how strongly nodes repel each other

Higher values = more spread out nodes
Lower values = tighter clustering

```yaml
plugins:
  - graph-view:
      repel_force: 1.2
```

### `center_force`

- **Type**: `float`
- **Default**: `0.2`
- **Range**: 0.1-0.5 (recommended)
- **Description**: Controls how strongly nodes are pulled toward the center

Higher values = stronger centering
Lower values = nodes can drift more

```yaml
plugins:
  - graph-view:
      center_force: 0.3
```

### `link_distance`

- **Type**: `int`
- **Default**: `50`
- **Range**: 30-100 (recommended)
- **Description**: Target pixel distance between connected nodes

```yaml
plugins:
  - graph-view:
      link_distance: 60
```

## Visual Settings

### `scale`

- **Type**: `float`
- **Default**: `1.1`
- **Range**: 0.8-1.5 (recommended)
- **Description**: Overall scale multiplier for the graph

```yaml
plugins:
  - graph-view:
      scale: 1.0
```

### `font_size`

- **Type**: `int`
- **Default**: `10`
- **Range**: 8-14 (recommended)
- **Description**: Font size in pixels for node labels

```yaml
plugins:
  - graph-view:
      font_size: 12
```

### `show_tags`

- **Type**: `bool`
- **Default**: `false`
- **Description**: Display tags as separate nodes in the graph view

When enabled, tags appear as distinct nodes in both local and global graph views, with edges connecting pages to their associated tags. This feature is inspired by [Quartz's graph view](https://quartz.jzhao.xyz/features/graph-view).

Requires the `tags` plugin to be enabled.

```yaml
plugins:
  - tags
  - graph-view:
      show_tags: true
```

Tag nodes are visually distinct from page nodes with:
- Different color (accent color)
- Non-clickable (they don't navigate anywhere)
- Semi-transparent appearance that becomes fully opaque on hover

## Interaction Settings

### `enable_drag`

- **Type**: `bool`
- **Default**: `true`
- **Description**: Allow users to drag nodes

```yaml
plugins:
  - graph-view:
      enable_drag: true
```

### `enable_zoom`

- **Type**: `bool`
- **Default**: `true`
- **Description**: Allow users to zoom and pan the graph

```yaml
plugins:
  - graph-view:
      enable_zoom: true
```

### `focus_on_hover`

- **Type**: `bool`
- **Default**: `true`
- **Description**: Highlight connections when hovering over nodes

Disabling can improve performance on large graphs.

```yaml
plugins:
  - graph-view:
      focus_on_hover: false
```

## Complete Example

```yaml
plugins:
  - search
  - tags
  - graph-view:
      # Plugin control
      enabled: true

      # Graph depth
      local_graph_depth: 2
      global_graph: true

      # Physics
      repel_force: 1.0
      center_force: 0.2
      link_distance: 50

      # Visual
      scale: 1.1
      font_size: 10
      show_tags: true

      # Interaction
      enable_drag: true
      enable_zoom: true
      focus_on_hover: true
```

## Next Steps

- See [Configuration Examples](examples.md) for common use cases
- Read [Best Practices](../usage/best-practices.md) for optimization tips
