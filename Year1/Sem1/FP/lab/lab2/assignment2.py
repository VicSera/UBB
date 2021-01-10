class complex_number:
    real = 0.
    imaginary = 0.

    def __init__(self):
        self.set(0., 0.)

    def __init__(self, arg_real, arg_imaginary):
        self.set(arg_real, arg_imaginary)

    def get(self):
        return self.real, self.imaginary

    def set(self, arg_real, arg_imaginary):
        if type(arg_imaginary) not in (float, int) or type(arg_real) not in (float, int):
            print("Wrong input type.")
            self.real = 0
            self.imaginary = 0
        else:
            print("Right input type.")
            self.real = arg_real
            self.imaginary = arg_imaginary

if __name__ == '__main__':
    list_of_numbers = []
    complex_number_1 = complex_number('1', 5)
    list_of_numbers.append(complex_number_1.get())
    complex_number_2 = complex_number(1, 5.7)
    list_of_numbers.append(complex_number_2.get())
    print(list_of_numbers)


