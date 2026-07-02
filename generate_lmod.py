# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "mako>=1.3.12",
# ]
# ///

import pathlib
import sys
from argparse import ArgumentParser
from mako.template import Template  # type: ignore
from mako.lookup import TemplateLookup  # type: ignore


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('script', help='Path to the build script', nargs='+')
    args = parser.parse_args(sys.argv[1:])
    prefix_root = "/sw/arc/pkgs"
    module_root = "/sw/arc/modules"
    dirs = TemplateLookup(directories=["./"])
    for pathstr in args.script:
        pathpath = pathlib.Path(pathstr)
        program_ver = pathpath.name
        program_name = pathpath.parent.stem
        base = Template(filename=f'{pathstr}.lua.mako', lookup=dirs,
                        input_encoding='utf-8', output_encoding='utf-8')
        (pathlib.Path(module_root) / pathpath.parent).mkdir(parents=True, exist_ok=True)
        with open(f"{module_root}/{pathstr}.lua", "wb") as f:
            f.write(base.render(root=prefix_root,
                                ver=program_ver, name=program_name))  # type: ignore


if __name__ == "__main__":
    main()
