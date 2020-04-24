#!/usr/bin/env python3

import os


HEADER="""
> 👨‍💻 A repository for my solutions submitted for problems on LeetCode.

---

"""


def main():
    content = ""
    content += HEADER

    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github', 'assets'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)

        content += "### Problem {}:\n\n".format(category)

        for file in files:
            name = os.path.basename(file).split('.')[1]
            path = os.path.join(category, file)
            with open(path) as f:
                code = f.read()
                f.close()
            content += "- [{}]({})\n```{}```\n\n".format(name, path, code)
        content += "\n"

    with open("README.md", "w") as fd:
        fd.write(content)


if __name__ == "__main__":
    main()
