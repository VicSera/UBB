# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /snap/clion/103/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /snap/clion/103/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/victor/Desktop/Programming/UBB/OOP/LiviaDates

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/victor/Desktop/Programming/UBB/OOP/LiviaDates/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/LiviaDates.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/LiviaDates.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/LiviaDates.dir/flags.make

CMakeFiles/LiviaDates.dir/main.c.o: CMakeFiles/LiviaDates.dir/flags.make
CMakeFiles/LiviaDates.dir/main.c.o: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/victor/Desktop/Programming/UBB/OOP/LiviaDates/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/LiviaDates.dir/main.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/LiviaDates.dir/main.c.o   -c /home/victor/Desktop/Programming/UBB/OOP/LiviaDates/main.c

CMakeFiles/LiviaDates.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/LiviaDates.dir/main.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/victor/Desktop/Programming/UBB/OOP/LiviaDates/main.c > CMakeFiles/LiviaDates.dir/main.c.i

CMakeFiles/LiviaDates.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/LiviaDates.dir/main.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/victor/Desktop/Programming/UBB/OOP/LiviaDates/main.c -o CMakeFiles/LiviaDates.dir/main.c.s

# Object files for target LiviaDates
LiviaDates_OBJECTS = \
"CMakeFiles/LiviaDates.dir/main.c.o"

# External object files for target LiviaDates
LiviaDates_EXTERNAL_OBJECTS =

LiviaDates: CMakeFiles/LiviaDates.dir/main.c.o
LiviaDates: CMakeFiles/LiviaDates.dir/build.make
LiviaDates: CMakeFiles/LiviaDates.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/victor/Desktop/Programming/UBB/OOP/LiviaDates/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable LiviaDates"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/LiviaDates.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/LiviaDates.dir/build: LiviaDates

.PHONY : CMakeFiles/LiviaDates.dir/build

CMakeFiles/LiviaDates.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/LiviaDates.dir/cmake_clean.cmake
.PHONY : CMakeFiles/LiviaDates.dir/clean

CMakeFiles/LiviaDates.dir/depend:
	cd /home/victor/Desktop/Programming/UBB/OOP/LiviaDates/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/victor/Desktop/Programming/UBB/OOP/LiviaDates /home/victor/Desktop/Programming/UBB/OOP/LiviaDates /home/victor/Desktop/Programming/UBB/OOP/LiviaDates/cmake-build-debug /home/victor/Desktop/Programming/UBB/OOP/LiviaDates/cmake-build-debug /home/victor/Desktop/Programming/UBB/OOP/LiviaDates/cmake-build-debug/CMakeFiles/LiviaDates.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/LiviaDates.dir/depend

