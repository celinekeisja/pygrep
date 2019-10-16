import re
import argparse
import os
import glob


def grep(given_file, path, expr):
    compiled = re.compile(r'{}.*'.format(expr))
    for r, d, f in os.walk(path):
        for text in f:
            d_path = os.path.abspath(r)
            name = os.path.basename(text)
            abspath = os.path.join(d_path, name)
            for apath in glob.glob(abspath):
                with open(apath, 'r') as f:
                    text = f.read()
                    match = compiled.finditer(text)
                    for m in match:
                        print(f'{file} \t {m.group(0)}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("regular_expression")
    parser.add_argument("file_pattern")
    parser.add_argument("path")

    args = parser.parse_args()
    file = args.file_pattern
    file_path = args.path
    expression = args.regular_expression

    grep(file, file_path, expression)

