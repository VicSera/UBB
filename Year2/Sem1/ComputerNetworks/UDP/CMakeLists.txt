cmake_minimum_required(VERSION 3.17)
project(UDP C)

set(CMAKE_C_STANDARD 11)

add_executable(UDP client.c server.c)
link_libraries(lws2_32)