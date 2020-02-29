#include <iostream>
#include <fstream>

#define THRESHOLD 4

typedef bool relation_matrix[30][30];

std::ifstream input_file ("input_files/input_file0.txt");
std::ofstream output_file("output_files/output_file0.txt");

void print(relation_matrix relations, unsigned int num_elements)
{
    //Function that prints the relation graph described by a matrix
    //If relations[a][b] == true, then a r b
    bool is_empty_set = true;
    output_file << "{";
    for (unsigned int i = 0; i < num_elements; ++i) //Go through each pair (i, j)
        for (unsigned int j = 0; j < num_elements; ++j)
            if (relations[i][j]) //If the pair (i, j) is found in the graph, print it out
            {
                if (is_empty_set)
                    output_file << '(' << i << ", " << j << ')'; //first element is printed without the ", " at the front
                else
                    output_file << ", "<< '(' << i << ", " << j << ')';
                is_empty_set = false;
            }
    if (is_empty_set) //If no relations are found, the resulting graph is the empty set
        output_file << "EMPTY SET}\n";
    else
        output_file << "}\n";
}

bool has_transitivity(relation_matrix relations, unsigned int num_elements)
{
    //Function that checks the transitivity property
    for (unsigned int a = 0; a < num_elements; ++a)
        for (unsigned int b = 0; b < num_elements; ++b)
            for (unsigned int c = 0; c < num_elements; ++c) //For any a, b, c in the set
                if (relations[a][b] && relations[b][c] && !relations[a][c]) //if a r b and b r c, then a r c. Otherwise, the relation is not transitive
                    return false;
    return true; //If no inconsistency was found, the relation is transitive
}

void get_all_transitive_relations(relation_matrix relations, unsigned int num_elements, unsigned int a, unsigned int b, unsigned int& num_relations)
{
    //Function that backtracks through all relation matrices
    if (a >= num_elements) //We reached the end of the matrix
    {
        if (has_transitivity(relations, num_elements)) //Check transitivity
        {
            if (num_elements <= THRESHOLD)
                print(relations, num_elements); //Print only if there are 4 or fewer elements
            ++num_relations; //Increment number of transitive relations found
        }
        return;
    }
    if (b >= num_elements) //We reached the end of a row, so we have to reset the column and go to the next row
        get_all_transitive_relations(relations, num_elements, a + 1, 0, num_relations);
    else
    {
        //do all graphs that contain a r b
        relations[a][b] = true;
        get_all_transitive_relations(relations, num_elements, a, b + 1, num_relations);
        //do all graphs that don't contain a r b
        relations[a][b] = false;
        get_all_transitive_relations(relations, num_elements, a, b + 1, num_relations);
    }
}

int main()
{
    relation_matrix relations = {false}; //Initially, no relations exist
    unsigned int set_dimension, number_of_relations = 0;

    input_file >> set_dimension; //Read input

    get_all_transitive_relations(relations, set_dimension, 0, 0, number_of_relations); //Call the backtracking function
    output_file << "Set used: {"; //Print out the initial set and the number of relations found
    output_file << 1;
    for (unsigned int i = 1; i < set_dimension; ++i)
        output_file  << ", " << i + 1;
    output_file << "}\nTotal number of transitive relations is: " << number_of_relations << std::endl;
    return 0;
}
