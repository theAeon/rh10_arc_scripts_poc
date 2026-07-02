-- local variables to be used inside the module file
local installDir   = "${root}/${name}/${ver}"
local app          = "${name}"
whatis("Version: ${ver}")

-- general system variables
prepend_path('PATH',            pathJoin(installDir,"bin"))
prepend_path('MANPATH',         pathJoin(installDir,"share/man"))
prepend_path('LD_LIBRARY_PATH', pathJoin(installDir,"lib64"))
prepend_path('LIBRARY_PATH',    pathJoin(installDir,"lib64"))
prepend_path('LD_RUN_PATH',     pathJoin(installDir,"lib64"))
