# chalmers-beamer
A [LaTeX Beamer](https://ctan.org/pkg/beamer?lang=en) theme for students and researchers at [Chalmers University of Technology](https://www.chalmers.se/). 

Update (May 2026): Updated to the new Chalmers logo. Thanks to Zicong Jiang for providing the idea and figures! See also [a-bordbar/chalmers-beamer-template-2026](https://github.com/a-bordbar/chalmers-beamer-template-2026) for another template with the updated color scheme. 

# Example
The template and an example can be found in the folder `template`. After compiling the `.tex` file, the resulting `.pdf` should look something like this: 

<p align="center"> 
<img width=400 src="slide1.jpg">
<img width=400 src="slide2.jpg">
</p>
<p align="center"> 
</p>

# Installation
The simplest way is to put the `.sty` file and figures in the same folder as your main `.tex` file. 
Alternatively, you can put these files in the folder `$TEXMFHOME/tex/latex`, where the value of `$TEXMFHOME` can be found via the command `kpsewhich -var-value TEXMFHOME`. 

