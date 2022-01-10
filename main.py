import fontforge
from pathlib import Path
from sys import exit as abort

class RMUnisy():
    def __init__(self, fonts: list, unicode_path: Path, output_dir: Path) -> None:
        # check arguments
        for font in fonts:
            self.is_file(font)
        self.is_file(unicode_path)
        self.is_dir(output_dir)

        # init object
        self.fonts = fonts
        self.unicode = self.get_unicode(unicode_path)
        self.output_dir = output_dir

    def is_file(self, path: Path) -> bool:
        if path.is_file():
            return True
        abort(f"RMUnisy: {path} is not a file.")

    def is_dir(self, path: Path) -> bool:
        if path.is_dir():
            return True
        abort(f"RMUnisy: {path} is not a directory.")

    def get_unicode(self, file: Path) -> list:
        with file.open() as file:
            unicodes = [int(u) for u in file.read().strip().split("\n")]
        return unicodes

    def patch(self, name_marked: bool=True) -> bool:
        if name_marked:
            name_mark = "-patched"
        else:
            name_mark = ""
        for path in self.fonts:
            font = fontforge.open(str(path))
            for unicode in self.unicode:
                font.selection.select(("unicode", None), unicode)
                font.clear()
            font.generate(f"{self.output_dir}/{path.stem}{name_mark}{path.suffix}")
            font.close()
        return True


def main():
    parser = ArgumentParser(description="Delete unicode characters from a font using FontForge")
    parser.add_argument('fonts_path', type=Path, nargs="+", help="The path to the fonts to patch")
    parser.add_argument('-i', dest="unicode", required=True, type=Path, help="The path of the file contain the unicodes to delete")
    parser.add_argument('-o', dest="output_dir", required=False, type=Path, default=Path("build"), help="Output Directory (default: working directory)")
    arguments_manager = parser.parse_args()

    program = RMUnisy(fonts=arguments_manager.fonts_path, unicode_path=arguments_manager.unicode, output_dir=arguments_manager.output_dir)
    program.patch(name_marked=False)

if __name__ == "__main__":
    from argparse import ArgumentParser
    main()

