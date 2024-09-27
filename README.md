# PB

## Overview

`pb` is a copy/paste utility for CLI using STDIN and STDOUT.

## Packaging

Use pyinstaller to create a standalone executable.

```bash
$ pip install pyinstaller
$ pyinstaller --onefile pb.py
```

## Usage

```bash
Usage: pb [--help] COMMAND

pb: Copy/paste CLI utility.

Commands:
  copy      Write to your clipboard the content from STDIN
  paste     Write to STDOUT the contents of your clipboard
```

## Examples

```bash
$ echo test | pb copy

$ pb paste
test
```
