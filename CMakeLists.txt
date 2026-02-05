cmake_minimum_required(VERSION 3.16)
project(bl-class LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(COMMON_FLAGS
	-Wall
	-Wextra
	-Werror
	-pedantic
	-march=native
)

add_executable(${PROJECT_NAME} app/main.cpp)
target_compile_options(${PROJECT_NAME} PRIVATE ${COMMON_FLAGS})
