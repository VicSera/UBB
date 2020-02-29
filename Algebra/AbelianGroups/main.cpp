#include <iostream>
#include <fstream>

using namespace std;

typedef unsigned int natural_number;
typedef natural_number operation[50][50];

#define THRESHOLD 7

ifstream input_file("input_files/input_file5");
ofstream output_file("output_files/output_file5");

bool is_unique(natural_number value, natural_number row, natural_number column, operation table, natural_number num_elements)
{
    // Check if a value has already appeared in a row or column
    for (natural_number row_iterator = 0; row_iterator < num_elements; ++row_iterator)
        if (table[row_iterator][column] == value) // Go through the column by fixing it and changing rows
            return false;
    for (natural_number column_iterator = 0; column_iterator < num_elements; ++column_iterator)
        if (table[row][column_iterator] == value) // Go through the row by fixing it and changing columns
            return false;
    return true; // Return true if no equal values were found on the row and column
}

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
            for (natural_number c = 0; c < num_elements; ++c)
                if (operation_table[operation_table[a][b]][c] != operation_table[a][operation_table[b][c]])
                    return false;
    return true;
}

void set_identity(natural_number identity, operation table, natural_number num_elements)
{
    // This function just 'prepares' the operation table for the next call of the backtracking function
    // by setting the identity row and column to the appropriate value

    for (natural_number i = 0; i < num_elements; ++i)
        for (natural_number j = 0; j < num_elements; ++j)
            table[i][j] = 999;

    for (natural_number row_iterator = 0; row_iterator < num_elements; ++row_iterator) // Column fixed
        table[row_iterator][identity] = row_iterator;
    for (natural_number column_iterator = 0; column_iterator < num_elements; ++column_iterator) // Row fixed
        table[identity][column_iterator] = column_iterator;
}

void generate_abelian_groups(operation operation_table, natural_number num_elements, natural_number a, natural_number b, natural_number identity, natural_number& num_groups)
{
    if (a >= num_elements) // Reached the end of the operation table
    {
        if (!check_associativity(operation_table, num_elements))
            return;
        // We know that the group is abelian, since it was being checked while in the building process
        if (num_elements <= THRESHOLD)
            print(operation_table, num_elements); // Print it out
        ++num_groups; // Increment number of groups found
        return;
    }
    else if (b >= num_elements) // Reached the end of a line
        generate_abelian_groups(operation_table, num_elements, a + 1, a + 1, identity, num_groups); // Hop on to the next line, directly on the diagonal
    else if (a == identity || b == identity) // Skip over the rows/columns of the current identity element
        generate_abelian_groups(operation_table, num_elements, a, b + 1, identity, num_groups);
    else
        for (natural_number value = 0; value < num_elements; ++value)
            if (is_unique(value, a, b, operation_table, num_elements)) // Check if the element is unique in its row and column
            {
                operation_table[a][b] = operation_table[b][a] = value; // Set a value to the current spot in the table
                generate_abelian_groups(operation_table, num_elements, a, b + 1, identity, num_groups); // Build all groups that have (a, b) fixed
                operation_table[a][b] = operation_table[b][a] = 999; // Reset the value of (a, b) so that it doesn't have residual effect over later table checks
            }
}

int main()
{
    operation phi;
    natural_number num_elements, num_groups = 0;

    input_file >> num_elements;

    for (natural_number identity = 0; identity < num_elements; ++identity) // Call the main backtracking function for each possible identity
    {
        set_identity(identity, phi, num_elements); // Clean up the table before looking for appropriate operations
        generate_abelian_groups(phi, num_elements, 0, 0, identity, num_groups); // Main function call
    }

    output_file << "Found " << num_groups << " abelian groups";

    return 0;
}
