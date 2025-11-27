# Configuration Examples

Real-world configuration examples for different use cases.

## Minimal Configuration

For most documentation sites, the defaults work great:

```yaml
plugins:
  - search
  - graph
```

## Small Documentation (< 50 pages)

Can afford deeper graph depth and tighter spacing:

```yaml
plugins:
  - graph-view:
      local_graph_depth: 3      # Show 3 levels deep
      repel_force: 0.5          # Tighter clustering
      link_distance: 30          # Shorter links
      focus_on_hover: true      # Enable hover effects
```

## Medium Documentation (50-100 pages)

Balanced configuration for moderate-sized sites:

```yaml
plugins:
  - graph-view:
      local_graph_depth: 2      # 2 levels deep
      repel_force: 1.0          # Good spacing
      link_distance: 50          # Medium link length
      font_size: 10             # Standard size
      focus_on_hover: true      # Enable hover effects
```

## Large Documentation (> 100 pages)

Optimized for performance with many pages:

```yaml
plugins:
  - graph-view:
      local_graph_depth: 1      # Only direct connections
      repel_force: 0.8          # More spread
      center_force: 0.2         # Less centering
      link_distance: 50          # More space
      font_size: 8              # Smaller labels
      focus_on_hover: false     # Disable for performance
```

## Knowledge Base / Wiki

For interconnected documentation with tags:

```yaml
plugins:
  - tags                        # Enable tags first
  - graph-view:
      local_graph_depth: 2
      show_tags: true           # Show tags in labels
      font_size: 11             # Larger for readability
      repel_force: 1.0
      focus_on_hover: true      # Highlight connections
```

## API Documentation

Clean, professional appearance:

```yaml
plugins:
  - graph-view:
      local_graph_depth: 1
      repel_force: 1.2          # Well-spaced
      link_distance: 60          # Longer links
      font_size: 9              # Compact
      enable_drag: true
      enable_zoom: true
      focus_on_hover: true
```

## Mobile-Optimized

Optimized for touch devices:

```yaml
plugins:
  - graph-view:
      local_graph_depth: 1      # Keep it simple
      enable_drag: true         # Touch drag works well
      enable_zoom: true         # Pinch zoom support
      font_size: 12             # Larger for mobile
      focus_on_hover: false     # Better for touch
      repel_force: 1.0
      link_distance: 50
```

## Presentation Mode

Minimal interactivity for presentations:

```yaml
plugins:
  - graph-view:
      local_graph_depth: 1
      enable_drag: false        # No dragging
      enable_zoom: false        # No zooming
      focus_on_hover: false     # No hover effects
      repel_force: 1.0
      link_distance: 50
```

## Development Mode

See everything during documentation development:

```yaml
plugins:
  - tags
  - graph-view:
      local_graph_depth: 3      # Deep connections
      global_graph: true        # Full graph enabled
      show_tags: true           # Show all tags
      repel_force: 0.6
      center_force: 0.25
      link_distance: 35
      scale: 1.1
      font_size: 10
      enable_drag: true
      enable_zoom: true
      focus_on_hover: true
```

## Compact/Dense Layout

For pages with many connections:

```yaml
plugins:
  - graph-view:
      local_graph_depth: 1
      repel_force: 0.5          # Less spacing
      center_force: 0.3         # More centering
      link_distance: 30          # Shorter links
      font_size: 8              # Smaller text
      scale: 0.9                # Slightly smaller
```

## Sparse/Spread Layout

For better readability with fewer connections:

```yaml
plugins:
  - graph-view:
      local_graph_depth: 2
      repel_force: 1.5          # More spacing
      center_force: 0.1         # Less centering
      link_distance: 70          # Longer links
      font_size: 12             # Larger text
      scale: 1.2                # Slightly larger
```

## Performance-First

Minimal features for maximum speed:

```yaml
plugins:
  - graph-view:
      local_graph_depth: 1      # Shallowest depth
      global_graph: false       # Disable full graph
      enable_drag: false        # No dragging
      enable_zoom: false        # No zooming
      focus_on_hover: false     # No hover effects
      repel_force: 1.0
      link_distance: 50
```

## Next Steps

- Learn about [Best Practices](../usage/best-practices.md)
- Read the complete [Options Reference](options.md)
- See [Advanced Features](../usage/advanced.md)
