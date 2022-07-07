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

By default every unicodes characters must be written as a **decimal number** (e.g. (U)**263A** -> **9786**), to use another base use the `-b` argument.

**\*WINDOWS ONLY\*** you have to esplicity run the script with python

## Program Arguments

| Argument | Required | Help | Notes |
| :--- | :--- | :--- | :--- |
| `--help` <br/>`-h` | No | Print the help section | |
| `-i` `--input` | If there <br/>is no `-if` | A string with the unicode characters to remove | Chars must be separted by a space |
| `-if` `--input-file` | If there <br/>is no `-i` | The path of the file contain the unicodes to delete | Each chars must be in a different line (see [Example](https://github.com/Daerckdev/font-rmunisy/blob/Master/unicode_exemple.txt)) |
| `-b` `--base` | No | The number base of the unicodes in input. (usually 10 or 16) | By default the number base is 10 |
| `-o` `--output-dir` | No | Output directory | By default is the working directory |
| `-m` `--mark=` | No | String to add to the patched file's name | |

## Special characters for input

### Range

You can select a range of unicodes by putting `-` between them without spaces.
```
rmunisy *fonts* -i "1 5 3 50-100"
```

