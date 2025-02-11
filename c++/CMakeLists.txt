cmake_minimum_required(VERSION 3.22)
project(BAEKJOON)

set(CMAKE_CXX_STANDARD 20)

# 모든 .cpp 파일들을 가져옴
file(GLOB_RECURSE APP_SOURCES */*.cpp)

# 모든 .cpp 파일을 하나의 실행 파일로 컴파일
add_executable(a.out ${APP_SOURCES})
add_executable(2753 boj/2753.cpp)
set_target_properties(2753 PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/boj/")