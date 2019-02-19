+++
title = "PhD Defense"
date = 2019-02-19T09:01:40-06:00  # Schedule page publish date.
draft = false

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
time_start = 2017-05-16T14:00:00
# time_end = 2017-05-16T09:01:40-06:00
all_day = false

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["Julien Vanharen"]

# Abstract and optional shortened version.
abstract = "This work deals with high-order numerical methods for unsteady flows around complex geometries. In order to cope with the low-order industrial Finite Volume Method, the proposed technique consists in computing on structured and unstructured zones with their associated schemes: this is called a hybrid approach. Structured and unstructured meshes are then coupled by a nonconforming grid interface. The latter is analyzed in details with special focus on unsteady flows. It is shown that a dedicated treatment at the interface avoids the reflection of spurious waves. Moreover, this hybrid approach is validated on several academic test cases for both convective and diffusive fluxes. The extension of this hybrid approach to high-order schemes is limited by the efficiency of unstructured high-order schemes in terms of computational time. This is why a new approach is explored: the Spectral Difference Method. A new framework is especially developed to perform the spectral analysis of Spectral Discontinuous Methods. The Spectral Difference Method seems to be a viable alternative in terms of computational time and number of points per wavelength needed for a given application to capture the flow physics."
abstract_short = ""

# Name of event and optional event URL.
event = "PhD Defense"
event_url = ""

# Location of event.
location = "CERFACS, 42 Avenue Gaspard Coriolis, 31100 Toulouse, France"

# Is this a featured talk? (true/false)
featured = false

# Projects (optional).
#   Associate this talk with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["deep-learning"]` references 
#   `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects = []

# Slides (optional).
#   Associate this page with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references 
#   `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides = ""

# Tags (optional).
#   Set `tags = []` for no tags, or use the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["Finite Volume", "Nonconforming Grid Interface", "Hybrid Approach", "High-Order Unstructured Schemes", "Spurious Waves", "Spectral Difference","Spectral Analysis"]

# Links (optional).
url_pdf = "files/phd.pdf"
url_slides = "files/PhD_Talk_Vanharen_2017_handout.pdf"
url_video = ""
url_code = ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
[image]
  # Caption (optional)
  caption = ""

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = ""
+++
