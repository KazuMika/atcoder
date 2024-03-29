# -*- coding: utf-8 -*-

from pathlib import Path
import shutil
import argparse

names = ['a.py', 'b.py', 'c.py', 'd.py', 'e.py']


def make_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--which", type=str, default=None)
    parser.add_argument("--dst", type=str, default=None)
    parser.add_argument("--src", type=str, default=None)
    args = parser.parse_args()
    return args


def make_data(src):
    root = Path(src)
    problems_path = root / 'problems'

    content = ''
    with open(str(root / 'utils' / "xcontents.py"), 'r') as fo:
        for line in fo.readlines():
            content += line
    content = content[:-1]  # remove /n

    for idx in range(100, 334):
        idx = f"{idx:03}"
        dir_path = problems_path / idx
        if dir_path.exists():
            shutil.rmtree(dir_path)
        dir_path.mkdir(parents=True, exist_ok=True)
        for name in names:
            name = idx + '_' + name
            fp = dir_path / name
            with open(str(fp), 'w') as fo:
                print(content, file=fo)


def change_name(src):
    root = Path(src)
    problems_path = root / 'problems'
    main_files = sorted(list(problems_path.rglob('*.py')))
    for path in main_files:
        rank = path.parent
        con_num = str(path.parent.parent.stem)[3:]
        new_name = con_num + rank.name.lower() + '.py'
        new_name = 'main.py'
        path.rename(path.parent / new_name)
        new_name = rank.name.upper()
        rank.rename(rank.parent / new_name)


def main():
    args = make_args()
    if args.which == 'make_data':
        make_data(args.src)
    elif args.which == 'change_name':
        change_name(args.src)


if __name__ == '__main__':
    main()
