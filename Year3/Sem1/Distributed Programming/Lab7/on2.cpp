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

#define TAG_NUM_PAIRS 1
#define TAG_PAIRS 2
#define TAG_LENGTH_P2 3
#define TAG_P2 4
#define TAG_PARTIAL_RESULT_SIZE 5
#define TAG_PARTIAL_RESULT 6

#define VERBOSE_LOGGING false

void printVector(const vector<int>& v) {
    std::for_each(v.begin(), v.end(), [](const int& coeff){
        printf("%d ", coeff);
    });
    printf("\n");
}

void printEntries(const int buffer[], const int numPairs) {
    for (auto pairNum = 0; pairNum < numPairs; ++pairNum)
        printf("(p: %d, c: %d) ", buffer[pairNum * 2], buffer[pairNum * 2 + 1]);
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
// I. It receives the number (numPairs) of (power, coefficient) pairs to multiply by
// II. It receives numPairs pairs of integers
// III. It receives the length (polynomialSize) of the polynomial to multiply
// IV. It receives polynomialSize coefficients that make up the polynomial
// V. It computes the partial multiplications and sums them up
// VI. It sends the partial result back to the source
void worker(int me) {
    int numPairs, polynomialSize;
    MPI_Status status;

    // I.
    MPI_Recv(&numPairs, 1, MPI_INT, 0, TAG_NUM_PAIRS, MPI_COMM_WORLD, &status);

#if VERBOSE_LOGGING
    printf("PROCESS %d: received numPairs = %d\n", me, numPairs);
#endif

    // II.
    int* pairBuffer = new int[numPairs * 2];
    MPI_Recv(pairBuffer, numPairs * 2, MPI_INT, 0, TAG_PAIRS, MPI_COMM_WORLD, &status);

#if VERBOSE_LOGGING
    printf("PROCESS %d: successfully received pairs = ", me);
    printPairs(pairBuffer, numPairs);
#endif

    // III.
    MPI_Recv(&polynomialSize, 1, MPI_INT, 0, TAG_LENGTH_P2, MPI_COMM_WORLD, &status);

#if VERBOSE_LOGGING
    printf("PROCESS %d: received polynomialSize = %d\n", me, polynomialSize);
#endif

    // IV.
    vector<int> polynomial(polynomialSize);
    MPI_Recv(polynomial.data(), polynomialSize, MPI_INT, 0, TAG_P2, MPI_COMM_WORLD, &status);

#if VERBOSE_LOGGING
    printf("PROCESS %d: successfully received polynomial = ", me);
    printVector(polynomial);
#endif

    // V.
    vector<int> result(0);
    for (auto pairNumber = 0; pairNumber < numPairs; ++pairNumber)
    {
        const int power = pairBuffer[pairNumber * 2];
        const int coefficient = pairBuffer[pairNumber * 2 + 1];

        auto partialResult = partialMultiplication(coefficient, power, polynomial);
        result = polynomialSum(result, partialResult);

#if VERBOSE_LOGGING
        printf("PROCESS %d: computed partial result = ", me);
        printVector(partialResult);
        printf("PROCESS %d: new result = ", me);
        printVector(result);
#endif
    }

    delete[] pairBuffer;

    // VI.
    auto resultSize = (int)result.size();
    MPI_Ssend(&resultSize, 1, MPI_INT, 0, TAG_PARTIAL_RESULT_SIZE, MPI_COMM_WORLD);

#if VERBOSE_LOGGING
    printf("PROCESS %d: sent resultSize = %d\n", me, resultSize);
#endif

    // VII.
    MPI_Ssend(result.data(), (int)result.size(), MPI_INT, 0, TAG_PARTIAL_RESULT, MPI_COMM_WORLD);

#if VERBOSE_LOGGING
    printf("PROCESS %d: sent result = ", me);
    printVector(result);
#endif
}

// The code to be executed by the master thread.
vector<int> multiplyPolynomials(const vector<int>& p1, const vector<int>& p2, int numProcesses)
{
    auto n = (int)p1.size();

    for(int i = 1; i < numProcesses; ++ i)
    {
        int startIndex = (i * n) / numProcesses;
        int endIndex = ((i + 1) * n) / numProcesses;
        int numPairs = endIndex - startIndex;

        // I.
        MPI_Ssend(&numPairs, 1, MPI_INT, i, TAG_NUM_PAIRS, MPI_COMM_WORLD);

#if VERBOSE_LOGGING
        printf("MASTER: sent numPairs = %d to PROCESS %d\n", numPairs, i);
#endif

        // II.
        int* pairBuffer = new int[numPairs * 2];
        for (auto pairNumber = 0; pairNumber < numPairs; ++pairNumber)
        {
            const auto power = startIndex + pairNumber;
            const auto coefficient = p1[power];

            pairBuffer[2 * pairNumber] = power;
            pairBuffer[2 * pairNumber + 1] = coefficient;
        }

        MPI_Ssend(pairBuffer, numPairs * 2, MPI_INT, i, TAG_PAIRS, MPI_COMM_WORLD);

#if VERBOSE_LOGGING
        printf("MASTER: sent pairs to PROCESS %d\n", i);
#endif

        delete[] pairBuffer;

        // III.
        auto polynomialSize = (int)p2.size();
        MPI_Ssend(&polynomialSize, 1, MPI_INT, i, TAG_LENGTH_P2, MPI_COMM_WORLD);

#if VERBOSE_LOGGING
        printf("MASTER: sent polynomialSize = %d to PROCESS %d\n", polynomialSize, i);
#endif

        // IV.
        MPI_Ssend(p2.data(), polynomialSize, MPI_INT, i, TAG_P2, MPI_COMM_WORLD);

#if VERBOSE_LOGGING
        printf("MASTER: sent polynomial to PROCESS %d\n", i);
#endif
    }

    vector<int> result(0);

    for(int i = 0; i < n / numProcesses; ++ i)
    {
        const auto power = i;
        const auto coefficient = p1[power];
        result = polynomialSum(result, partialMultiplication(coefficient, power, p2));

#if VERBOSE_LOGGING
        printf("MASTER: calculated first partial result = ");
        printVector(result);
#endif
    }

    for(int i = 1; i < numProcesses; ++ i)
    {
        // VI.
        int partialResultSize;
        MPI_Status status;

        MPI_Recv(&partialResultSize, 1, MPI_INT, i, TAG_PARTIAL_RESULT_SIZE, MPI_COMM_WORLD, &status);

#if VERBOSE_LOGGING
        printf("MASTER: received partialResultSize = %d from PROCESS %d\n", partialResultSize, i);
#endif

        // VII.
        vector<int> partialResult(partialResultSize);

        MPI_Recv(partialResult.data(), partialResultSize, MPI_INT, i, TAG_PARTIAL_RESULT, MPI_COMM_WORLD, &status);

#if VERBOSE_LOGGING
        printf("MASTER: received partialResult from PROCESS %d = ", i);
        printVector(partialResult);
#endif

        result = polynomialSum(result, partialResult);
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