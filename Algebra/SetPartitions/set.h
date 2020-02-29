#pragma once

//Header file that contains the declarations of all structures and functions used
//See set.cpp file for all the implementations

#include <iostream>
#include <vector>
#include <string>
#include <array>
#include <fstream>

#define THRESHOLD 8 //Threshold after which only the number of partitions will be printed out

typedef std::pair<int, int> relation;
typedef std::vector<relation> graph;
typedef std::vector<std::vector<int>> partition;

std::string int_to_string(unsigned int number);

std::string reverse(std::string& arg_string);

graph get_union(graph& a, graph& b);

graph get_graph(std::vector<int> parent_class_list);

graph get_class_subgraph(std::vector<int> elements);

void print_partition(partition P);

partition get_partition_from_parents(std::vector<int>& parent_list, unsigned int num_classes);

bool is_ordered(partition P);

bool is_valid(std::vector<int>& parent_list, unsigned int num_classes);

void print_graph(graph G);

unsigned int num_classes(std::vector<int> parent_class_list);

void print_all_graphs(unsigned int num_elements);
