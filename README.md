# Distributed Sytems challenge by fly.io

Attempting the https://fly.io/dist-sys challenge

## Installation

1. Maelstorm

To get started with the challenge, we need to install [maelstrom](https://github.com/jepsen-io/maelstrom/blob/main/doc/01-getting-ready/index.md)

### MacOS (using homebrew)

```bash
brew install openjdk graphviz gnuplot
wget https://github.com/jepsen-io/maelstrom/releases/download/v0.2.4/maelstrom.tar.bz2
tar -xjf maelstrom.tar.bz2
rm maelstrom.tar.bz2
```

Now maelstorm is installed locally under `./maelstrom/maelstrom`

2. Conan + CMake

```bash
brew install conan cmake
conan profile detect --force
```



