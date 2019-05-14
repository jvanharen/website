+++
title = "Mesh Adaptation For Fluid-Structure Interaction Problems"
date = 2019-02-20T21:32:44-06:00  # Schedule page publish date.
draft = false

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
time_start = 2018-06-26T10:30:00
# time_end = 2019-02-20T21:32:44-06:00
all_day = false

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["Julien Vanharen"]

# Abstract and optional shortened version.
abstract = "A new strategy for mesh adaptation dealing with Fluid-Structure Interaction (FSI) problems is presented using a partitioned approach. The Euler equations are solved by an edge-based Finite Volume solver whereas the linear elasticity equations are solved by the Finite Element Method using the Lagrange $P^1$ elements. The coupling between both codes is realized by imposing boundary conditions. Small displacements of the structure are assumed and so the mesh is not deformed. The computation of a well-documented FSI test case is finally carried out to perform validation of this new strategy. The capability of treating three-dimensional complex cases is also demonstrated."
abstract_short = ""

# Name of event and optional event URL.
event = "2018 Fluid Dynamics Conference, AIAA AVIATION Forum"
event_url = "https://arc.aiaa.org/doi/book/10.2514/MFD18"

# Location of event.
location = "Atlanta, GA, USA"

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
tags = []

# Links (optional).
url_pdf = ""
url_slides = "slides/2018_aiaa_fsi_vanharen.html"
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

### Main results

**2D elastic panel in a shock tube.** To validate our FSI approach, a well-documented test case is chosen. 
The test case deals with an elastic panel in a shock tube. [Giordano](https://doi.org/10.1007/s00193-005-0246-9) *et al.* 
gave in his paper a complete set of numerical and experimental data. 
For the sake of clarity, we recall the main characteristics of the experiments 
but the reader is referred to [Giordano]([Giordano](https://doi.org/10.1007/s00193-005-0246-9)) *et al.* 
for a complete description of the geometry and the pressure sensor location in particular.
This test case is very well-documented in the literature and was numerically investigated
by [Sanches](https://doi.org/10.1016/j.apm.2013.11.025) *et al.* and [Pasquariello](https://doi.org/10.1016/j.jcp.2015.12.013) 
*et al.*. A right-moving shock at a Mach number of $M_S = 1.21$ impacts a vertical elastic panel
which is clamped at its basis.
Regarding the flow characteristics, the superscript $L$ (resp. $R$) refers to upstream (resp. downstream) quantities.

<figcaption> Panel characteristics for the elastic panel in a shock tube test case. </figcaption>

|  Characteristic |  Symbol  |  Value |    Units   |
|:---------------:|:--------:|:------:|:----------:|
|      Length     |    $L$   |  $40$  |   $[mm]$   |
|    Thickness    |    $e$   |   $1$  |   $[mm]$   |
| Young's modulus |    $E$   |  $220$ |   $[GPa]$  |
| Poisson's ratio |   $\nu$  | $0.33$ |    $[-]$   |
|     Density     | $\rho_S$ | $7600$ | $[km/m^3]$ |

<figcaption> Flow characteristics for the elastic panel in a shock tube test case. </figcaption>

|      Quantity     |             Value            |    Units   |
|:-----------------:|:----------------------------:|:----------:|
|       $p^R$       |            $10^5$            |   $[Pa]$   |
| $\underline{v}^R$ | $\left(0,0,0 \right)^{\top}$ |   $[m/s]$  |
|     $\rho_F^R$    |            $1.189$           | $[kg/m^3]$ |

The other unknowns are classically given by the Rankine-Hugoniot conditions and one may find
$p^L = 154145.0$ $[Pa]$, $\underline{v}^L = \left( v_x^L, 0, 0 \right)^{\top}$ where $v_x^L = 109.68$ $[m/s]$ and
$\rho_F^L = 1.616$ $[kg/m^3]$.

{{< video src="mach.mov" caption="2D elastic panel in a shock tube. Mach number." numbered="true" library="true">}}

{{< video src="dsp.mov" caption="Displacement magnitude of the panel. The meshes are deformed according to the displacement multiplied by 10." numbered="true" library="true">}}

**3D elastic panel in a shock tube.** To demonstrate our ability to treat complex three-dimensional problems, 
the previous test case dealing with an elastic panel in a shock tube was computed in a three-dimensional configuration. 
In our simulation, the T80 shock tube has a $80~[mm]$ square cross section as stated by 
[Giordano]([Giordano](https://doi.org/10.1007/s00193-005-0246-9)) *et al.*.
For the elastic panel, we considered a panel length of $40~[mm]$, panel thickness of $1~[mm]$ as in the bidimensional case and 
a width of $60~[mm]$. Consenquently, the flow can circulate around the top of the panel with a gap of $25~[mm]$ and 
around the left and right of the panel with a gap of $10~[mm]$ for each side.

{{< video src="mach3d.mov" caption="3D elastic panel in a shock tube. Mach number." numbered="true" library="true">}}

{{< video src="dsp3d.mov" caption="Displacement magnitude of the panel. The meshes are deformed according to the displacement multiplied by 20." numbered="true" library="true">}}