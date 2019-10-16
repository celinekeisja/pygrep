import re
import argparse
import os
import glob


def ignore_case(expr):
    compiled = re.compile(r'{}.*'.format(expr), re.IGNORECASE)
    return compiled


def compile(expr):
    compiled = re.compile(r'{}.*'.format(expr))
    return compiled


def grep(file_pattern, path, expr, compiled):
    for r, d, f in os.walk(path):
        for fname in f:
            d_path = os.path.abspath(r)
            name = os.path.basename(fname)
            abspath = os.path.join(d_path, name)
            for apath in glob.glob(abspath):
                with open(apath, 'r') as f:
                    text = f.read()
                    match = compiled.finditer(text)
                    for m in match:
                        print(f'{name} \t {m.group(0)}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("regular_expression")
    parser.add_argument("file_pattern")
    parser.add_argument("path")
    parser.add_argument("-i", "--ignore_case", action="store_true")

    args = parser.parse_args()
    file = args.file_pattern
    file_path = args.path
    expression = args.regular_expression

    if args.ignore_case:
        grep(file, file_path, expression, ignore_case(expression))
    else:
        grep(file, file_path, expression, compile(expression))

