# dviware

This is an implementation of a DVI ware writen in Python3.
A DVI ware is an interpreter for DVI files which obtained by LaTeX.

The script dvi2docx converts from *.dvi to *.dvi.docx by
```
python3 pathtosrc/dvi2docx.py input.dvi
```

## Tips to convert

Modify your tex source:
* please insert `\usepackage[T1]{fontenc}` in preamble (to use T1 font encoding for output dvi).
* please insert `\pagestyle{empty}` in preamble (to omit page numbers in header or footer).
* please insert `\thispagestyle{empty}` after `\maketitle` if  `\maketitle` exists  (to omit page numbers in header or footer).
* please copy `src/texstructurespecial.sty` to your directory where tex source is. And do the following:
* please insert `\usepackage{texstructurespecial}` before `\begin{document}` (to embed structures of text as special).
* please insert `\indentedraggedright` after `\begin{document}` (to change from "justified" alignment to "ragged right" alignment for avoiding line-breaks in inline mathmode).

Compile your tex source (e.g., hoge.tex) to a dvi file (e.g., hoge.dvi) by LaTeX (not pdflatex).

Convert your dvi file (e.g., hoge.dvi) to a docx file (e.g., hoge.dvi.docx) by
```
python3 pathtosrc/dvi2docx.py hoge.dvi
```

Open your docx (e.g., hoge.dvi.docx) file by Word, and modify:
* replace ` ]` (space+ket) to `]` (ket). (`\cite` makes this string.)
* replace `[!?...]` (bra+!+?+fontname+:+codepoint(decimal)+ket) to better characters. (symbol fonts in text make this string.)
* remove or modify footnotes.
* remove page-breaks.

## Note

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
* colors.