cmake_minimum_required(VERSION 3.30)
project(new)

set(CMAKE_CXX_STANDARD 20)

add_executable(new main.cpp)

add_executable(Out boj/5086.cpp
        boj/9506.cpp
)
