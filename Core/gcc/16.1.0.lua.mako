<%include file=".pkgInfo.lua.mako"/>
<%include file="../compiler.mako"/>


-- compile and link flag variables
setenv('GCC_ROOT',    installDir)
setenv('GCC_LIB',     pathJoin(installDir,"lib64"))
setenv('GCC_INCLUDE', pathJoin(installDir,"include"))

-- set compilation variables for include files and compiler command names
setenv('CPATH',                 pathJoin(installDir,"/lib/gcc/x86_64-pc-linux-gnu/${ver}/include"))
prepend_path('CPATH',           pathJoin(installDir,"/lib/gcc/x86_64-pc-linux-gnu/${ver}/include-fixed"))
setenv('CC',  pathJoin(installDir,"bin", "gcc"))
setenv('CXX', pathJoin(installDir,"bin", "g++"))
setenv('FC',  pathJoin(installDir,"bin", "gfortran"))
setenv('C_INCLUDEPATH', pathJoin(installDir,"include"))
