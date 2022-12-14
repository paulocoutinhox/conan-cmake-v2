# Conan CMake V2

This is a test project to understand how Conan V2 works with a complex layout.

<p align="center">
    <a href="https://github.com/paulocoutinhox/conan-cmake-v2/actions/workflows/linux.yml"><img src="https://github.com/paulocoutinhox/conan-cmake-v2/actions/workflows/linux.yml/badge.svg"></a>
    <a href="https://github.com/paulocoutinhox/conan-cmake-v2/actions/workflows/macos.yml"><img src="https://github.com/paulocoutinhox/conan-cmake-v2/actions/workflows/macos.yml/badge.svg"></a>
    <a href="https://github.com/paulocoutinhox/conan-cmake-v2/actions/workflows/ios.yml"><img src="https://github.com/paulocoutinhox/conan-cmake-v2/actions/workflows/ios.yml/badge.svg"></a>    
    <a href="https://github.com/paulocoutinhox/conan-cmake-v2/actions/workflows/android.yml"><img src="https://github.com/paulocoutinhox/conan-cmake-v2/actions/workflows/android.yml/badge.svg"></a>    
    <a href="https://github.com/paulocoutinhox/conan-cmake-v2/actions/workflows/wasm.yml"><img src="https://github.com/paulocoutinhox/conan-cmake-v2/actions/workflows/wasm.yml/badge.svg"></a>
    <a href="https://github.com/paulocoutinhox/conan-cmake-v2/actions/workflows/catalyst.yml"><img src="https://github.com/paulocoutinhox/conan-cmake-v2/actions/workflows/catalyst.yml/badge.svg"></a>    
    <a href="https://github.com/paulocoutinhox/conan-cmake-v2/actions/workflows/ios-sim.yml"><img src="https://github.com/paulocoutinhox/conan-cmake-v2/actions/workflows/ios-sim.yml/badge.svg"></a>    
</p>

## How to build for generic desktop

Execute on terminal:

`make desktop`

## How to build for iOS

Execute on terminal:

`make ios`

## How to build for Android

Execute on terminal:

`make android`

## How to build for Web Assembly

Execute on terminal:

`make wasm`

## How to build for Catalyst

Execute on terminal:

`make catalyst`

## How to build for iOS Simulator

Execute on terminal:

`make ios-sim`

## Tree

This is the project structure when run `make tree`:

```
.
├── CMakeLists.txt
├── Makefile
├── README.md
├── conan
│   ├── darwin-toolchain
│   │   ├── README.md
│   │   ├── build.py
│   │   ├── conanfile.py
│   │   └── test_package
│   │       ├── CMakeLists.txt
│   │       ├── conanfile.py
│   │       └── src
│   │           └── example.cpp
│   ├── profiles
│   │   ├── android_profile
│   │   ├── catalyst_profile
│   │   ├── ios_profile
│   │   ├── ios_sim_profile
│   │   └── wasm_profile
│   └── recipe
│       └── conanfile.py
├── include
│   ├── hello-objc.h
│   └── hello.h
├── requirements.txt
├── src
│   ├── hello-objc.m
│   └── hello.cpp
└── test_package
    ├── CMakeLists.txt
    ├── conanfile.py
    └── src
        └── example.cpp

10 directories, 23 files
```
