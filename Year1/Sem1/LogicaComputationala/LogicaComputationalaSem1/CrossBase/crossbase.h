#pragma once

#include <string>
#include <iostream>

#define PRECISION 4

template<typename p1, typename p2>
struct pair
{
    p1 left;
    p2 right;
};

class num;

typedef pair<num, num> div_result;

static const std::string digits = "0123456789ABCDEF";

class num
{
private:
    std::string value;
    num pow10 (int power);
    void concatenate (const num& other);
    void eliminate_padding ();
    int to_base_10();

public:
    unsigned int base;
    bool negative;

    div_result int_division (const num& other) const;

    void _reverse();

    num (); //empty constructor
    num (unsigned int base); //constructor that takes in base
    num (const char* value, unsigned int base); //constructor that takes in a value and its base
    num (const char value, unsigned int base);

    void set_value(const std::string& new_value);
    void set_value(const char* new_value);
    std::string get_value() const;
    void append(char c);
    void prepend(char c);

    num convert_base (unsigned int target_base);

    unsigned int integer_length() const;
    unsigned int decimal_length() const;

    bool operator < (const num& other) const;
    bool operator > (const num& other) const;
    bool operator <= (const num& other) const;
    bool operator >= (const num& other) const;
    bool operator == (const num& other) const;
    bool operator != (const num& other) const;

    num operator + (const num& other) const;
    num operator - (const num& other) const;
    num operator * (const num& other) const;
    num operator / (const num& other) const;
    num operator ^ (const num& other) const;

    void operator += (const num& other);
    void operator -= (const num& other);
    void operator *= (const num& other);
    num operator ++ ();
    num operator -- ();
    num operator - ();
    num operator ()(unsigned int target_base);

    void operator = (const num& other);
    void operator = (const char* val);

    void apply_offset (unsigned int offset);
};

int pow(int a, int b);

num from_base_10 (int n, unsigned int base);

std::ostream& operator << (std::ostream& output_stream, const num& number);

int search (const char c, const std::string v); //find char in string, return index

unsigned int char_to_dec_int (const char c); //convert character to decimal integer

char dec_int_to_char (const unsigned int d); //convert decimal integer to character

num char_to_int (const char c, unsigned int target_base);

void pad_numbers (num& n1, num& n2); //adjust the lengths of two strings by padding the shorter one with zeroes

void reverse (std::string& s); //reverse a string
