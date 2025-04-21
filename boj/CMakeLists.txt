cmake_minimum_required(VERSION 3.24)
project(baekjoon)
set(CMAKE_CXX_STANDARD 17)

# 현재 디렉토리 기준으로 하위 문제 폴더 검색 (1000/, 1001/ 등)
file(GLOB_RECURSE problem_sources CONFIGURE_DEPENDS RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "1*/main.cpp")

foreach(src_path ${problem_sources})
    # src_path 예: 1000/main.cpp
    get_filename_component(folder ${src_path} DIRECTORY)
    set(target_name "boj_${folder}")

    add_executable(${target_name} ${src_path})

    # 실행 파일을 각 문제 폴더에 생성
    set_target_properties(${target_name} PROPERTIES
            RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/${folder}
    )
endforeach()