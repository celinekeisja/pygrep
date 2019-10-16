import re
import argparse
import os
import glob


def recursive(file_pattern, path, expr, compiled):
    ''' Return all files that includes the expression recursively. '''
    for r, d, f in os.walk(path):
        abspath = os.path.join(r, file_pattern)
        for apath in glob.glob(abspath):
            with open(apath, 'r', encoding='utf-8') as f:
                text = f.read()
                match = compiled.finditer(text)
                for m in match:
                    print(f'{os.path.basename(apath)} \t {m.group(0)}')


def ignore_case(expr):
    ''' Include the re.IGNORECASE to ignore cases of given expression. '''
    compiled = re.compile(r'{}.*'.format(expr), re.IGNORECASE)
    return compiled


def compile(expr):
    ''' Compile the expression. '''
    compiled = re.compile(r'{}.*'.format(expr))
    return compiled


def grep(file_pattern, path, expr,  compiled):
    ''' Print all the names of the files that contain the specific expression in the specified directory. '''
    for r, d, f in os.walk(path):
        d_path = os.path.abspath(r)
        abspath = os.path.join(d_path, file_pattern)
        for apath in glob.glob(abspath):
            with open(apath, 'r', encoding='utf-8') as f:
                text = f.read()
                match = compiled.finditer(text)
                for m in match:
                    print(f'{os.path.basename(apath)} \t {m.group(0)}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("regular_expression")
    parser.add_argument("file_pattern")
    parser.add_argument("path")
    parser.add_argument("-i", "--ignore_case", action="store_true")
    parser.add_argument("-v", "--invert_match", action="store_true")
    parser.add_argument("-r", "--recursive", action="store_true")

    args = parser.parse_args()
    file = args.file_pattern
    file_path = args.path
    expression = args.regular_expression

    if args.ignore_case:
        grep(file, file_path, expression, ignore_case(expression))
    elif args.invert_match:
        expression = f'.[^"{expression}"].+'
        grep(file, file_path, expression, compile(expression))
    elif args.recursive:
        recursive(file, file_path, expression, compile(expression))
    else:
        grep(file, file_path, expression, compile(expression))

