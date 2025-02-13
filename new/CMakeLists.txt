cmake_minimum_required(VERSION 3.30)
project(boj)

set(CMAKE_CXX_STANDARD 20)

# 가장 최근 수정된 .cpp 파일 찾기
execute_process(
        COMMAND bash -c "ls -t *.cpp | head -n 1"
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        OUTPUT_VARIABLE TARGET_FILE
        OUTPUT_STRIP_TRAILING_WHITESPACE
)

# 파일 경로가 제대로 설정되었는지 확인
message(STATUS "Target file: ${TARGET_FILE}")

add_executable(boj ${CMAKE_CURRENT_SOURCE_DIR}/${TARGET_FILE})
add_executable(Out boj/2798.cpp)
