# Podium

[![Podium logo](icons/podium.png)](https://podium.beeware.org/)

[![Discord server](https://img.shields.io/discord/836455665257021440?label=Discord%20Chat&logo=discord&style=plastic)](https://beeware.org/bee/chat/)

A markup-based slide presentation tool.

## Quickstart

Official releases of Podium can be downloaded from the [GitHub releases page](https://github.com/beeware/podium/releases).

Download the binary for your platform of choice, and run it. This should open a file dialog, prompting you to open a `.podium` slide deck. An example Podium slide deck is also available in the `releases` folder. Unzip the deck, and open it in Podium.

Controls from here are keyboard based:

- CMD-Shift-P - Enter presentation mode; or, if in presentation mode, Pause timer
- CMD-P - Open presentation in Print view
- Esc - Exit presentation mode
- CMD-Tab - Switch displays
- Right/Left arrows - Next/previous slide
- Down/Up arrows - Next/previous slide
- Enter - Next slide
- Home/End - first/last slide
- CMD-A - Switch aspect ratio between 16:9 and 4:3
- CMD-R - Reload slide deck
- CMD-T - Reset timer

If you're on Linux, "CMD" is the Control key.

## Developing Podium

Podium uses the [BeeWare](https://beeware.org) suite of tools and libraries -most notably, the [Toga](https://github.com/beeware/toga) widget toolkit, and the [Briefcase](https://github.com/beeware/briefcase) packaging tool.

To develop Podium, create a virtual environment, and install the BeeWare tools.

Then, you can create a virtual environment and install the BeeWare tools:

```console
$ mkdir beeware
$ cd beeware
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install briefcase
```

Now that you have the code, you can clone the Podium repository and run it in developer mode:

```console
(venv) $ git clone https://github.com/beeware/podium.git
(venv) $ cd podium
(venv) $ briefcase dev
```

This should open the same file dialog as before.

### Packaging with Briefcase

Use [Briefcase](https://github.com/beeware/briefcase) to package this repository as a standalone application:

```console
$ briefcase package
```

Depending on your platform, this will produce a `macOS` folder containing a Podium DMG file, or a `linux` folder containing a system package appropriate to your distribution (a .deb, .rpm or .pkg.zip file).

## Overriding Default themes

Define a `style.css` file to override the default theme. You can use the **Debugging** section to help you create a theme that suites your style.

## Debugging

If you need to debug the CSS for a slide, you may want to use the "inspect element" feature of the webview. You may need to manually enable the feature at an operating system level:

- **macOS**: at a terminal prompt, run:

    ```console
    > defaults write org.beeware.podium WebKitDeveloperExtras -bool true
    ```

## Documentation

Documentation for Podium can be found on [Read The Docs](https://podium.beeware.org/).

## Community

Podium is part of the [BeeWare suite](https://beeware.org). You can talk to the community through:

- [@beeware@fosstodon.org on Mastodon](https://fosstodon.org/@beeware)
- [Discord](https://beeware.org/bee/chat/)

We foster a welcoming and respectful community as described in our [BeeWare Community Code of Conduct](https://beeware.org/community/behavior/).

## Contributing

If you experience problems with Podium, [log them on GitHub](https://github.com/beeware/podium/issues).

If you want to contribute, please check out the [Contribution guide](https://podium.beeware.org/how-to/contribute/).
