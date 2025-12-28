cmake_minimum_required(VERSION 3.20)

# Use GCC 15
set(CMAKE_CXX_COMPILER /opt/homebrew/bin/g++-15 CACHE FILEPATH "C++ compiler")

# Generate compile_commands.json for clangd
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(example VERSION 0.1.0 LANGUAGES CXX)

add_executable(example main.cpp)
