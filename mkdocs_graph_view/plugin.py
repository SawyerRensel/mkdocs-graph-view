# Copyright (c) 2016-2025 Martin Donath <martin.donath@squidfunk.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import os
import json
import logging
import shutil
from html.parser import HTMLParser
from urllib.parse import urljoin

from mkdocs import utils
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
from .config import GraphConfig

log = logging.getLogger("mkdocs.material.plugins.graph")

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href":
                    self.links.append(value)

class GraphPlugin(BasePlugin[GraphConfig]):
    def __init__(self):
        self.nodes = {}  # Use dict to avoid duplicates
        self.links = []
        self.page_tags = {}  # Store tags for each page if available

    def on_page_content(self, html, page, config, files):
        # Extract links
        parser = LinkParser()
        parser.feed(html)

        # Extract tags if available (from page metadata)
        tags = []
        if hasattr(page, 'meta') and 'tags' in page.meta:
            tags = page.meta.get('tags', [])
            if isinstance(tags, str):
                tags = [tags]

        # Add node (using dict to avoid duplicates)
        self.nodes[page.url] = {
            "id": page.url,
            "title": page.title,
            "tags": tags,
            "group": 1
        }

        # Process links
        for link in parser.links:
            # Ignore external links, anchors, mailto
            if link.startswith(("http", "https", "mailto", "tel", "#")):
                continue

            # Remove anchor
            url = link.split("#")[0]
            if not url:
                continue

            # Resolve relative URL
            target = urljoin(page.url, url)

            self.links.append({
                "source": page.url,
                "target": target,
                "value": 1
            })

        # Inject base url and config for graph
        rel_root = utils.get_relative_url(".", page.url)
        if rel_root != "." and not rel_root.endswith("/"):
             rel_root += "/"
        elif rel_root == ".":
             rel_root = ""

        # Pass configuration to frontend
        graph_config = {
            "local_graph_depth": self.config.local_graph_depth,
            "global_graph": self.config.global_graph,
            "repel_force": self.config.repel_force,
            "center_force": self.config.center_force,
            "link_distance": self.config.link_distance,
            "scale": self.config.scale,
            "font_size": self.config.font_size,
            "show_tags": self.config.show_tags,
            "enable_drag": self.config.enable_drag,
            "enable_zoom": self.config.enable_zoom,
            "focus_on_hover": self.config.focus_on_hover
        }

        script = f'''<script>
var graph_base_url = "{rel_root}";
var graph_current_page = "{page.url}";
var graph_config = {json.dumps(graph_config)};
</script>'''
        return script + html

    def on_post_build(self, config):
        # Convert nodes dict to list
        nodes_list = list(self.nodes.values())

        # Filter links to ensure target exists in nodes
        node_ids = set(self.nodes.keys())
        valid_links = [l for l in self.links if l["target"] in node_ids]

        # Remove self-loops
        valid_links = [l for l in valid_links if l["source"] != l["target"]]

        # Count link frequencies for weight
        link_counts = {}
        for link in valid_links:
            key = (link["source"], link["target"])
            link_counts[key] = link_counts.get(key, 0) + 1

        # Deduplicate links and add weights
        unique_links = []
        seen = set()
        for link in valid_links:
            key = (link["source"], link["target"])
            if key not in seen:
                seen.add(key)
                unique_links.append({
                    "source": link["source"],
                    "target": link["target"],
                    "value": link_counts[key]
                })

        graph_data = {
            "nodes": nodes_list,
            "links": unique_links
        }

        # Write graph.json
        output_path = os.path.join(config["site_dir"], "graph.json")
        with open(output_path, "w") as f:
            json.dump(graph_data, f, indent=2)

        log.info(f"Graph plugin: Generated graph with {len(nodes_list)} nodes and {len(unique_links)} links")

        # Copy assets
        base_path = os.path.dirname(os.path.abspath(__file__))
        assets_src = os.path.join(base_path, "assets")
        assets_dst = os.path.join(config["site_dir"], "assets")

        js_dst = os.path.join(assets_dst, "javascripts", "graph.js")
        css_dst = os.path.join(assets_dst, "stylesheets", "graph.css")

        os.makedirs(os.path.dirname(js_dst), exist_ok=True)
        os.makedirs(os.path.dirname(css_dst), exist_ok=True)

        shutil.copy(os.path.join(assets_src, "javascripts", "graph.js"), js_dst)
        shutil.copy(os.path.join(assets_src, "stylesheets", "graph.css"), css_dst)

    def on_config(self, config):
        if not self.config.enabled:
            return
            
        config["extra_javascript"].append("https://d3js.org/d3.v7.min.js")
        config["extra_javascript"].append("assets/javascripts/graph.js")
        config["extra_css"].append("assets/stylesheets/graph.css")
