# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "mako>=1.3.12",
# ]
# ///

import pathlib
import sys
from argparse import ArgumentParser
from mako.template import Template
from mako.lookup import TemplateLookup


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('script', help='Path to the build script', nargs='+')
    args = parser.parse_args(sys.argv[1:])
    prefix_root = "/sw/arc/pkgs"
    dirs = TemplateLookup(directories=["./"])
    for pathstr in args.script:
        pathpath = pathlib.Path(pathstr)
        program_ver = pathpath.name
        program_name = pathpath.parent.stem
        base = Template(filename=f'{pathstr}.lua.mako', lookup=dirs)
        print(base.render(root=prefix_root,
              ver=program_ver, name=program_name))


if __name__ == "__main__":
    main()
