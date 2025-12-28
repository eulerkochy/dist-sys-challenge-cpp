cmake_minimum_required(VERSION 4.0)

# Use Clang 21 from Homebrew for better module support
set(CMAKE_CXX_COMPILER /opt/homebrew/opt/llvm/bin/clang++)
set(CMAKE_C_COMPILER /opt/homebrew/opt/llvm/bin/clang)

# Enable import std; support - must be before project()
set(CMAKE_EXPERIMENTAL_CXX_IMPORT_STD "d0edc3af-4c50-42ea-a356-e2862fe7a444")
set(CMAKE_CXX_MODULE_STD ON)
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(modules_example VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Module library
add_library(math_module)
target_sources(math_module
    PUBLIC FILE_SET CXX_MODULES FILES
    math.cppm
)
target_compile_features(math_module PUBLIC cxx_std_23)

# Executable consuming the module
add_executable(modules_demo main.cpp)
target_link_libraries(modules_demo PRIVATE math_module)
target_compile_features(modules_demo PRIVATE cxx_std_23)
