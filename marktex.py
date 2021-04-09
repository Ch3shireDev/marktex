import sys
import os
from shutil import move
from tools import split_filename


def main(*args):
    filename = None
    flags = []
    for arg in args:
        if arg.startswith('-'):
            flags.append(arg)
        elif filename is None:
            filename = arg

    if filename.startswith('.\\'):
        filename = filename.replace('.\\', '')

    with open(filename, encoding='utf-8') as f:
        data = f.read()
        f.close()

    _, old_file = os.path.split(filename)
    base, ext = split_filename(old_file)
    new_file = f"{base}_tmp.{ext}"

    with open(new_file, 'w+', encoding='utf-8') as f:
        f.write(data)
        f.close()

    result = os.system(str.join(' ', ['pdflatex', new_file] + list(args)))

    if result == 0:
        move(f"{base}_tmp.pdf", f"{base}.pdf")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Arguments required!")
        exit()
    args = sys.argv[1:]
    main(*args)
