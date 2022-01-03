/* A distributed program, using MPI, that sums up the elements in a vector of integers.
  - The main process splits the vector into equal size chunks and distributes them to all processes (including to itself),
  - each process sums the numbers in its chunk and sends the sum back to the main process
  - the main process gets the sums of the chunks, sums them and prints the result

This example uses regular MPI_Ssend() to distribute the data to the worker nodes (processes).
*/

#include <iostream>
#include <mpi.h>
#include <vector>
#include <chrono>

using namespace std;

#define TAG_LENGTH_P1 1
#define TAG_P1 2
#define TAG_LENGTH_P2 3
#define TAG_P2 4
#define TAG_START_POWER 5
#define TAG_END_POWER 6
#define TAG_COEFFICIENTS 7

#define VERBOSE_LOGGING false

int d(int power, const vector<int>& p1, const vector<int>& p2) {
    return p1[power] * p2[power];
}

int d(int power1, int power2, const vector<int>& p1, const vector<int>& p2) {
    return (p1[power1] + p1[power2]) * (p2[power1] + p2[power2]);
}

int computeCoefficient(int power, const vector<int>& p1, const vector<int>& p2)
{
    const auto degree = (int)std::max(p1.size(), p2.size()) - 1;
    auto t1 = 0, t2 = 0, t3 = 0;

    if (power == 0)
        return d(0, p1, p2);
    else if (power == 2 * degree)
        return d(degree, p1, p2);

    for (auto s = 0; s <= power / 2; ++s)
    {
        const auto t = power - s;
        if (s <= degree && t <= degree & s < t)
        {
            t1 += d(s, t, p1, p2);
            t2 += d(s, p1, p2) + d(t, p1, p2);
        }
    }


    if (power % 2 == 0)
        t3 = d(power / 2, p1, p2);

    return t1 - t2 + t3;
}

void printVector(const vector<int>& v) {
    std::for_each(v.begin(), v.end(), [](const int& coeff){
        printf("%d ", coeff);
    });
    printf("\n");
}

// generates a random vector, to be used as input
void generate(vector<int>& v, size_t n)
{
    v.reserve(n);
    for(size_t i=0 ; i<n ; ++i) {
        v.push_back(rand() % 10);
    }
}

vector<int> partialMultiplication(int coefficient, int power, const vector<int>& polynomial)
{
    vector<int> result(polynomial.size() + power, 0);

    for (auto currentPower = 0; currentPower < polynomial.size(); ++currentPower)
        result[currentPower + power] = polynomial[currentPower] * coefficient;

    return result;
}

vector<int> polynomialSum(const vector<int>& p1, const vector<int>& p2)
{
    const auto& bigger = p1.size() > p2.size() ? p1 : p2;
    const auto& smaller = p1.size() > p2.size() ? p2 : p1;

    vector<int> result(bigger.size());

    for (auto power = 0; power < smaller.size(); ++power)
        result[power] = smaller[power] + bigger[power];
    for (auto power = smaller.size(); power < bigger.size(); ++power)
        result[power] = bigger[power];

    return result;
}

// computes and checks the result, to prove that the program is correct
bool checkResult(const vector<int>& p1, const vector<int>& p2, const vector<int>& computed) {
    vector<int> expected(p1.size() + p2.size() - 1, 0);

    for (auto power = 0; power < p1.size(); ++power)
        expected = polynomialSum(expected, partialMultiplication(p1[power], power, p2));

    printf("Checking:\nExpected: ");
    printVector(expected);
    printf("Computed: ");
    printVector(computed);

    for (auto power = 0; power < expected.size(); ++power)
        if (expected[power] != computed[power])
            return false;

    return true;
}

// The code to be executed by a worker thread.
// I. It receives the length of p1
// II. It receives p1
// III. It receives the length of p2
// IV. It receives p2
// V. It receives the first and last powers to compute
// VI. It calculates the coefficients
// VII. It sends coefficients back
void worker(int me) {
    int numPowers, lengthP1, lengthP2, startPower, endPower;
    MPI_Status status;

    // I.
    MPI_Recv(&lengthP1, 1, MPI_INT, 0, TAG_LENGTH_P1, MPI_COMM_WORLD, &status);

#if VERBOSE_LOGGING
    printf("PROCESS %d: received lengthP1 = %d\n", me, lengthP1);
#endif

    // II.
    vector<int> p1(lengthP1);
    MPI_Recv(p1.data(), lengthP1, MPI_INT, 0, TAG_P1, MPI_COMM_WORLD, &status);

#if VERBOSE_LOGGING
    printf("PROCESS %d: successfully received p1 = ", me);
    printVector(p1);
#endif

    // III.
    MPI_Recv(&lengthP2, 1, MPI_INT, 0, TAG_LENGTH_P2, MPI_COMM_WORLD, &status);

#if VERBOSE_LOGGING
    printf("PROCESS %d: received lengthP2 = %d\n", me, lengthP2);
#endif

    // IV.
    vector<int> p2(lengthP2);
    MPI_Recv(p2.data(), lengthP2, MPI_INT, 0, TAG_P2, MPI_COMM_WORLD, &status);

#if VERBOSE_LOGGING
    printf("PROCESS %d: successfully received p2 = ", me);
    printVector(p2);
#endif

    // V.
    MPI_Recv(&startPower, 1, MPI_INT, 0, TAG_START_POWER, MPI_COMM_WORLD, &status);
    MPI_Recv(&endPower, 1, MPI_INT, 0, TAG_END_POWER, MPI_COMM_WORLD, &status);

    // VI.
    vector<int> coefficients(endPower - startPower);
    for (auto power = startPower; power < endPower; ++power)
    {
        coefficients[power - startPower] = computeCoefficient(power, p1, p2);
#if VERBOSE_LOGGING
        printf("PROCESS %d: computed coefficient for power %d = %d\n", me, power, coefficients[power - startPower]);
#endif
    }

    // VII.
    MPI_Ssend(coefficients.data(), endPower - startPower, MPI_INT, 0, TAG_COEFFICIENTS, MPI_COMM_WORLD);

#if VERBOSE_LOGGING
    printf("PROCESS %d: sent result = ", me);
    printVector(coefficients);
#endif
}

