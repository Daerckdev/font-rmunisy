import fontforge, sys
import argparse, pathlib

parser = argparse.ArgumentParser(description="Delete unicode characters from a font using FontForge")
parser.add_argument('fonts_path', type=pathlib.Path, nargs="+", help="The path to the fonts to patch")
parser.add_argument('-i', dest="to_delete", required=True, type=pathlib.Path, help="The path of the file contain the unicodes to delete")
parser.add_argument('-o', dest="output_dir", required=False, type=pathlib.Path, default=pathlib.Path("build"), help="Output Directory")

args = parser.parse_args()

for path in args.fonts_path:
    if not path.is_file():
        sys.exit(f"{args.fonts_path} is not a file.")

if not args.output_dir.is_dir():
    sys.exit(f"{args.output_dir} is not a directory.")

if args.to_delete.is_file():
    with args.to_delete.open() as file:
        unicodes = [int(u) for u in file.read().strip().split("\n")]
else:
    sys.exit(f"{args.to_delete} is not a file")

for path in args.fonts_path:
    font = fontforge.open(str(path))

    for unicode in unicodes:
        font.selection.select(("unicode", None), unicode)
        font.clear()

    file_name = str(path).split("/")[-1]
    font.generate(f"build/{file_name}", flags=('opentype'))

