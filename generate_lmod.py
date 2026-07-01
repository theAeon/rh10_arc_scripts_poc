# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "mako>=1.3.12",
# ]
# ///

import glob
import pathlib
from mako.template import Template
from mako.lookup import TemplateLookup


def main() -> None:
    modlist = glob.glob("**/*.lua.mako", recursive=True)
    prefix_root = "/sw/arc/pkgs"
    dirs = TemplateLookup(directories=["./"])
    for pathstr in modlist:
        pathpath = pathlib.Path(pathstr[:-5])  # remove .mako suffix
        program_ver = pathpath.stem
        program_name = pathpath.parent.stem
        base = Template(filename=pathstr, lookup=dirs)
        print(base.render(root=prefix_root,
              ver=program_ver, name=program_name))


if __name__ == "__main__":
    main()
