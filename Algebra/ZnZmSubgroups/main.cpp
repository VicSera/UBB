#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream input("input_files/input_file1");
ofstream output("output_files/output_file1");

typedef unsigned int natural; // define natural numbers as unsigned integers
typedef vector<pair<natural, natural>> cartesian_subgroup; // we call cartesian subgroups those subgroups of sets that are obtained through a cartesian product

bool find(cartesian_subgroup S, pair<natural, natural> value)
{
    // Look for a value in a set
    for (auto it = S.begin(); it != S.end(); ++it)
        if (*it == value) // If it is found, return true
            return true;
    return false; // Otherwise, return false
}

natural Zn_sum(natural a, natural b, natural n)
{
    // Compute the sum of two numbers a,b in Zn
    natural result = a + b;
    if (result >= n)
        result -= n;
    return result;
}

bool check_subgroup(cartesian_subgroup S, natural n, natural m)
{
    // Check if the current subgroup is stable
    for (auto a = S.begin(); a != S.end(); ++a)
        for (auto b = a; b != S.end(); ++b) // For all (a->first, a->second), (b->first, b->second) in Zn x Zm
        {
            pair<natural, natural> sum_ab = {Zn_sum(a->first, b->first, n), Zn_sum(a->second, b->second, m)}; // Compute the sum of a and b
            if (!find(S, sum_ab)) // Check if their sum is in the subset
                return false;
        }
    return true;
}

void print(cartesian_subgroup S)
{
    // Print a subset
    output << "{(" << S.begin()->first << ", " << S.begin()->second << ")";
    for (auto it = S.begin() + 1; it != S.end(); ++it)
        output << ", (" << it->first << ", " << it->second << ')';
    output << "}" << endl;
}

void generate_ZnZm_subgroups(natural current_pos, natural max_pos, natural n, natural m, cartesian_subgroup ZnZmSubgroup, natural& solutions)
{
    if (current_pos == max_pos) // If there are sufficient elements generated, stop
        return;

    pair<natural, natural> last = ZnZmSubgroup.back();

    for (natural x1 = 0; x1 < n; ++x1) // Pick an element from Zn
        for (natural x2 = 0; x2 < m; ++x2) // Pick and element from Zm
        {
            if (find(ZnZmSubgroup, {x1, x2})) // If it is already in the set, skip
                continue;
            if (x1 < last.first) // If x1 is not ordered, skip
                continue;
            if (x1 == last.first && x2 < last.second) // If x2 is not ordered, skip
                continue;
            ZnZmSubgroup.push_back({x1, x2}); // Append the pair to the list
            if (check_subgroup(ZnZmSubgroup, n, m)) // If the newly obtained subset is valid
            {
                print(ZnZmSubgroup); // Print it out
                ++solutions; // Increment the number of solutions
            }
            generate_ZnZm_subgroups(current_pos + 1, max_pos, n, m, ZnZmSubgroup, solutions); // Generate all the subsets that already contain the pair (x1, x2)
            ZnZmSubgroup.pop_back(); // Remove (x1, x2)
        }
}

int main()
{
    natural n, m, solutions = 1; // Start with 1 solution because of the identities
    cartesian_subgroup ZnZm = {{0, 0}}; // Initialise with (0, 0) because each subset will contain this pair by default

    input >> n >> m; // Read input

    print(ZnZm); // Print the subset containing the identities
    generate_ZnZm_subgroups(1, n*m, n, m, ZnZm, solutions); // Call the backtracking function

    output << "-------------------------------------------\n";
    output << "For Z" << n << " x Z" << m << " there are " << solutions << " solutions.\n";

    return 0;
}
