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
rmunisy *path_files_to_patch* -i *path_file_with_unicode* -o *output_directory*
```

**WINDOWS ONLY** you have to esplicity run the script with python

### Format of file contain the unicode characters to remove

Each unicode must be write as a decimal number and in a different line. (see [Example](https://github.com/Daerckdev/font-rmunisy/blob/Master/unicode_exemple.txt))
