# Distributed Systems challenge by fly.io

Attempting the https://fly.io/dist-sys challenge

## Installation

### 1. Maelstrom

To get started with the challenge, we need to install [maelstrom](https://github.com/jepsen-io/maelstrom/blob/main/doc/01-getting-ready/index.md)

#### MacOS (using homebrew)

```bash
brew install openjdk graphviz gnuplot
wget https://github.com/jepsen-io/maelstrom/releases/download/v0.2.4/maelstrom.tar.bz2
tar -xjf maelstrom.tar.bz2
rm maelstrom.tar.bz2
```

Now maelstrom is installed locally under `./maelstrom/maelstrom`

### 2. Build Tools

#### MacOS (using homebrew)

```bash
# Install Conan (C++ package manager)
brew install conan

# Install CMake (build system)
brew install cmake

# Install GCC 15 (C++23 compiler)
brew install gcc@15

# Install Ninja (build tool)
brew install ninja

# Configure Conan profile
conan profile detect --force
```

## Project Setup

### 1. Install Dependencies with Conan

This project uses [Conan](https://conan.io/) for dependency management. Install dependencies:

```bash
# Install Release dependencies
conan install . --output-folder=build --build=missing -s build_type=Release

# Optional: Install Debug dependencies
conan install . --output-folder=build-debug --build=missing -s build_type=Debug
```

This will:
- Download and build Boost 1.90.0 (and its dependencies)
- Generate CMake configuration files in the `build/` directory
- Create `conan_toolchain.cmake` for CMake integration

### 2. Build the Project

#### Using CMake Presets (Recommended)

The project uses CMake presets for easy configuration:

```bash
cd example
cmake --preset conan-release
cmake --build --preset conan-release
```

#### From Root Directory

```bash
cmake -S example --preset conan-release
ninja -C build all
```

#### Run the Example

```bash
./build/example
```

## Project Structure

```
fly-io-dist-sys-cpp/
├── example/                 # Example project
│   ├── CMakeLists.txt      # CMake configuration
│   ├── CMakePresets.json   # CMake presets (Debug/Release)
│   └── main.cpp            # Example code using Boost.JSON
├── build/                  # Release build directory
├── build-debug/            # Debug build directory
├── conanfile.txt          # Conan dependencies
├── .vscode/               # VS Code settings
│   └── settings.json      # CMake Tools configuration
└── maelstrom/             # Maelstrom testing framework
```

## Dependencies

- **Boost 1.90.0** - C++ libraries (using Boost.JSON)
- **GCC 15** - C++23 compiler
- **CMake 3.20+** - Build system
- **Ninja** - Build tool

## Build Configurations

- **Release**: Optimized build, uses `build/` directory
- **Debug**: Debug symbols, uses `build-debug/` directory

Both configurations use separate Conan package installations to avoid conflicts.

## Troubleshooting

### Toolchain file not found

If you get an error about `conan_toolchain.cmake` not found, regenerate it:

```bash
conan install . --output-folder=build --build=missing -s build_type=Release
```

### Boost not found

Ensure:
1. Conan dependencies are installed
2. You're using the CMake preset (which loads the toolchain file)
3. The build directory contains `BoostConfig.cmake`