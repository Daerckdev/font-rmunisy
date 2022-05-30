# R(e)M(ove)Uni(code)(ea)sy

RMUnisy is a python tool to easily remove specific unicode characters from font files.

### Why?

Some fonts, which i like, occupy some unicode characters reserved for emoji;
so they make more difficult to correctly set up fonts.

# Installation

For now you can only install it by cloning this repository:

```
git clone https://github.com/Daerckdev/font-rmunisy.git
```

## Dependency

To use this tool you must have installed:

- [Python3](https://www.python.org/downloads/)
- [python-fontforge](https://github.com/fontforge/fontforge) (this is required to modify font files)

# Usage

Run the script with the correct auguments:

```
rmunisy *path_files_to_patch* -i *unicode_chars_to_delete*
```

Every unicodes characters must be write as a **decimal number**. (e.g. U**263A** -> **9786**)

**\*WINDOWS ONLY\*** you have to esplicity run the script with python

## Program Arguments

| Argument | Required | Help | Notes |
| :--- | :--- | :--- | :--- |
| `--help` <br/>`-h` | No | Print the help section | |
| `-i` | If there <br/>is no `-if` | Get unicode characters to delete as a string | Chars must be separted by a space |
| `-if` | If there <br/>is no `-i` | Get unicode characters to delete by a file | Each chars must be in a different line (see [Example](https://github.com/Daerckdev/font-rmunisy/blob/Master/unicode_exemple.txt)) |
| `-e` | No | Treats input unicodes as hexadecimal | By default they will be treat as decimal |
| `-o` | No | Output directory | By default is the working directory |
| `--mark=` | No | String to add to the patched file's name | |

