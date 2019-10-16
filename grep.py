import re
import argparse
import os


'''def grep(given_file, path, pattern):
    """ Read text in the given file. """
    p = re.compile(r'{}.*'.format(pattern))
    files = f'{path}/{given_file}'
    for r, d, f in os.walk(path):
        for text in f:
            abspath = os.path.join(d, text)
            if given_file.match(abspath):
                yield abspath
           result = p.search(text)
            print(f'{file} \t {result.group(0)}')'''

def grep(file, search):
    pattern = re.compile(r'{}.*'.format(search))
    with open(file, 'r') as f:
        text = f.read()
        res = pattern.finditer(text)

        for r in res:
            print(f'{file} \t {r.group(0)}')


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
    # grep(file, expression)

