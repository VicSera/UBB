#include "crossbase.h"

num::num() : value(""), base(10), negative(false)
{

}

num::num(unsigned int base) : value(""), base(base), negative(false)
{

}

num::num(const char* _value, unsigned int base) : value(_value), base(base)
{
    if (value[0] == '-')
    {
        negative = true;
        value.erase(value.begin());
    }
    else
        negative = false;
}

num::num(const char _value, unsigned int base) : base(base)
{
    value.push_back(_value);
}

void num::_reverse()
{
    std::string new_str = "";
    for (auto it = value.rbegin(); it != value.rend(); ++it)
        new_str.push_back(*it);

    set_value(new_str);
}

num from_base_10 (int n, unsigned int base)
{
    num new_num(base);

    while (n)
    {
        unsigned int rest = n % base;

        new_num.append(dec_int_to_char(rest));
        n = n / base;
    }

   new_num._reverse();
   return new_num;
}

int pow (int a, int b)
{
    if (b == 1)
        return a;
    if (b == 0)
        return 1;

    if (b % 2 == 0)
        return pow(a * a, b / 2);
    else
        return a * pow(a * a, (b - 1) / 2);
}

int num::to_base_10()
{
    int new_num = 0;
    for (auto digit = value.begin(); digit != value.end(); ++digit)
    {
        new_num += char_to_dec_int(*digit) * pow(base, (integer_length() - 1 - (digit - value.begin())));
        std::cout << "Turned a digit to " << new_num << std::endl;
    }
    return new_num;
}

void num::set_value(const std::string &new_value)
{
    if (value[0] == '-')
    {
        negative = true;
        value = new_value.substr(1); //cut -
    }
    else
        value = new_value;
}

void num::set_value(const char* new_value)
{
    value = new_value;
    if (value[0] == '-')
    {
        negative = true;
        value.erase(value.begin()); //cut -
    }
}

std::string num::get_value() const
{
    return value;
}

std::ostream& operator << (std::ostream& output_stream, const num& number)
{
    if (number.negative)
        output_stream << '-';
    output_stream << number.get_value();
    return output_stream;
}

unsigned int num::integer_length() const
{
    for (auto it = value.begin(); it != value.end(); ++it)
        if (*it == '.')
            return (it - value.begin());
    return 0;
}

unsigned int num::decimal_length() const
{
    for (auto it = value.rbegin(); it != value.rend(); ++it)
        if (*it == '.')
            return (it - value.rbegin());
    return 0;
}

void reverse (std::string& s)
{
    std::string new_str = "";
    for (auto it = s.rbegin(); it != s.rend(); ++it)
        new_str.push_back(*it);

    s = new_str;
}

num num::operator ++ ()
{
    *this += num("1", base);
    return *this;
}

num num::operator -- ()
{
    *this -= num("1", base);
    return *this;
}

num num::pow10(int power)
{
    num new_num("1", base);

    for (int it = 0; it < power; ++it)
        new_num *= *this;

    return new_num;
}

num num::convert_base(unsigned int target_base)
{
    num new_value(target_base);

    int tmp_base_10_val = to_base_10();
    std::cout << "Moving to base 10: " << tmp_base_10_val << std::endl;
    new_value = from_base_10(tmp_base_10_val, target_base);

    return new_value;
}

num num::operator ^ (const num& other) const
{
    num new_num("1", base);
    num iterator("0", base);

    for (iterator; iterator < other; ++iterator)
        new_num *= *this;

    return new_num;
}

num num::operator + (const num& other) const
{
    if (base != other.base)
    {
        std::cout << "Trying to add numbers of different bases. Exiting.\n";
        exit(1);
    }
    unsigned int carry = 0;
    num n1 = *this, n2 = other;

    pad_numbers(n1, n2); //pad with zeroes in case lengths differ
    //std::cout << "\nPadded numbers: " << n1 << ", " << n2 << std::endl;
    std::string &v1 = n1.value, &v2 = n2.value;

    num new_num;
    new_num.base = base;

    for (long i = long(v1.size() - 1); i >= 0; --i)
    {
        if (v1[i] == '.')
        {
            new_num.value.push_back('.');
            continue;
        }
        unsigned int result = carry + char_to_dec_int(v1[i]) + char_to_dec_int(v2[i]);
        carry = 0;
        if (result >= base)
        {
            carry = 1;
            result -= base;
        }
        new_num.value.push_back(dec_int_to_char(result));
    }
    if (carry) //check for any value carried over
        new_num.value.push_back(dec_int_to_char(carry));

    reverse (new_num.value);
    new_num.eliminate_padding();
    return new_num;
}

void num::operator = (const num &other)
{
    //std::cout << "Used my = operator instead of the default one.\n";
    value = other.value;
    base = other.base;
}

void num::operator = (const char* val)
{
    value = val;
}

void num::operator += (const num &other)
{
    *this = *this + other;
}

