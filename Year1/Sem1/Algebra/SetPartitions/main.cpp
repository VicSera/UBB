#include "set.h"
#include <fstream>
#include <map>

std::ifstream input_file("input_files/input_file.txt");
std::ofstream output_file("output_files/output_file.txt");

int main()
{
    unsigned int n_elements;
    input_file >> n_elements; //read the input from the input file
    print_all_graphs(n_elements); //call the function that coordinates everything else
    return 0;
}
