# Contributing

Thank you for your interest in contributing to the MkDocs Graph Plugin!

## Ways to Contribute

- 🐛 Report bugs
- 💡 Request features
- 📝 Improve documentation
- 🔧 Submit code changes
- 🧪 Add tests
- 🌐 Improve translations

## Getting Started

### Development Setup

1. **Fork and clone the repository**:

```bash
git clone https://github.com/sawyerrensel/mkdocs-graph-view.git
cd mkdocs-graph-view
```

2. **Create a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install in development mode**:

```bash
pip install -e .
pip install -r requirements-dev.txt  # If exists
```

4. **Test the plugin**:

```bash
cd docs
mkdocs serve
```

### Making Changes

1. **Create a feature branch**:

```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes**:

Edit the relevant files:
- `mkdocs_graph_plugin/plugin.py` - Backend logic
- `mkdocs_graph_plugin/config.py` - Configuration options
- `mkdocs_graph_plugin/assets/javascripts/graph.js` - Frontend visualization
- `mkdocs_graph_plugin/assets/stylesheets/graph.css` - Styling

3. **Test your changes**:

```bash
mkdocs serve
# Navigate and test the graph functionality
```

4. **Commit your changes**:

```bash
git add .
git commit -m "Add feature: description of your changes"
```

5. **Push and create PR**:

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Code Guidelines

### Python Code Style

- Follow [PEP 8](https://pep8.org/)
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

Example:
```python
def extract_links(html: str) -> list[str]:
    """
    Extract internal links from HTML content.

    Args:
        html: HTML content to parse

    Returns:
        List of internal link URLs
    """
    parser = LinkParser()
    parser.feed(html)
    return parser.links
```

### JavaScript Code Style

- Use ES6+ features
- Add comments for complex logic
- Keep functions small and focused
- Use meaningful variable names

Example:
```javascript
/**
 * Initialize graph visualization
 * @param {HTMLElement} container - Container element
 * @param {Object} data - Graph data with nodes and links
 * @param {Object} options - Configuration options
 */
function initGraph(container, data, options) {
    // Implementation
}
```

### CSS Code Style

- Use Material theme CSS variables
- Add comments for sections
- Keep selectors specific but not overly complex

Example:
```css
/* --- Mini Graph Container --- */
#mini-graph-container {
    width: 100%;
    height: 200px;
    background-color: var(--md-default-bg-color);
}
```

## Testing

### Manual Testing

Test your changes with:

1. **Different documentation sizes**:
   - Small (< 20 pages)
   - Medium (50-100 pages)
   - Large (> 100 pages)

2. **Different configurations**:
   - Various depth settings
   - Different physics parameters
   - Enabled/disabled features

3. **Different devices**:
   - Desktop browsers (Chrome, Firefox, Safari)
   - Mobile devices
   - Different screen sizes

4. **Different themes**:
   - Light mode
   - Dark mode
   - Different Material theme colors

### What to Test

- [ ] Mini graph appears correctly
- [ ] Full graph opens and closes
- [ ] Navigation works (clicking nodes)
- [ ] Hover effects work (if enabled)
- [ ] Drag and zoom work (if enabled)
- [ ] Mobile layout works
- [ ] Resize handling works
- [ ] No console errors
- [ ] Performance is acceptable

## Documentation

### Updating Documentation

If your change affects usage:

1. Update relevant `.md` files in `docs/`
2. Add examples if introducing new features
3. Update configuration examples if needed
4. Test documentation builds:

```bash
mkdocs serve
```

### Documentation Style

- Use clear, concise language
- Provide code examples
- Include configuration snippets
- Add warnings/notes where appropriate

Use admonitions:
```markdown
!!! note
    This feature requires MkDocs 1.4+

!!! warning
    High depth values can impact performance

!!! tip
    Start with default settings and adjust
```

## Submitting Pull Requests

### PR Checklist

Before submitting:

- [ ] Code follows style guidelines
- [ ] Changes are tested manually
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] Branch is up to date with main

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
How were these changes tested?

## Screenshots
If applicable, add screenshots

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

## Reporting Issues

### Bug Reports

Include:

1. **Description**: Clear description of the bug
2. **Steps to Reproduce**: How to reproduce the issue
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**:
   - OS
   - Python version
   - MkDocs version
   - Plugin version
   - Browser (if frontend issue)
6. **Configuration**: Your `mkdocs.yml` graph config
7. **Screenshots**: If applicable

### Feature Requests

Include:

1. **Description**: What feature you'd like to see
2. **Use Case**: Why this feature is needed
3. **Examples**: Examples from other tools
4. **Alternatives**: What you currently do instead

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism gracefully
- Focus on what's best for the community

### Unacceptable Behavior

- Harassment of any kind
- Trolling or insulting comments
- Publishing others' private information
- Unprofessional conduct

## Questions?

- Check existing [Issues](https://github.com/sawyerrensel/mkdocs-graph-view/issues)
- Read the [Documentation](https://sawyerrensel.github.io/mkdocs-graph-view/)
- Open a new issue for questions

## License

By contributing, you agree that your contributions will be licensed under the GNU GPLv3 License.