num num::operator - (const num &other) const
{
    if (base != other.base)
    {
        std::cout << "Trying to add numbers of different bases. Exiting.\n";
        exit(1);
    }
    int carry = 0;
    num n1 = *this, n2 = other; //pad with zeroes in case lengths differ
    if (n1 < n2)
        return -(n2 - n1);
    pad_numbers(n1, n2);

    std::string &v1 = n1.value, &v2 = n2.value;
    std::string new_val = "";

    num new_num(base);

    for (long i = long(v1.size() - 1); i >= 0; --i)
    {
        if (v1[i] == '.')
        {
            new_val.push_back('.');
            continue;
        }
        int result = carry + char_to_dec_int(v1[i]) - char_to_dec_int(v2[i]);
        carry = 0;
        if (result < 0)
        {
            carry = -1;
            result += base;
        }
        new_val.push_back(dec_int_to_char(result));
    }
    if (carry) //check for any value carried over
        new_val.push_back(dec_int_to_char(carry * (-1)));

    new_num.set_value(new_val);
    reverse (new_num.value);
    new_num.eliminate_padding();
    return new_num;
}

void num::operator -= (const num& other)
{
    *this = *this - other;
}

num num::operator * (const num& other) const
{
    num new_num("0", base);
    num partial_result("", base);
    unsigned int offset = 0;
    unsigned int carry = 0;

    for (auto digit = other.value.rbegin(); digit != other.value.rend(); ++digit)
    {
        partial_result = "";
        for (auto my_digit = value.rbegin(); my_digit != value.rend(); ++my_digit)
        {
            unsigned int result = carry + char_to_dec_int(*digit) * char_to_dec_int(*my_digit);
            carry = result / base;
            result = result % base;
            partial_result.append(dec_int_to_char(result));
        }
        if (carry)
            partial_result.append(dec_int_to_char(carry));

        carry = 0;

        reverse(partial_result.value);
        partial_result.apply_offset(offset);

        new_num += partial_result;

        ++offset;
    }

    return new_num;
}

void num::operator *= (const num& other)
{
    *this = *this * other;
}

div_result num::int_division (const num &other) const
{
    num final_quotient(base);
    num rest(base);
    num carry(base);


    for (auto digit = value.begin(); digit != value.end(); ++digit)
    {
        if (*digit == '.')
        {
            final_quotient.append('.');
            continue;
        }
        num quotient(base);
        num current_num("", base);

        if (carry.get_value() != "0")
            current_num = carry;
        current_num.append(*digit);

        while (quotient * other <= current_num)
            ++quotient;
        --quotient;

        carry = current_num - (quotient * other);

        final_quotient.concatenate(quotient);
    }

    final_quotient.eliminate_padding();
    //std::cout << *this << " - (" << other << " * " << final_quotient << ") = " ;
    rest = *this - (other * final_quotient);
    //std::cout << rest << std::endl;
    rest.eliminate_padding();

    return {final_quotient, rest};
}

num num::operator / (const num& other) const
{
    num new_num(base);
    num carry(base);


    for (auto digit = value.begin(); digit != value.end(); ++digit)
    {
        if (*digit == '.')
        {
            new_num.append('.');
            continue;
        }
        num quotient(base);
        num current_num("", base);

        if (carry.get_value() != "0")
            current_num = carry;
        current_num.append(*digit);

        while (quotient * other <= current_num)
            ++quotient;
        --quotient;

        carry = current_num - (quotient * other);

        new_num.concatenate(quotient);
    }

    unsigned int d_len = decimal_length();
    if (!d_len)
        new_num.append('.');

    for (unsigned int i = 0; i < PRECISION - d_len; ++i)
    {
        num quotient("0", base);
        num current_num("", base);


        if (carry.get_value() != "0")
            current_num += carry;
        current_num.append('0');

        while (quotient * other <= current_num)
            ++quotient;
        --quotient;

        carry = current_num - (quotient * other);

        new_num.concatenate(quotient);
    }

    new_num.eliminate_padding();
    return new_num;
}

void num::eliminate_padding()
{
    if (value == "0")
        return;

    std::string new_val = "";
    while (value[0] == '0')
        value.erase(value.begin()); //remove insignificant 0s in the beginning
    if (decimal_length())
        while (value[value.size() - 1] == '0') //remove insignificant 0s after decimal point
            value.erase(value.end() - 1);

    if (*(value.end() - 1) == '.') //remove . if no decimal digits remain
        value.erase(value.end() - 1);

    if (value == "")
        value = "0";
}

int search (const char c, const std::string v)
{
    for (auto it = v.begin(); it != v.end(); ++it)
        if (*it == c)
            return int(it - v.begin());
    return -1;
}

void num::concatenate(const num &other)
{
    value += other.value;
}

unsigned int char_to_dec_int (const char c)
{
    return search(c, digits);
}

