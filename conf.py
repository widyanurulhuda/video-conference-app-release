# -- Project information -----------------------------------------------------
project = 'Moil Meeting'
copyright = '2025 Preseverance Technology , Taiwan'
author = 'Preseverance Technology , Taiwan'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = []
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
#html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

# pakai logo SVG di sidebar (atas)
html_logo = "_static/moil_meeting_app.png"

# supaya tema tidak menaruh judul versi dsb
html_theme_options = {
    "logo_only": True,
   # "display_version": False,
}
templates_path = ['_templates']
html_css_files = ['custom.css']

html_sidebars = {
    "**": [
        "sidebar-logo.html",   # custom kita
        "searchbox.html",
        "localtoc.html",       # gunakan localtoc untuk RTD theme
        "relations.html",
    ]
}
