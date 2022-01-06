import fontforge, sys, os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('font_path', help='The path to the font to patch')

args = parser.parse_args()

if not os.path.isfile(args.font_path):
    sys.exit(f"{args.font_path} is not a file")

font = fontforge.open(args.font_path)

with open("unicode.txt", "r") as file:
    unicodes = [int(u) for u in file.read().strip().split("\n")]

for unicode in unicodes:
    font.selection.select(("unicode", None), unicode)
    font.clear()

# print(list(font.selection))
font.generate("build/output.ttf", flags=('opentype'))