char dec_int_to_char (const unsigned int d)
{
    return digits[d];
}

void num::append(char c)
{
    value += c;
}

void num::prepend(char c)
{
    value = c + value;
}

void pad_numbers (num& n1, num& n2)
{
    //left padding - integer side
    long len_diff = long(n1.integer_length()) - n2.integer_length(); //std::string::size() returns unsigned long values

    if (len_diff > 0) //s1 > s2
        for (long i = 0; i < len_diff; ++i)
            n2.prepend('0');
    else //s1 <= s2
    {
        len_diff *= -1;
        for (long i = 0; i < len_diff; ++i)
            n1.prepend('0');
    }

    //right padding - decimal side
    len_diff = long(n1.decimal_length() - n2.decimal_length());

    if (len_diff > 0) //s1 > s2
        for (long i = 0; i < len_diff; ++i)
            n2.append('0');
    else //s1 <= s2
    {
        len_diff *= -1;
        for (long i = 0; i < len_diff; ++i)
            n1.append('0');
    }
}

bool num::operator < (const num &other) const
{
    unsigned int len1 = this->integer_length();
    unsigned int len2 = other.integer_length();
    if (negative == other.negative)
    {
        if (len1 == len2)
        {
            for (unsigned int i = 0; i < std::min(value.size(), other.value.size()); ++i)
            {
                unsigned int val1 = char_to_dec_int(value[i]);
                unsigned int val2 = char_to_dec_int(other.value[i]);
                if (val1 < val2)
                    return true;
                else if (val1 > val2)
                    return false;
            }
            if (value.size() < other.value.size()) //if both values are equal until one ends, the longer one is bigger
                return true;
            return false;
        }
        return len1 < len2; //if integer lengths differ - the shorter one is smaller
    }
    else if (negative && !other.negative) //different signs
        return true;
    else
        return false;
}

bool num::operator > (const num &other) const
{
    unsigned int len1 = this->integer_length();
    unsigned int len2 = other.integer_length();
    if (negative == other.negative)
    {
        if (len1 == len2)
        {
            for (unsigned int i = 0; i < std::min(value.size(), other.value.size()); ++i)
            {
                unsigned int val1 = char_to_dec_int(value[i]);
                unsigned int val2 = char_to_dec_int(other.value[i]);
                if (val1 > val2)
                    return true;
                else if (val1 < val2)
                    return false;
            }
            if (value.size() > other.value.size()) //if both values are equal until one ends, the longer one is bigger
                return true;
            return false;
        }
        return len1 > len2; //if integer lengths differ - the shorter one is smaller
    }
    else if (!negative && other.negative) //different signs
        return true;
    else
        return false;
}

bool num::operator == (const num &other) const
{
    return (value == other.value && negative == other.negative);
}

bool num::operator != (const num &other) const
{
    return (value != other.value || negative != other.negative);
}

bool num::operator <= (const num &other) const
{
    unsigned int len1 = this->integer_length();
    unsigned int len2 = other.integer_length();
    if (negative == other.negative)
    {
        if (len1 == len2)
        {
            for (unsigned int i = 0; i < std::min(value.size(), other.value.size()); ++i)
            {
                unsigned int val1 = char_to_dec_int(value[i]);
                unsigned int val2 = char_to_dec_int(other.value[i]);
                if (val1 < val2)
                    return true;
                else if (val1 > val2)
                    return false;
            }
            if (value.size() <= other.value.size()) //if both values are equal until one ends, the longer one is bigger
                return true;
            return false;
        }
        return len1 < len2; //if integer lengths differ - the shorter one is smaller
    }
    else if (negative && !other.negative) //different signs
        return true;
    else
        return false;
}

bool num::operator >= (const num &other) const
{
    unsigned int len1 = this->integer_length();
    unsigned int len2 = other.integer_length();
    if (negative == other.negative)
    {
        if (len1 == len2)
        {
            for (unsigned int i = 0; i < std::min(value.size(), other.value.size()); ++i)
            {
                unsigned int val1 = char_to_dec_int(value[i]);
                unsigned int val2 = char_to_dec_int(other.value[i]);
                if (val1 > val2)
                    return true;
                else if (val1 < val2)
                    return false;
            }
            if (value.size() >= other.value.size()) //if both values are equal until one ends, the longer one is bigger
                return true;
            return false;
        }
        return len1 > len2; //if integer lengths differ - the shorter one is smaller
    }
    else if (negative && !other.negative) //different signs
        return true;
    else
        return false;
}

num num::operator - ()
{
    num new_num = *this;
    new_num.negative = !negative;

    return new_num;
}

void num::apply_offset(unsigned int offset)
{
    if (this->decimal_length())
    {
        std::cout << "Trying to apply an offset to a decimal number. Exiting.\n";
        exit(1);
    }

    for (offset; offset; --offset)
        this->append('0');
}

