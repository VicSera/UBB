cmake_minimum_required(VERSION 3.17)
project(MultiplexChatClient C)
project(MultiplexChatServer C)

set(CMAKE_C_STANDARD 99)

add_executable(MultiplexChatClient client.c)
add_executable(MultiplexChatServer server.c)