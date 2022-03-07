cmake_minimum_required(VERSION 3.21)
project(Lab7)

set(CMAKE_CXX_STANDARD 23)

find_package(MPI REQUIRED)

include_directories(${MPI_INCLUDE_PATH})

add_executable(on2 on2.cpp)
add_executable(karatsuba karatsuba.cpp)

target_link_libraries(on2 PUBLIC ${MPI_LIBRARIES})
target_link_libraries(karatsuba PUBLIC ${MPI_LIBRARIES})

if(MPI_COMPILE_FLAGS)
    set_target_properties(on2 PROPERTIES COMPILE_FLAGS "${MPI_COMPILE_FLAGS}")
    set_target_properties(karatsuba PROPERTIES COMPILE_FLAGS "${MPI_COMPILE_FLAGS}")
endif()

if(MPI_LINK_FLAGS)
    set_target_properties(on2 PROPERTIES LINK_FLAGS "${MPI_LINK_FLAGS}")
    set_target_properties(karatsuba PROPERTIES LINK_FLAGS "${MPI_LINK_FLAGS}")
endif()