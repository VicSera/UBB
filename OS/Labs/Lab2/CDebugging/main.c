#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

int randomNumber()
{
	return rand() % 5 + 1;
}

int main()
{
	// Matrix size
	unsigned int n;

	//srand(time(NULL));
	srand(getpid());

	printf("Please input the matrix size: ");
	// Read input
	scanf("%u", &n);

	unsigned int** matrix = (unsigned int**)malloc(n * sizeof(unsigned int*));

	// Allocate space and fill the matrix with random numbers
	for (unsigned int i = 0; i < n; ++i)
	{
		matrix[i] = (unsigned int*)malloc(n * sizeof(unsigned int));

		for (unsigned int j = 0; j < n; ++j)
		{
			matrix[i][j] = randomNumber();
			printf("%d ", matrix[i][j]);
		}
		printf("\n");
	}

	// Free the matrix
	for (unsigned int i = 0; i < n; ++i)
		free(matrix[i]);
	free(matrix);

	return 0;
}
