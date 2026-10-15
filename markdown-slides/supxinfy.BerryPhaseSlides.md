# Typst Slides: Berry's Phase for Quantum Graphs

This repository contains two [Typst](https://typst.app) / [Touying](https://github.com/touying-typ/touying) slide decks presenting research on **Berry's phase under topology changes** (the figure-eight graph model), at two different levels and for two different audiences.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./readme-assets/topology-change-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./readme-assets/topology-change-light.svg">
    <img alt="Topology change cycle" src="assets/topology_change-light.svg" width="81%">
  </picture>
</p>

| Folder | Audience | Description |
|---|---|---|
| [`mathclub-talk/`](./mathclub-talk) | General / [Матклуб](https://t.me/club_math/80) seminar audience | An accessible introduction to graph theory, building up to the main result. |
| [`msc-thesis-defense/`](./msc-thesis-defense) | Thesis committee | The full MSc thesis defense presentation: model, secular equation, and the Berry's phase theorem. |

Each folder is self-contained — with its own `main.typ`, `README.md`, `LICENSE`, and assets — and can be built independently.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="readme-assets/figure-eight-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="readme-assets/figure-eight-light.svg">
    <img alt="Figure-eight graph" src="assets/figure_eight-light.svg" width="81%">
  </picture>
</p>

Related preprint: [arXiv:2605.10798](https://arxiv.org/pdf/2605.10798)

You can also find slides for bachelor's presentation [here](https://github.com/supxinfy/Diplom-slides)

---

## Quick start

Both decks are plain Typst projects and follow the same basic workflow:

```bash
cd mathclub-talk        # or msc-thesis-defense
typst compile main.typ
```

---

## Citing

If you build on the results presented in either deck, please cite the accompanying preprint:

```
P. Kurasov, V. Shubin, A. Tibbling, "Berry's Phase under Topology Change", arXiv:2605.10798.
```
