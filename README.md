# Silksong Launch Clock

a simple clock to check if silksong has launched on steam, built using tkinter, pillow (for images in tkinter) and pystray (System tray).

When the game launchs on steam on september 4, you will receive a message box notification at exactly 14:00 UTC.

# Dependencies:
- tkinter
- pillow = 11.3.0
- pystray = 0.19.5

# Developer Dependencies:
- Nuitka = 2.7.13

# Building
use the build script with [Poetry](https://python-poetry.org/).

<details>
<summary>Nuitka</summary>

> `poetry run build-nuitka`

</details>
