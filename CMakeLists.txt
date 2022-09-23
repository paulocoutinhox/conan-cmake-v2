cmake_minimum_required(VERSION 3.15)
project(hello CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED YES)

set(CMAKE_POLICY_DEFAULT_CMP0091 NEW)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "$<0:>${CMAKE_BINARY_DIR}/bin") # .exe and .dll
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "$<0:>${CMAKE_BINARY_DIR}/lib") # .so and .dylib
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "$<0:>${CMAKE_BINARY_DIR}/lib") # .lib and .a

add_library(${PROJECT_NAME} src/hello.cpp)
target_include_directories(${PROJECT_NAME} PRIVATE include)

find_package(SQLite3 REQUIRED CONFIG)
target_link_libraries(${PROJECT_NAME} PRIVATE ${SQLite3_LIBRARIES})
target_include_directories(${PROJECT_NAME} PRIVATE ${SQLite3_INCLUDE_DIRS})
target_compile_definitions(${PROJECT_NAME} PRIVATE ${SQLite3_DEFINITIONS})

find_package(SQLiteCpp REQUIRED CONFIG)
target_link_libraries(${PROJECT_NAME} PRIVATE ${SQLiteCpp_LIBRARIES})
target_include_directories(${PROJECT_NAME} PRIVATE ${SQLiteCpp_INCLUDE_DIRS})
target_compile_definitions(${PROJECT_NAME} PRIVATE ${SQLiteCpp_DEFINITIONS})

set_target_properties(${PROJECT_NAME} PROPERTIES PUBLIC_HEADER "include/hello.h")

install(TARGETS ${PROJECT_NAME})
