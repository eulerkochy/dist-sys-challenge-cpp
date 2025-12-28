#!/usr/bin/env python3
import argparse
import shutil
import subprocess
from pathlib import Path


def run(cmd: list[str]) -> None:
    print(f"$ {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def clean_cmake_cache(build_dir: str) -> None:
    """Remove CMake cache to avoid stale configuration issues."""
    cache_file = Path(build_dir) / "CMakeCache.txt"
    cmake_files = Path(build_dir) / "CMakeFiles"
    if cache_file.exists():
        cache_file.unlink()
    if cmake_files.exists():
        shutil.rmtree(cmake_files)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build and test workloads")
    parser.add_argument("workload", nargs="?", default="echo", help="Workload to build and test (default: echo)")
    parser.add_argument("--debug", action="store_true", help="Use debug build")
    parser.add_argument("--build-only", action="store_true", help="Only build, don't run tests")
    parser.add_argument("--node-count", type=int, default=1, help="Number of nodes (default: 1)")
    parser.add_argument("--time-limit", type=int, default=10, help="Time limit in seconds (default: 10)")
    parser.add_argument("--compiler", type=str, help="Compiler to use (e.g., gcc)")
    parser.add_argument("--compiler-version", type=str, help="Compiler version (e.g., 13)")
    parser.add_argument("--cppstd", type=str, default="23", help="C++ standard version (default: 23)")
    args = parser.parse_args()

    # Validate compiler arguments
    if (args.compiler and not args.compiler_version) or (args.compiler_version and not args.compiler):
        parser.error("--compiler and --compiler-version must be specified together")

    build_type = "Debug" if args.debug else "Release"
    preset = "conan-debug" if args.debug else "conan-release"
    build_dir = "build-debug" if args.debug else "build"

    # Conan install
    print(f"Installing dependencies ({build_type})...")
    conan_cmd = ["conan", "install", ".",
        f"--output-folder={build_dir}",
        "--build=missing",
        "-s", f"build_type={build_type}",
        "-s", f"compiler.cppstd={args.cppstd}",
        "-c", "tools.cmake.cmaketoolchain:generator=Ninja"]
    
    if args.compiler and args.compiler_version:
        conan_cmd.extend([
            "-s", f"compiler={args.compiler}",
            "-s", f"compiler.version={args.compiler_version}"
        ])
    
    run(conan_cmd)

    # Clean stale CMake cache and build
    clean_cmake_cache(build_dir)
    print(f"\nBuilding {args.workload} ({build_type})...")
    run(["cmake", "--preset", preset])
    run(["cmake", "--build", "--preset", preset, "--target", args.workload])

    if args.build_only:
        return

    # Run maelstrom test
    print(f"\nRunning maelstrom test for {args.workload}...")
    run([
        "./maelstrom/maelstrom", "test",
        "-w", args.workload,
        "--bin", f"./{build_dir}/{args.workload}/{args.workload}",
        "--node-count", str(args.node_count),
        "--time-limit", str(args.time_limit),
    ])


if __name__ == "__main__":
    main()
