# Important Note: You'll probably want [Nix][nix-inst] instead.

Nix is a ridiculously powerful, declarative package manager that forces packages to play nice with each other. That includes the system glibc. [You can learn about nix here][nixtutor], and [you can check if your package is available here][nix-pkgs].

SteamOS 3.5 and above have a built-in overlay for the `/nix` directory, and Nix is designed to work with (effectively) immutable root filesystems, like those found on the Steam Deck. It's a purpose-built solution.

Rwfus is not tested with all packages in the SteamOS/Arch repositories, and many of them will install to locations not covered by the overlay. If you just need to install Yakuake, but don't want to unlock your Deck, this'll do the trick. If you're looking for anything more complex, I suggest Nix.

## Rwfus: Read-Write OverlayFS for your Steam Deck!
---

Like a vinyl couch cover for your filesystem, Rwfus covers your Deck's /usr/ directory (and some others) allowing you to initialize and use* pacman (the Arch Linux package manager) on the Steam Deck without losing packages when the next update comes out.

Directories covered in a default installation:
| Directory         | Contents               |
| ----------------- | ---------------------- |
| /etc/pacman.d     | `pacman` configuration |
| /usr              | Programs and libraries |
| /var/cache/pacman | Package cache          |

### * Jank warning

Due to the way Valve's firmware updates work, doing `pacman -S[y[y]]u` at any time will leave your system in a partially updated state. This may cause crashes, hangs, boot-loops, or other undesired behavior, and will be annoying to fix. If you run into this issue, you can disable the Rwfus service from the recovery console with `systemctl disable rwfusd.service`

### Installation:

1. Download the latest release from GitHub's [Releases][releases] page
2. `cd rwfus`
3. `./rwfus -i`

Then you're all set! Remember to periodically run `pacman -Sy` to update your repos

### Usage:

```
Rwfus v0.5.0
Carry Pacman across SteamOS updates!

USAGE:
    ./rwfus [FLAGS] [OPTIONS]

FLAGS:
    -h, --help          Show this help text, then exit
    -v, --version       Show the version number, then exit

    -i, --install*      Install or update Rwfus
    -u, --update*       Alias for --install
    -r, --remove*       Remove ALL FILES AND DIRECTORIES associated with Rwfus

    -e, --enable*       Activate overlays
    -d, --disable*      Deactivate overlays
    -s, --status        Get the status of the overlay-mounter and disk image

        --mount*        Mount Rwfus's disk image
        --umount*       Unmount Rwfus's disk image

    -t, --test          Use fake directory targets when performing operations
    -g, --gen-config    Generate a sample config file, which you can use to customize your install

    * flags marked with a star require root, unless the --test flag is set.

OPTIONS:
    -l, --logfile <path>    Specify the location of Rwfus's log file
                                Default: /var/log/rwfus.log
    -c, --config <path>     Specify a configuration file to use
                                Default: /opt/rwfus/
        --backup <dest>*    Backup Rwfus's disk image to (file path) <dest>
        --restore <src>*    Restore Rwfus's disk image from (file path) <src>

    * options marked with a star require root, unless the --test flag is set.
```

#### Examples:

> `rwfus`: Get status

> `rwfus --install`: Install Rwfus

> `rwfus --update`: Update Rwfus

> `rwfus --remove`: Remove Rwfus and all overlaid files

> `rwfus --gen-config`: Generate a sample config file in your present working directory

> `rwfus --config ./rwfus.conf`: Use a config file called `rwfus.conf` when setting up Rwfus

# Adding `rwfus` to your `$PATH`

To access the `rwfus` manager utility from anywhere, you may want to [add it to your PATH][archpath].

[releases]: https://github.com/ValShaped/rwfus/releases
[archpath]: https://wiki.archlinux.org/title/Environment_variables#Per_user
[nix-inst]: https://github.com/DeterminateSystems/nix-installer
[nix-pkgs]: https://search.nixos.org/packages
[nixtutor]: https://nix.dev/tutorials/
