cmake_minimum_required(VERSION 3.0)
project(buildingStuff)

add_library(stlib STATIC source/block.c)
add_executable(static_block program.c)
target_link_libraries(static_block stlib)

add_library(shlib SHARED source/block.c)
add_executable(dynamic_block program.c)
target_link_libraries(dynamic_block shlib)