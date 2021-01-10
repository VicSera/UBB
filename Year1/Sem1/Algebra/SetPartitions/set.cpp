#include "set.h"

//cpp file that contains all the definitions of the structures and functions declared in set.h

//This implementation uses backtracking on a list of "parents", using the following logic:
//Let a be a number in the set A
//Let P be a partition of the set A
//parent_list[a] = i, where Pi is the class that contains a
//In other words, the "parent" of a number is just the class that contains it
//Classes start from 0, and there can be at most n classes, where n = |A|

//For any two numbers a, b, if parent_list[a] = parent_list[b], the two numbers are part of the same class
//Therefore, a and b are related, so the pair (a, b) is added to the graph

//The parent list structure is then passed on to functions that construct the usual partition structure
//{{.., ..},{.., ..},....,{.., ..}}

extern std::ofstream output_file;

void divide(unsigned int num_classes, unsigned int num_elements, unsigned int current_element, std::vector<int>& parent_list, unsigned int& counter)
{
    //Backtracking function that generates all possible partitions using parent lists
    if (current_element > num_elements) //If all the necessary elements have been assigned, it's time to check the resulting partition for skipped classes
    {
        if (is_valid(parent_list, num_classes)) //Checking function
        {
            partition P = get_partition_from_parents(parent_list, num_classes);
            if (!is_ordered(P)) //Function that checks if the classes in the partition are ordered, to avoid equivalent partitions from being counted and displayed twice
                return;
            ++counter; //Increment the counter that keeps track of the partitions
            if (num_elements > THRESHOLD)
                return; //If there are more elements than the set THRESHOLD (in this case 8), skip printing and just count the partitions
            output_file << "Partition:\n";
            print_partition(P); //Print the partition
            output_file << "Equivalence relation:\n";
            print_graph(get_graph(parent_list)); //Print the equivalence relation graph
            output_file << "\n";
        }
        return; //placed each element in a class
    }
    for (unsigned int current_class = 0; current_class < num_classes; ++current_class) //Main backtracking body, place each element through each class
    {
        parent_list.push_back(current_class); //Actual placing of the element in the class
        divide(num_classes, num_elements, current_element + 1, parent_list, counter); //Call the backtracking function for the remaining elements that have not yet been placed
        parent_list.pop_back(); //Remove the element so that it can be placed somewhere else in future calls of the function
    }
}

graph get_union(graph& a, graph& b)
{
    //Function that returns the union of two graphs
    //(in this case, elements will not repeat because of the way the graphs are generated, so no extra checking is required for duplicate entries)
    graph new_graph = a;
    for (auto it = b.begin(); it != b.end(); ++it)
        new_graph.push_back(*it); //Simply append all the elements of b to a
    return new_graph;
}

graph get_graph (std::vector<int> parent_class_list)
{
    //Function that turns a parent list into a graph
    //It calls the get_class_subgraph function for each found class in the parent_list
    unsigned int n_classes = num_classes(parent_class_list);
    graph final_graph; //The graph

    for (unsigned int current_class = 0; current_class < n_classes; ++current_class) //Loop through each class
    {
        std::vector<int> elements_in_class; //Array containing the elements in the current class
        for (auto it = parent_class_list.begin(); it != parent_class_list.end(); ++it) //Loop through all the elements in the set
            if (*it == current_class)
                elements_in_class.push_back(it - parent_class_list.begin() + 1); //If the element's parent class corresponds to the current class we're looking for, add it to the array
        graph class_graph = get_class_subgraph(elements_in_class); //Call the get_class_subgraph for the elements found
        final_graph = get_union(final_graph, class_graph); //Add the found relations to the final graph
    }
    return final_graph;
}

graph get_class_subgraph(std::vector<int> elements)
{
    //Function that generates the subgraph (included in the graph of the relation) that corresponds to a certain class in the partition
    graph class_subgraph;
    relation current_relation;
    for (auto element1 = elements.begin(); element1 != elements.end(); ++element1) //Take one element from the class
        for (auto element2 = elements.begin(); element2 != elements.end(); ++element2) //Take another element from the class
        {
            current_relation = {*element1, *element2}; //Since the relation is an equivalence relation, all elements are related so that each condition is satisfied
            class_subgraph.push_back(current_relation); //Add the obtained relation to the subgraph
        }
    return class_subgraph;
}


