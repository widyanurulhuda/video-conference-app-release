# -- Project information -----------------------------------------------------
project = "Moil Meeting"
author = "Preseverance Technology, Taiwan"
copyright = "2025 Preseverance Technology, Taiwan"
release = "1.0"

# -- General configuration ---------------------------------------------------
extensions = []  # add Sphinx extensions here if you use any (e.g. "myst_parser")
templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]
html_css_files = ["custom.css"]  # make sure _static/custom.css exists

# Sidebar logo (PNG path is fine)
html_logo = "_static/moil_meeting_app.png"

# Theme options
html_theme_options = {
    "logo_only": True,
    # "display_version": False,
}

# Optional: customize sidebars (these templates exist in RTD theme)
html_sidebars = {
    "**": [
        "sidebar-logo.html",
        "searchbox.html",
        "localtoc.html",
        "relations.html",
    ]
}
