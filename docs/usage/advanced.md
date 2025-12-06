# Advanced Features

Explore advanced features and techniques for power users.

## Custom Styling

### Overriding Colors

You can override graph colors using CSS in your `docs/stylesheets/extra.css`:

```css
/* Change current page color */
.graph-node.active {
    fill: #ff6600 !important;
}

/* Change hover color */
.graph-node:hover {
    fill: #00ff00 !important;
}

/* Change link color */
.graph-link {
    stroke: #666666 !important;
}
```

Add to `mkdocs.yml`:
```yaml
extra_css:
  - stylesheets/extra.css
```

### Adjusting Graph Container

Customize the mini graph container:

```css
#mini-graph-container {
    height: 300px !important;  /* Make taller */
    border: 2px solid #333 !important;
    border-radius: 8px !important;
}
```

## Integration with Other Plugins

### With Tags Plugin

Display tags as separate nodes in the graph:

```yaml
plugins:
  - tags
  - graph-view:
      show_tags: true
```

When enabled, tags appear as distinct nodes in the graph view, similar to [Quartz](https://quartz.jzhao.xyz/features/graph-view). Pages are connected to their tag nodes via edges, making it easy to see which pages share common tags.

### With Search Plugin

The graph complements search by providing visual navigation:

```yaml
plugins:
  - search
  - graph-view
```

Users can:
- Search for pages by name
- Use graph to understand relationships

### With Blog Plugin

Great for showing relationships between blog posts:

```yaml
plugins:
  - blog
  - graph-view:
      local_graph_depth: 2
      show_tags: true
```

## Performance Optimization

### For Large Sites (500+ pages)

```yaml
plugins:
  - graph-view:
      local_graph_depth: 1      # Minimize nodes
      focus_on_hover: false     # Disable expensive hover
      global_graph: false       # Disable full graph
      enable_drag: false        # Reduce interactions
      enable_zoom: false
```

### Lazy Loading

The full graph is lazy-loaded only when the expand button is clicked, not on page load.

### Efficient Filtering

The plugin uses BFS (Breadth-First Search) algorithm for efficient depth-based filtering:

```python
# Efficient O(n) filtering instead of O(n²)
BFS from current page → Find nodes within depth → Filter
```

## Programmatic Access

### Accessing Graph Data

The graph data is available at `/graph.json`:

```javascript
fetch('/graph.json')
  .then(res => res.json())
  .then(data => {
    console.log('Nodes:', data.nodes);
    console.log('Links:', data.links);
  });
```

### Graph Data Structure

```json
{
  "nodes": [
    {
      "id": "page/path/",
      "title": "Page Title",
      "tags": ["tag1", "tag2"],
      "group": 1
    }
  ],
  "links": [
    {
      "source": "page/a/",
      "target": "page/b/",
      "value": 1
    }
  ]
}
```

## Advanced Configurations

### Disable Graph on Specific Pages

#### Per-Page Control (Frontmatter)

Hide the graph on individual pages using frontmatter:

```yaml
---
hide:
  - graph-view
---

# Page Title

This page won't display the graph view.
```

This works just like hiding the table of contents or navigation in MkDocs Material theme.

#### Global Control (Environment Variables)

Use conditional configuration with environment variables:

```yaml
plugins:
  - graph-view:
      enabled: !ENV [ENABLE_GRAPH, true]
```

Then control per-build:
```bash
ENABLE_GRAPH=false mkdocs build
```

### Different Configs for Dev vs Production

```yaml
plugins:
  - graph-view:
      # Use env variable with fallback
      local_graph_depth: !ENV [GRAPH_DEPTH, 1]
      focus_on_hover: !ENV [GRAPH_HOVER, true]
```

Development:
```bash
GRAPH_DEPTH=3 GRAPH_HOVER=true mkdocs serve
```

Production:
```bash
GRAPH_DEPTH=1 GRAPH_HOVER=false mkdocs build
```

## Graph Algorithms

### Depth Filtering (BFS)

The plugin uses Breadth-First Search to find connected nodes:

1. Start at current page
2. Add to queue with distance 0
3. For each node in queue:
   - If distance < max_depth:
     - Add neighbors to queue
     - Mark as visited
4. Return all visited nodes

### Link Deduplication

Multiple links between same pages are counted and weighted:

```python
# Before: Multiple links
A → B
A → B
A → B

# After: Single weighted link
A →(weight=3)→ B
```

## Troubleshooting

### Graph Not Showing

Check browser console for errors:
```javascript
// Expected output
Graph plugin: Generated graph with X nodes and Y links
```

### Incorrect Connections

The plugin only detects `<a href="...">` links in rendered HTML. Ensure:
- Links are properly formatted
- URLs are relative or absolute internal links
- Links are not in code blocks (unless intended)

### Performance Issues

Monitor with browser DevTools:
1. Open Performance tab
2. Record page load
3. Check for long-running scripts
4. Consider reducing `local_graph_depth`

## Next Steps

- Review [Best Practices](best-practices.md)
- Check [Configuration Examples](../configuration/examples.md)
- Read the [Options Reference](../configuration/options.md)
