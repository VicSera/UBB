#include <iostream>
#include <fstream>

using namespace std;

typedef unsigned int natural_number;
typedef natural_number operation[20][20];

#define THRESHOLD 4

ifstream input_file("input_files/input_file4");
ofstream output_file("output_files/output_file4");

void print(operation operation_table, natural_number num_elements)
{
    // First lines are for printing the table structure

    output_file << "   |";
    for (natural_number i = 0; i < num_elements; ++i)
        output_file << " a" << i + 1;
    output_file << endl;
    for (natural_number i = 0; i < num_elements * 5; ++i)
        output_file << '-';
    output_file << endl;
    for (natural_number i = 0; i < num_elements; ++i, output_file << endl)
    {
        output_file << 'a' << i + 1 << " |";
        for (natural_number j = 0; j < num_elements; ++j) // Print all numbers
            output_file <<  " a" << operation_table[i][j] + 1;
    }
    output_file << endl;
}

bool check_associativity(operation operation_table, natural_number num_elements)
{
    for (natural_number a = 0; a < num_elements; ++a)
        for (natural_number b = 0; b < num_elements; ++b)
            for (natural_number c = 0; c < num_elements; ++c) // For all a, b, c in the set
                if (operation_table[operation_table[a][b]][c] != operation_table[a][operation_table[b][c]]) // check (a * b) * c = a * (b * c)
                    return false;
    return true; // If we reached the end, the operation is associative
}

void generate_operation_table(operation operation_table, natural_number a, natural_number b, natural_number num_elements, natural_number& num_results)
{
    if (b == num_elements) // Reached end of line
        generate_operation_table(operation_table, a + 1, 0, num_elements, num_results);
    else if (a == num_elements) // Reached end of table
    {
        if (check_associativity(operation_table, num_elements)) // If the operation is associative
        {
            ++num_results; // Increment the number of results
            if (num_elements <= THRESHOLD) // If we have 4 or fewer elements
                print(operation_table, num_elements); // Print the table
        }
    }
    else // If the table is still incomplete
        for (natural_number value = 0; value < num_elements; ++value) // Go through each possible value
        {
            operation_table[a][b] = value; // Assign it to the current spot in the operation table
            generate_operation_table(operation_table, a, b + 1, num_elements, num_results); // Generate the rest of the table
        }

}

int main()
{
    operation alpha; // Initialisation of the operation, called alpha
    natural_number num_elements, num_results = 0; // Initialisation of the number of elements and number of associative results

    input_file >> num_elements; // Read input from file

    generate_operation_table(alpha, 0, 0, num_elements, num_results); // Generate the table, starting from the corner (position (0,0))

    output_file << "Total number of associative operations on the set:\n";
    output_file << "{a0";
    for (natural_number n = 1; n < num_elements; ++n)
        output_file << ", a" << n;
    output_file << "}\n";
    output_file << "is " << num_results << endl;

    return 0;
}
