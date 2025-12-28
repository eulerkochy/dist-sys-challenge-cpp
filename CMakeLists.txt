cmake_minimum_required(VERSION 3.20)

# Use GCC 15 on macOS if available
if(APPLE AND EXISTS /opt/homebrew/bin/g++-15)
    set(CMAKE_CXX_COMPILER /opt/homebrew/bin/g++-15 CACHE FILEPATH "C++ compiler")
endif()

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Conan toolchain
if(CMAKE_BUILD_TYPE STREQUAL "Release")
    set(CONAN_TOOLCHAIN_FILE ${CMAKE_CURRENT_SOURCE_DIR}/build/conan_toolchain.cmake)
else()
    set(CONAN_TOOLCHAIN_FILE ${CMAKE_CURRENT_SOURCE_DIR}/build-debug/conan_toolchain.cmake)
endif()
include(${CONAN_TOOLCHAIN_FILE})

set(CMAKE_FIND_PACKAGE_PREFER_CONFIG ON)
if(POLICY CMP0167)
    cmake_policy(SET CMP0167 NEW)
endif()

project(fly-io-dist-sys-cpp VERSION 0.1.0 LANGUAGES CXX)

find_package(Boost REQUIRED COMPONENTS json)

# maelstrom-cpp library
add_library(maelstrom-cpp STATIC maelstrom-cpp/maelstrom.cpp)
target_include_directories(maelstrom-cpp PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/maelstrom-cpp)
target_link_libraries(maelstrom-cpp PUBLIC Boost::json)

# Subdirectories
add_subdirectory(echo)
add_subdirectory(example)
