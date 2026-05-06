# BindDrift LaTeX Draft

This directory is the M7 LaTeX starting point, not a final submission package.
The target template is IEEE conference LaTeX for the SANER/ICSME route. The
`main.tex` file uses `IEEEtran` when it is installed and falls back to the
standard `article` class so artifact validation can still compile the draft in
minimal environments.

The reader is a CCF-B software-engineering reviewer landing cold on the work.
After reading this draft, they should understand the claim boundary, method,
oracle-blind evaluation protocol, arm64 external-validity slice, and why the
paper is framed as warning prioritization rather than bug confirmation.

M7 intentionally stops at skeleton, method, and evaluation protocol. Later
polish should tighten prose, replace placeholder figure boxes with production
figures, and adapt the bibliography to the selected venue.
