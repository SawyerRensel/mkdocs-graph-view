# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- **BREAKING**: `show_tags` now displays tags as separate nodes in the graph view instead of appending them to page titles
  - Tags appear as distinct nodes with visual styling (accent color, semi-transparent)
  - Pages are connected to their tag nodes via edges
  - Tag nodes are non-clickable
  - Inspired by [Quartz's graph view](https://quartz.jzhao.xyz/features/graph-view)

## [0.1.0] - 2025-11-29

- Initial release of MkDocs Graph Plugin

### Added
- Mini graph view in sidebar showing connected pages
- Full graph overlay with all documentation pages
- Configurable graph depth using BFS algorithm
- D3.js force-directed layout visualization
- Responsive design (mobile and desktop)
- Material theme integration
- Dark mode support
- Configurable physics simulation (repel force, center force, link distance)
- Visual customization options (scale, font size, tag display)
- Interaction controls (drag, zoom, hover effects)
- Tag support integration
- Touch device support
- Automatic resize handling
- Link deduplication and weighting
- Performance optimizations for large documentation sites

### Configuration Options
- `enabled` - Enable/disable plugin
- `local_graph_depth` - Graph depth for mini view
- `global_graph` - Enable full graph overlay
- `repel_force` - Node repulsion strength
- `center_force` - Centering force strength
- `link_distance` - Distance between connected nodes
- `scale` - Overall graph scale
- `font_size` - Label font size
- `show_tags` - Display page tags
- `enable_drag` - Allow node dragging
- `enable_zoom` - Allow zoom and pan
- `focus_on_hover` - Highlight on hover

[Unreleased]: https://github.com/sawyerrensel/mkdocs-graph-view/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/sawyerrensel/mkdocs-graph-view/releases/tag/v0.1.0
