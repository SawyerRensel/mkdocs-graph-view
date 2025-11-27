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

from mkdocs.config import config_options

class GraphConfig(config_options.Config):
    """
    Graph plugin configuration.
    """
    enabled = config_options.Type(bool, default=True)

    # Local graph settings (mini graph in sidebar)
    local_graph_depth = config_options.Type(int, default=1)

    # Global graph settings
    global_graph = config_options.Type(bool, default=True)

    # Physics simulation settings
    repel_force = config_options.Type(float, default=1.0)
    center_force = config_options.Type(float, default=0.2)
    link_distance = config_options.Type(int, default=50)

    # Visual settings
    scale = config_options.Type(float, default=1.1)
    font_size = config_options.Type(int, default=10)
    show_tags = config_options.Type(bool, default=False)

    # Interaction settings
    enable_drag = config_options.Type(bool, default=True)
    enable_zoom = config_options.Type(bool, default=True)
    focus_on_hover = config_options.Type(bool, default=True)
