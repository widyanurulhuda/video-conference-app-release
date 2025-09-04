# -- Project information -----------------------------------------------------
project = "Moil Meeting"
copyright = "2025 Preseverance Technology , Taiwan"
author = "Preseverance Technology , Taiwan"
release = "1.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx_multiversion",   # <— aktifkan multiversi
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
#html_css_files = ["custom.css"]

# logo di sidebar
html_logo = "_static/moil_meeting_app.png"

html_theme_options = {
    "logo_only": True,
    # "display_version": False,  # biarkan default agar menu versi tampil
}

# pastikan versions.html ada supaya dropdown versi muncul
html_sidebars = {
    "**": [
        "sidebar-logo.html",
        "searchbox.html",
        "localtoc.html",
        "relations.html",
        "versions.html",          # <— penting
    ]
}

# ------------------- sphinx-multiversion -------------------
# Tag release seperti v1.0, v2.0, v3.1, ...
smv_tag_whitelist = r"^v\d+\.\d+(\.\d+)?$"

# Branch yang dibuild sebagai "latest".
# GANTI sesuai nama branch kamu (cek dengan: git symbolic-ref --short HEAD)
smv_branch_whitelist = r"^(main|master)$"

# Anggap semua tag sebagai rilis
smv_released_pattern = r"^tags/.*$"

# Label untuk branch utama
smv_latest_version = "latest"

# Urutan versi (semver-aware) dan format folder output
smv_sort = "version"
smv_outputdir_format = "{ref.name}"
