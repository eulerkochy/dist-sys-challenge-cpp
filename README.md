# Distributed Systems Challenge by fly.io

Attempting the https://fly.io/dist-sys challenge in C++.

## Prerequisites

### Maelstrom

```bash
brew install openjdk graphviz gnuplot
wget https://github.com/jepsen-io/maelstrom/releases/download/v0.2.4/maelstrom.tar.bz2
tar -xjf maelstrom.tar.bz2
rm maelstrom.tar.bz2
```

### Build Tools

```bash
brew install gcc@15 cmake ninja conan
conan profile detect --force
```

## Quick Start

```bash
# Install dependencies
conan install . --output-folder=build --build=missing -s build_type=Release

# Build
cmake -S example --preset conan-release
cmake --build --preset conan-release

# Run
./build/example
```

For debug builds, use `build-debug` and `conan-debug` preset instead.

## Project Structure

```
fly-io-dist-sys-cpp/
├── example/              # Example project
│   ├── CMakeLists.txt
│   ├── CMakePresets.json
│   └── main.cpp
├── conanfile.txt         # Dependencies (Boost 1.90.0)
└── maelstrom/            # Testing framework
```

## Troubleshooting

**Toolchain file not found**: Regenerate with `conan install . --output-folder=build --build=missing -s build_type=Release`

**Boost not found**: Ensure Conan dependencies are installed and you're using the CMake preset.
