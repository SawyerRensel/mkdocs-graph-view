# Basic Usage

Learn how to use the Graph Plugin effectively in your documentation.

## Understanding the Graph Views

### Mini Graph (Sidebar)

The mini graph appears in the sidebar on desktop and at the bottom of the content on mobile.

**Features**:
- Shows the current page (highlighted in blue)
- Shows connected pages within configured depth
- Updates automatically when navigating
- Click nodes to navigate to pages
- Drag nodes to rearrange (if enabled)

**When You See It**:
- Desktop: Top of the right sidebar
- Mobile: Bottom of page content

### Full Graph (Overlay)

Click the expand button in the mini graph to open the full graph overlay.

**Features**:
- Shows all pages in your documentation
- Pan by dragging the background
- Zoom with mouse wheel or pinch gesture
- Click nodes to navigate
- Click background or X button to close

## Navigating with the Graph

### Click to Navigate

Click any node in either graph view to navigate to that page.

```
[Graph Node] → Click → [Navigate to Page]
```

### Hover to Explore

Hover over nodes to see connections highlighted (if `focus_on_hover` is enabled).

**What Happens**:
- Hovered node grows slightly
- Connected links become opaque
- Unconnected nodes fade
- Connected nodes stay visible

### Drag to Rearrange

Drag nodes to manually position them (if `enable_drag` is enabled).

**Behavior**:
- Dragged node follows cursor
- Physics simulation continues around it
- Release to let it settle into new position

## Understanding Node Colors

| Color | Meaning |
|-------|---------|
| Blue (Primary) | Current page you're viewing |
| Gray | Other pages in your documentation |
| Orange (Accent) | Hovered page |

## Understanding Connections

### Direct Connections (Depth 1)

Pages with links to/from the current page:

```
Current Page ←→ Connected Page
```

### Indirect Connections (Depth 2+)

Pages connected through other pages:

```
Current Page ←→ Intermediate Page ←→ Distant Page
```

## Common Scenarios

### Finding Related Content

1. Open any page
2. Look at the mini graph
3. See what pages link to/from this page
4. Click to explore related content

### Understanding Documentation Structure

1. Click the expand button
2. View the full graph
3. Observe clusters of related pages
4. Navigate to areas of interest

### Discovering Isolated Pages

Pages with no connections appear as single nodes (only visible on their own page).

**This indicates**:
- Page has no internal links
- Page is not linked from other pages
- Consider adding connections for better navigation

## Tips for Users

### On Desktop

- Use the sidebar mini graph for quick navigation
- Hover to see connections
- Click expand for full overview

### On Mobile

- Scroll to bottom of page for mini graph
- Tap expand button for full view
- Use pinch-to-zoom for better visibility
- Tap nodes to navigate

### Keyboard Users

- Tab through nodes in the graph
- Enter to navigate to selected node
- Escape to close full graph overlay

## Troubleshooting

### Mini Graph is Empty

**Possible Reasons**:
- Current page has no links to/from other pages
- Graph depth is set too low
- Page is isolated in documentation

**Solution**: Check page content and add relevant links.

### Too Many Nodes

**Solution**: Site administrator should reduce `local_graph_depth` in configuration.

### Graph Performs Slowly

**Solution**: Site administrator should disable `focus_on_hover` or reduce graph depth.

## Next Steps

- Learn about [Advanced Features](advanced.md)
- Read [Best Practices](best-practices.md)
- Explore [Configuration Options](../configuration/options.md)
