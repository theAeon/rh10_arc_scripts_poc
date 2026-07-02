<%include file="../base.mako"/>

-- set this as a compiler and add its modules to MODULEPATH
family('compiler')
local module_root  = '/sw/modules/Compilers/${name}/${ver}'
prepend_path("MODULEPATH", module_root)
