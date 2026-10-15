# touying-unipd

[Touying](https://github.com/touying-typ/touying) theme inspired by [beamer-padova](https://www.math.unipd.it/~burattin/other/tema-latex-beamer-padova/), ported from [polylux-unipd](https://github.com/augustozanellato/polylux-unipd).

## Usage

```typst
#import "@preview/touying:0.7.4": *
#import "unipd.typ": *

#show: unipd-theme.with(
  config-info(
    title: "Random title",
    subtitle: "Discussione Tesi LT Informatica",
    author: "Mario Rossi",
    date: "20/04/2023",
  ),
)

#title-slide()

= My section

== My first slide

Slide content.
```

Sections are registered with level-1 headings (`= Section`) and shown on the right side of the slide header; level-2 headings (`== Title`) start a new slide with that title. Plain `#slide[...]` also works, along with `#focus-slide[...]` and `#slides-outline()`.

Dynamic content works the Touying way: `#pause`, `#uncover`, `#only`, `#alternatives`, `#item-by-item`, and so on — see the [Touying documentation](https://touying-typ.github.io/).

I'm too lazy to write a proper documentation so you'll have to figure it out yourself but an [example](./slides.typ) is provided, you can see it built [here](./slides.pdf).
