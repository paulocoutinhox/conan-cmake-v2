cmake_minimum_required(VERSION 3.15)

project(hello CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED YES)

set(CMAKE_POLICY_DEFAULT_CMP0091 NEW)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "$<0:>${CMAKE_BINARY_DIR}/bin") # .exe and .dll
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "$<0:>${CMAKE_BINARY_DIR}/lib") # .so and .dylib
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "$<0:>${CMAKE_BINARY_DIR}/lib") # .lib and .a

# test variables
message(STATUS "Variable Before: MYVAR_FROM_CONANFILE_1 = ${MYVAR_FROM_CONANFILE_1}")
set(MYVAR_FROM_CONANFILE_1 "default-value" CACHE STRING "Variable From Conanfile")
message(STATUS "Variable After: MYVAR_FROM_CONANFILE_1 = ${MYVAR_FROM_CONANFILE_1}")

message(STATUS "Variable Before: MYVAR_FROM_CONANFILE_2 = ${MYVAR_FROM_CONANFILE_2}")
set(MYVAR_FROM_CONANFILE_2 "default-value" CACHE STRING "Variable From Conanfile")
message(STATUS "Variable After: MYVAR_FROM_CONANFILE_2 = ${MYVAR_FROM_CONANFILE_2}")

# test env variables
message(STATUS "Variable BITCODE: ${CMAKE_XCODE_ATTRIBUTE_ENABLE_BITCODE}")
message(STATUS "Variable ARC: ${CMAKE_XCODE_ATTRIBUTE_ENABLE_ARC}")
message(STATUS "Variable VISIBILITY: ${CMAKE_XCODE_ATTRIBUTE_ENABLE_VISIBILITY}")

# library
if (APPLE)
    set(SRC_FILES "src/hello.cpp" "src/hello-objc.m")
    set(HRD_FILES "include/hello.h" "include/hello-objc.h")
else()
    set(SRC_FILES "src/hello.cpp")
    set(HRD_FILES "include/hello.h")
endif()

add_library(${PROJECT_NAME} ${SRC_FILES})
target_include_directories(${PROJECT_NAME} PRIVATE include)

# public headers
set(PUBLIC_HEADERS ${HRD_FILES})
set_target_properties(${PROJECT_NAME} PROPERTIES PUBLIC_HEADER "${PUBLIC_HEADERS}")

# sqlite3
find_package(SQLite3 CONFIG REQUIRED)
target_link_libraries(${PROJECT_NAME} PRIVATE SQLite::SQLite3)

# sqlitecpp
find_package(SQLiteCpp CONFIG REQUIRED)
target_link_libraries(${PROJECT_NAME} PRIVATE SQLiteCpp)

# install
install(TARGETS ${PROJECT_NAME})
