# Best Practices

Guidelines for optimal graph plugin usage and documentation structure.

## Documentation Structure

### Create Meaningful Connections

Link related pages to create useful graphs:

✅ **Good**:
```markdown
See [Installation Guide](installation.md) for setup instructions.
Related: [Configuration](config.md), [Troubleshooting](troubleshooting.md)
```

❌ **Bad**:
```markdown
Isolated page with no links.
```

### Use Consistent Linking Patterns

Establish patterns for how pages link to each other:

**Hub-and-Spoke**:
```
Overview Page
├── Feature A
├── Feature B
└── Feature C
```

**Sequential**:
```
Step 1 → Step 2 → Step 3 → Step 4
```

**Cross-Referenced**:
```
Concept A ←→ Concept B ←→ Concept C
```

### Avoid Orphan Pages

Every page should have at least one incoming or outgoing link:

```markdown
---
# At minimum, link back to index
[← Back to Home](../index.md)
---
```

## Configuration Best Practices

### Start with Defaults

Begin with default configuration and adjust based on results:

```yaml
plugins:
  - graph  # Start here
```

Then customize:
```yaml
plugins:
  - graph-view:
      local_graph_depth: 2  # Adjust as needed
```

### Match Config to Site Size

| Site Size | Recommended Depth | Hover Effects |
|-----------|-------------------|---------------|
| < 50 pages | 2-3 | Enabled |
| 50-100 pages | 2 | Enabled |
| 100-500 pages | 1 | Enabled |
| > 500 pages | 1 | Disabled |

### Test on Real Data

Don't guess at configuration - build and test:

1. `mkdocs serve`
2. Navigate to various pages
3. Check graph appearance
4. Adjust configuration
5. Repeat

## Performance Best Practices

### For Large Documentation

Optimize for performance:

```yaml
plugins:
  - graph-view:
      local_graph_depth: 1       # Minimize nodes
      focus_on_hover: false      # Reduce JS work
      enable_drag: false         # Simplify interactions
```

### Monitor Build Time

Check how the plugin affects build time:

```bash
time mkdocs build
```

If slow, consider:
- Reducing graph depth
- Disabling features
- Using conditional enabling

### Lazy Load Full Graph

The full graph is lazy-loaded by default - don't change this unless necessary.

## Content Best Practices

### Link Contextually

Add links where they make sense in content:

✅ **Good**:
```markdown
For installation instructions, see the [Installation Guide](install.md).
```

❌ **Bad**:
```markdown
Related pages: [Install](install.md) [Config](config.md) [API](api.md)
```

### Use Descriptive Link Text

Help users understand what they'll find:

✅ **Good**:
```markdown
[Learn how to configure the plugin](configuration.md)
```

❌ **Bad**:
```markdown
[Click here](configuration.md)
```

### Balance Links

Too few = disconnected graph
Too many = cluttered graph

**Aim for**: 3-7 outgoing links per page

## Visual Best Practices

### Readable Font Sizes

Choose font sizes appropriate for your theme:

**Material Theme**: 10-12px
**Other Themes**: Test and adjust

```yaml
plugins:
  - graph-view:
      font_size: 10  # Start here
```

### Balanced Spacing

Adjust spacing so nodes don't overlap but aren't too sparse:

```yaml
plugins:
  - graph-view:
      repel_force: 1.0     # Adjust between 0.5-1.5
      link_distance: 50     # Adjust between 30-70
```

### Test Both Themes

If your site has dark mode, test graph in both:

1. Switch to dark mode
2. Check label visibility
3. Verify color contrast
4. Adjust if needed

## Mobile Best Practices

### Mobile-Friendly Config

Optimize for touch devices:

```yaml
plugins:
  - graph-view:
      font_size: 12          # Larger for mobile
      enable_drag: true      # Touch drag
      enable_zoom: true      # Pinch zoom
      focus_on_hover: false  # Better for touch
```

### Test on Mobile

Always test on actual mobile devices:

1. Build documentation
2. View on phone/tablet
3. Check graph positioning
4. Verify interactions work
5. Adjust configuration

## Accessibility Best Practices

### Provide Alternative Navigation

Don't rely solely on graph for navigation:

- Include navigation sidebar
- Add breadcrumbs
- Provide search functionality
- Use clear page hierarchies

### Descriptive Page Titles

Page titles appear as node labels:

✅ **Good**: "Installation Guide"
❌ **Bad**: "Guide" or "Page 1"

### Keyboard Access

Ensure graph is keyboard-accessible:

- Tab through nodes
- Enter to navigate
- Escape to close overlay

## Maintenance Best Practices

### Regular Audits

Periodically check your graph:

1. Build documentation
2. Open full graph view
3. Look for isolated nodes
4. Check for unexpected connections
5. Fix broken links

### Document Your Configuration

Add comments to your configuration:

```yaml
plugins:
  - graph-view:
      # Depth of 2 works well for our ~75 pages
      local_graph_depth: 2

      # Disabled for performance on mobile
      focus_on_hover: false
```

### Version Control

Track configuration changes in git:

```bash
git log -p mkdocs.yml  # See config history
```

## Common Pitfalls to Avoid

### Too Deep Depth

❌ Don't set `local_graph_depth: 5` on large sites
✅ Use `local_graph_depth: 1-2`

### Too Many Features Enabled

❌ Don't enable every feature on large sites
✅ Disable what you don't need for performance

### Inconsistent Link Styles

❌ Don't mix absolute and relative links randomly
✅ Choose one style and stick to it

### Ignoring Mobile

❌ Don't only test on desktop
✅ Always test mobile layout and interactions

### No Testing

❌ Don't change config without testing
✅ Test every configuration change

## Next Steps

- Review [Configuration Examples](../configuration/examples.md)
- Read [Advanced Features](advanced.md)
- Check [Options Reference](../configuration/options.md)