// The code to be executed by the master thread.
vector<int> multiplyPolynomials(const vector<int>& p1, const vector<int>& p2, int numProcesses)
{
    auto resultSize = 2 * ((int)std::max(p1.size(), p2.size()) - 1) + 1;

    for(int i = 1; i < numProcesses; ++ i)
    {
        int startPower = (i * resultSize) / numProcesses;
        int endPower = ((i + 1) * resultSize) / numProcesses;

        // I.
        auto p1Length = (int)p1.size();
        MPI_Ssend(&p1Length, 1, MPI_INT, i, TAG_LENGTH_P1, MPI_COMM_WORLD);

#if VERBOSE_LOGGING
        printf("MASTER: sent p1Length = %d to PROCESS %d\n", p1Length, i);
#endif

        // II.
        MPI_Ssend(p1.data(), p1Length, MPI_INT, i, TAG_P1, MPI_COMM_WORLD);

#if VERBOSE_LOGGING
        printf("MASTER: sent p1 to PROCESS %d\n", i);
#endif

        // III.
        auto p2Length = (int)p2.size();
        MPI_Ssend(&p2Length, 1, MPI_INT, i, TAG_LENGTH_P2, MPI_COMM_WORLD);

#if VERBOSE_LOGGING
        printf("MASTER: sent p2Length = %d to PROCESS %d\n", p2Length, i);
#endif

        // IV.
        MPI_Ssend(p2.data(), p2Length, MPI_INT, i, TAG_P2, MPI_COMM_WORLD);

#if VERBOSE_LOGGING
        printf("MASTER: sent p2 to PROCESS %d\n", i);
#endif

        // V.
        MPI_Ssend(&startPower, 1, MPI_INT, i, TAG_START_POWER, MPI_COMM_WORLD);
        MPI_Ssend(&endPower, 1, MPI_INT, i, TAG_END_POWER, MPI_COMM_WORLD);
    }

    vector<int> result(resultSize);

    for(int power = 0; power < resultSize / numProcesses; ++power)
    {
        result[power] = computeCoefficient(power, p1, p2);

#if VERBOSE_LOGGING
        printf("MASTER: calculated coefficient for power %d = %d\n", power, result[power]);
#endif
    }

    for(int i = 1; i < numProcesses; ++ i)
    {
        int startPower = (i * resultSize) / numProcesses;
        int endPower = ((i + 1) * resultSize) / numProcesses;
        MPI_Status status;

        // VII.
        vector<int> coefficients(endPower - startPower);

        MPI_Recv(coefficients.data(), endPower - startPower, MPI_INT, i, TAG_COEFFICIENTS, MPI_COMM_WORLD, &status);

        for (auto power = startPower; power < endPower; ++power)
        {
            result[power] = coefficients[power - startPower];
#if VERBOSE_LOGGING
            printf("MASTER: received coefficient for power %d from PROCESS %d = %d\n", power, i, coefficients[power - startPower]);
#endif
        }
    }

    return result;
}

int main(int argc, char** argv)
{
    srand(time(nullptr));

    MPI_Init(nullptr, nullptr);
    int me;
    int numProcesses;
    MPI_Comm_size(MPI_COMM_WORLD, &numProcesses);
    MPI_Comm_rank(MPI_COMM_WORLD, &me);

    unsigned n;
    vector<int> p1;
    vector<int> p2;

    if(argc != 2 || 1 != sscanf(argv[1], "%u", &n) ){
        fprintf(stderr, "usage: sum-mpi <n>\n");
        return 1;
    }


    {
        using namespace chrono;
        if(me == 0) {
            generate(p1, n);
            generate(p2, n);
            printf("Generated polynomials\n");

            printVector(p1);
            printVector(p2);

            high_resolution_clock::time_point const beginTime = high_resolution_clock::now();

            auto result = multiplyPolynomials(p1, p2, numProcesses);
            high_resolution_clock::time_point const endTime = high_resolution_clock::now();

            printf("Result %s, finished in %ld milliseconds\n", (checkResult(p1, p2, result) ? "CORRECT" : "WRONG"),
                   (duration_cast<milliseconds>(endTime-beginTime)).count());
        } else {
            // worker
            high_resolution_clock::time_point const beginTime = high_resolution_clock::now();
            worker(me);
            high_resolution_clock::time_point const endTime = high_resolution_clock::now();

            printf("PROCESS %d: finished in %ld milliseconds\n", me,
                   (duration_cast<milliseconds>(endTime-beginTime)).count());
        }
    }

    MPI_Finalize();
}