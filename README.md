# Distributed Systems Challenge by fly.io

Attempting the https://fly.io/dist-sys challenge in C++.

## Prerequisites

### Maelstrom

```bash
brew install openjdk graphviz gnuplot
sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
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
# Install dependencies (or just use run.py which handles this)
conan install . --output-folder=build --build=missing -s build_type=Release -c tools.cmake.cmaketoolchain:generator=Ninja
conan install . --output-folder=build-debug --build=missing -s build_type=Debug -c tools.cmake.cmaketoolchain:generator=Ninja

# Build and test echo workload
python3 run.py echo

# Or build and run manually
cmake --preset conan-release
cmake --build --preset conan-release
./maelstrom/maelstrom test -w echo --bin ./build/echo/echo --node-count 1 --time-limit 10
```

### run.py Options

```bash
python3 run.py <workload>           # Build and test a workload
python3 run.py echo --debug         # Use debug build
python3 run.py echo --build-only    # Only build, skip tests
python3 run.py echo --node-count 3  # Run with 3 nodes
python3 run.py echo --time-limit 20 # Run for 20 seconds
```

For debug builds, use `build-debug` and `conan-debug` preset instead.

## Project Structure

```
fly-io-dist-sys-cpp/
├── CMakeLists.txt        # Root CMake configuration
├── conanfile.txt         # Dependencies (Boost)
├── run.py                # Build and test runner
├── maelstrom-cpp/        # Maelstrom C++ library
│   ├── maelstrom.h
│   └── maelstrom.cpp
├── echo/                 # Echo challenge
│   ├── CMakeLists.txt
│   └── main.cpp
├── example/              # Example project
│   ├── CMakeLists.txt
│   └── main.cpp
└── maelstrom/            # Maelstrom testing framework
```

## Troubleshooting

**Toolchain file not found**: Run `python3 run.py` or manually run `conan install . --output-folder=build --build=missing -s build_type=Release -c tools.cmake.cmaketoolchain:generator=Ninja`

**Boost not found**: Ensure Conan dependencies are installed and you're using the CMake preset.
