# dviware

This is an implementation of a DVI ware writen in Python3.
A DVI ware is an interpreter for DVI files which obtained by LaTeX.


At this moment,
dvi2docx.py does not work well.

The DVI file for dvi2docx should be compiled with the latex style file,
texstructurespecial.sty, in src.
The style file requires everyhook.sty.

The script dvi2docx.py requires Python-docx, that
you can install by pip3.
