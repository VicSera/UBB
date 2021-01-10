#include <iostream>
#include "CrossBase/crossbase.h"

int main()
{
    //num A("7003", 10), B("3", 10);
    num A("21", 10), B("8", 10);

    std::cout << A.convert_base(16) << std::endl;
#if 0
    std::cout << A << " + " << B << " = " << (A + B) << '\n';
    std::cout << B << " + " << A << " = " << (B + A) << '\n';
    std::cout << A << " - " << B << " = " << (A - B) << '\n';
    std::cout << B << " - " << A << " = " << (B - A) << '\n';
    std::cout << A << " == " << B << " = " << (A == B) << '\n';
    std::cout << A << " < " << B << " = " << (A < B) << '\n';
    std::cout << A << " > " << B << " = " << (A > B) << '\n';
    std::cout << A << " <= " << B << " = " << (A <= B) << '\n';
    std::cout << A << " >= " << B << " = " << (A >= B) << '\n';
#endif
    return 0;
}
