# dviware

This is an implementation of a DVI ware writen in Python3.
A DVI ware is an interpreter for DVI files which obtained by LaTeX.

The script dvi2docx converts from *.dvi to *.dvi.docx by
```
python3 pathtosrc/dvi2docx.py input.dvi
```


The DVI file for dvi2docx should be compiled with the latex style file,
texstructurespecial.sty, in src.
The style file requires everyhook.sty.

The script dvi2docx.py requires Python-docx, that
you can install by pip3.
It also uses dvipng command to convert mathexpression to png image.

All math expressions will embeded as image file,
which is converted by dvipng.
Hence ..
* Japanese word should not included in math expressions.
If Japanese words are appeared in math expressions,
then the Japanese words will be removed from images.
(Japanese words not in math mode will be appear in resulted docx).
* Picture environments in math modes will be embeded as images.
(Picture environments not in math mode will not be appear in resulted docx).


At this moment, the following are not implemented:
* images included by includegraphics.
* non-text fonts not in math modes.
* page footers and headers.
* alternative font names.
* convert dvi files not in current directories.