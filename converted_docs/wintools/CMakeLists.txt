project(wintools NONE)
cmake_minimum_required(VERSION 3.17.0)
set(CMAKE_VERBOSE_MAKEFILE "ON") 
set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake_modules")
message("the module path is ${CMAKE_SOURCE_DIR}/cmake_modules")
include(TargetCopyFiles)
set(to_dir "$ENV{CONDA_PREFIX}/trythis/thirdlevel")

add_custom_target(make-dir ALL 
    COMMAND ${CMAKE_COMMAND} -E make_directory ${to_dir})

add_custom_target(make_copy ALL)

add_copy_files(make_copy "binwin/jbwin.ps1" DESTINATION ${to_dir})
add_dependencies(make_copy make-dir)

#https://github.com/UCL/GreatCMakeCookOff/wiki/Target-for-copying-files-and-directories
