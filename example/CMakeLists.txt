cmake_minimum_required(VERSION 3.20)

# Use GCC 15 on macOS if available, otherwise use system default
if(APPLE AND EXISTS /opt/homebrew/bin/g++-15)
    set(CMAKE_CXX_COMPILER /opt/homebrew/bin/g++-15 CACHE FILEPATH "C++ compiler")
endif()

# Generate compile_commands.json for clangd
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)


set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Set build type (required by Conan)
if (CMAKE_BUILD_TYPE STREQUAL "Release")
    set(CONAN_TOOLCHAIN_FILE ${CMAKE_CURRENT_SOURCE_DIR}/../build/conan_toolchain.cmake)
else()
    set(CONAN_TOOLCHAIN_FILE ${CMAKE_CURRENT_SOURCE_DIR}/../build-debug/conan_toolchain.cmake)
endif()
include(${CONAN_TOOLCHAIN_FILE})

# Prefer config-based find_package (for Conan)
set(CMAKE_FIND_PACKAGE_PREFER_CONFIG ON)
if(POLICY CMP0167)
    cmake_policy(SET CMP0167 NEW)
endif()

project(example VERSION 0.1.0 LANGUAGES CXX)

find_package(Boost REQUIRED COMPONENTS json)

add_executable(example main.cpp)

target_link_libraries(example PRIVATE Boost::json)