unsigned int num_classes (std::vector<int> parent_class_list)
{
    //Function that figures out how many classes there should be, based on a parent list
    unsigned int highest_class = 0;
    for (auto it = parent_class_list.begin(); it != parent_class_list.end(); ++it)
        if (highest_class < (*it) + 1) //We have to add one since the classes are kept in from 0 to n-1, but we want to return n
            highest_class = (*it) + 1;
    return highest_class;
}

bool is_valid(std::vector<int>& parent_list, unsigned int num_classes)
{
    //Function that checks whether the set was split properly
    for (unsigned int class_number = 0; class_number < num_classes; ++class_number)
    {
        bool flag = false;
        for (auto it = parent_list.begin(); it != parent_list.end() && !flag; ++it)
            if (*it == class_number)
                flag = true; //Mark that the current class contains at least one element
        if (!flag) //If the current class is empty, that means the partition is not right
            return false;
    }
    return true;
}

bool is_ordered(partition P)
{
    for (auto subclass = P.begin(); subclass + 1 != P.end(); ++subclass)
        if ((*subclass)[0] > (*(subclass + 1))[0])
            return false;
    return true;
}

partition get_partition_from_parents(std::vector<int>& parent_list, unsigned int num_classes)
{
    //Function used to turn a parent list to an actual partition
    partition P;
    for (unsigned int i = 0; i < num_classes; ++i)
    {
        std::vector<int> empty; //Assign empty space for the classes in the partition
        P.push_back(empty);
    }
    for (auto it = parent_list.begin(); it != parent_list.end(); ++it)
        P[*it].push_back(it - parent_list.begin() + 1); //Fill the classes with the found numbers, based on each one's parent class
    return P;
}

//PRINTING FUNCTIONS

void print_subclass(std::vector<int> subclass)
{
    output_file << "{";
    for (auto element = subclass.begin(); (element + 1) != subclass.end(); ++element)
        output_file << *element << ", ";
    output_file << *(subclass.end() - 1) << "}";
}

void print_partition(partition P)
{
    //Function used to print the contents of a partition
    output_file << "{";
    for (auto subclass = P.begin(); (subclass + 1) != P.end(); ++subclass)
    {
        print_subclass(*subclass);
        output_file << ", ";
    }
    print_subclass(*(P.end() - 1));
    output_file << "}\n";
}

void print_all_graphs(unsigned int num_elements)
{
    if (num_elements == 0)
    {
        output_file<< "Size of the set is 0.\n";
        exit(1);
    }
    //Function that triggers the backtracking
    unsigned int counter = 0;
    for (unsigned int num_classes = 1; num_classes <= num_elements; ++num_classes)
    {
        std::vector<int> parent_list; //Reset the parent list
        divide(num_classes, num_elements, 1, parent_list, counter); //Call the backtracking function
    }
    output_file << "---------------\nFound " << counter << " partitions.\n";
    output_file << "Set used: {1";
    for (unsigned int i = 2; i <= num_elements; ++i)
        output_file << ", " << i;
    output_file << "}\n";
}

void print_graph(graph G)
{
    //Function that prints the graph of a relation
    output_file << '{';
    for (auto it = G.begin(); (it + 1) != G.end(); ++it)
        output_file << '(' << it->first << ", " << it->second << "), ";
    output_file << '(' << (G.end() - 1)->first << ", " << (G.end() - 1)->second << ')';
    output_file << "}\n";
}

//STRING MANIPULATION FUNCTIONS

std::string int_to_string(unsigned int number)
{
    //Function that turns an integer to a standard string
    std::string string_result = "";
    if (number == 0) //Special case for 0, since the program would skip the while loop entirely
        string_result = "0";
    while (number)
    {
        string_result.push_back((number % 10) + (int)'0'); //Convert last digit to ASCII code by adding it to the ASCII code of '0', and then adding it to our string
        number /= 10; //Cut off the right-most digit to be able to use MOD 10 the right way
    }

    return reverse(string_result); //Reverse function has to be called since the number was parsed from right to left, but the string was constructed from left to right
}

std::string reverse(std::string& arg_string)
{
    //Function that reverses a string
    std::string new_string = "";
    for (auto iterator = arg_string.rbegin(); iterator != arg_string.rend(); ++iterator) //Parse the string from right to left
        new_string.push_back(*iterator); //Append the current character to a new string, from left to right
    return new_string;
}
