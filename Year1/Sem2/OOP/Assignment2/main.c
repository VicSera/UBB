#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct _Point {
    int x;
    int y;
} Point;

Point* readPoint()
{
    char input[10];
    scanf("%s", input);

    if (strcmp (input, "exit") == 0)
        return NULL;

    Point* newPoint = (Point*) malloc (sizeof(Point));
    newPoint->x = (int) strtol (input, NULL, 10);
    scanf ("%d", &(newPoint->y));

    return newPoint;
}

Point* readInput(unsigned int* numberOfPoints)
{
    Point* points = (Point*) malloc (25 * sizeof(Point));
    *numberOfPoints = 0;

    while(1)
    {
        Point* point = readPoint();

        if (!point)
            break;

        points[*numberOfPoints] = *point;
        free(point);

        ++(*numberOfPoints);
    }

    return points;
}

int collinear(Point* firstPoint, Point* secondPoint)
{
    return ((float)firstPoint->x / firstPoint->y == (float)secondPoint->x / secondPoint->y);
}

int ordered(Point* firstPoint, Point* secondPoint)
{
    return firstPoint->x >= secondPoint->x;
}

void getLongestCollinearSubsequence(Point* points, unsigned int numberOfPoints, unsigned int* start, unsigned int* sequenceLength)
{
    *start = 0;
    *sequenceLength = 1;

    unsigned int currentStart = 0;
    unsigned int currentLength = 1;

    for (unsigned int i = 1; i < numberOfPoints; ++i)
    {
        // Skip the first point, since collinearity is not a unary property
        // For each point, check if it's collinear with its left neighbor
        if (collinear(points + i, points + i - 1), ordered(points + i, points + i - 1))
        {
            ++currentLength;
            if (currentLength > *sequenceLength)
            {
                *sequenceLength = currentLength;
                *start = currentStart;
            }
        }
    }
}

//TEST INPUT
void printPoints(Point* points, unsigned int numberOfPoints)
{
    for (unsigned int i = 0; i < numberOfPoints; ++i)
        printf("%d %d ", points[i].x, points[i].y);
}

int main() {
    unsigned int numberOfPoints = 0, sequenceStart, sequenceLength;
    Point* points;

    points = readInput(&numberOfPoints);

    getLongestCollinearSubsequence(points, numberOfPoints, &sequenceStart, &sequenceLength);
    printPoints(points + sequenceStart, sequenceLength);
    return 0;
}
