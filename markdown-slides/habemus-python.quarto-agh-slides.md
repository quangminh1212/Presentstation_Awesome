# <span class="emoji">🎓</span> [AGH](https://www.agh.edu.pl/en) slide deck for [Quarto](https://quarto.org/docs/presentations/)/Jupyter/Python <span class="emoji">🐍</span>

<span class="emoji">💡</span> This repo provides a single Jupyter/Python notebook file which can get you started with authoring a&nbsp;reproducible
  presentation in&nbsp;a&nbsp;template themed following [AGH University of Krakow](https://www.agh.edu.pl/en/) (🇵🇱)
  [visual identity](https://www.agh.edu.pl/en/university/multimedia/graphic-symbol)
  and [logo usage](https://www.agh.edu.pl/en/o-agh/multimedia/znak-graficzny-agh/znak-graficzny-bez-nazwy) guidelines.

<span class="emoji">👩‍💻</span> It allows to&nbsp;tightly couple the code generating all figures and values in the slides with other presentation content.
It enables you (or&nbsp;others) to recreate all slides, including figures and any in-text dynamic content 
  with a&nbsp;single `quarto render ...` command, thus ensuring that slide
  contents are by-design in&nbsp;sync with the code, in the spirit of "reproducible manuscripts" approach
  (see,&nbsp;e.g.,&nbsp;[Perkel 2022, Nature](https://doi.org/10.1038/d41586-022-00563-z)).

<span class="emoji">📚</span> In addition, the sample notebook includes BibTeX-format bibliography setup which automatically
  adds reference footnotes for slides with `[@label]` citations.

## <span class="emoji">🧭</span> How to use it?

<span class="emoji">📝</span> Everything is in a single file, so you can grab the [example `.ipynb` file](https://github.com/habemus-python/quarto-agh-slides/blob/main/slides.ipynb)
  in any way (downloading the ipynb file, [downloading the repo contents](https://github.com/habemus-python/quarto-agh-slides/archive/refs/heads/main.zip),
  cloning, [forking](https://github.com/habemus-python/quarto-agh-slides/fork), ...) and edit it with your favourite Jupyter notebook tool 
  (e.g., [Jupyter lab](https://jupyterlab.readthedocs.io), [VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks), 
  [PyCharm](https://www.jetbrains.com/help/pycharm/jupyter-notebook-support.html), [Colab](https://colab.google), [Spyder](https://docs.spyder-ide.org/current/plugins/notebook.html),&nbsp;...).
Forking the repo will additionally help you in setting up [CI workflows](https://github.com/habemus-python/quarto-agh-slides/tree/main/.github/workflows) for rendering on different platforms,
  code linting, url- and spell-checks, etc.

<span class="emoji">🌐</span> To generate HTML files for presentation, do `quarto render slides.ipynb --execute --to revealjs`, the output (`slides.html` file) should look like this:

<p align="center">
    <img 
        src="https://raw.githubusercontent.com/habemus-python/quarto-agh-slides/refs/heads/gif/slides.gif" 
        alt="slides converted to animated gif"
        width="75%"
    />
</p>

<span class="emoji">🖨️</span> To convert it to a pdf, open in a browser, select `☰ :: Tools :: PDF Export Mode` and use the browser's print dialog to save a pdf.

<span class="emoji">✨</span> To learn more about Quarto/Revealjs features, e.g., speaker notes, multi-column slides, layout helpers, absolute positioning, animations, backgrounds, videos,
  slide numbering and navigation, speaker view, audible accessibility helpers, automatic slide stepping, timing, chalkboard plugin, multiplexing and many more, 
  [read the friendly manual](https://quarto.org/docs/presentations/revealjs/).

## <span class="emoji">🏛️</span> Quarto templates from other universities
- 🇦🇺 [monash.edu (Melbourne)](https://github.com/quarto-monash)
- 🇳🇱 [uu.nl (Utrecht)](https://github.com/UtrechtUniversity/uu-quarto-presentation-template)
- 🏴󠁧󠁢󠁳󠁣󠁴󠁿 [ed.ac.uk (Edinburgh)](https://open.ed.ac.uk/how-to-make-a-professionally-sexy-quarto-presentation/)
- 🇬🇧 [warwick.ac.uk (Warwick)](https://github.com/warwick-stats-resources/warwickpres)
- 🇦🇺 [mq.edu.au (Sydney)](https://github.com/thomas-fung/quarto-mq-revealjs-theme)
- 🇺🇸 [gatech.edu (Atlanta, GA)](https://github.com/evannsmc/quarto-gatech-slides)
- 🇩🇰 [au.dk (Aarhus)](https://github.com/davidycliao/quarto-revealjs-aarhus)
- 🇺🇸 [unm.edu (Albuquerque, NM)](https://github.com/Data-Wise/dtslides)
 
## <span class="emoji">🗂️</span> Other AGH presentation templates
- [templates listed at the official agh.edu.pl page](https://www.agh.edu.pl/en/university/multimedia/presentation-templates)
