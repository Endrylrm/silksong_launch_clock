import os
import shutil
import subprocess


def Build_Nuitka():
    subprocess.run(
        [
            ".venv/Scripts/python.exe",
            "-m",
            "nuitka",
            "--standalone",
            "--plugin-enable=upx",
            f"--upx-binary={os.getcwd()}/upx/upx.exe",
            "--enable-plugin=tk-inter",
            "--windows-console-mode=disable",
            "--windows-icon-from-ico=./images/icon.ico",
            "./src/main.py",
        ]
    )
    shutil.copytree("./images/", "./main.dist/images")
