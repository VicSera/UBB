#include "Vector.h"

Vector* createVector(FreeFunction freeFunction, CopyFunction copyFunction)
{
	Vector* vector = (Vector*)malloc(sizeof(Vector));

	if (!vector)
		return NULL;

	vector->items = (void**)malloc(INITIAL_SIZE * sizeof(void*));

	if (!vector->items)
	{
		free(vector);
		return NULL;
	}

	vector->capacity = INITIAL_SIZE;
	vector->count = 0;
	vector->freeItem = freeFunction;
	vector->copyItem = copyFunction;

	return vector;
}

Vector* copyVector(Vector* vector)
{
	Vector* vectorCopy = (Vector*)malloc(sizeof(Vector));

	if (!vectorCopy)
		return NULL;

	void** itemsCopy = (void**)malloc(vector->capacity * sizeof(void*));

	if (!itemsCopy)
	{
		free(vectorCopy);
		return NULL;
	}

	// Copy the actual elements
	for (unsigned int index = 0; index < vector->count; ++index)
		itemsCopy[index] = vector->copyItem(vector->items[index]);

	vectorCopy->items = itemsCopy;

	// Copy the vector metadata
	vectorCopy->capacity = vector->capacity;
	vectorCopy->count = vector->count;
	vectorCopy->freeItem = vector->freeItem;
	vectorCopy->copyItem = vector->copyItem;

	return vectorCopy;
}

void sort(Vector* vector, ComparisonFunction ordered)
{
	int sorted;
	unsigned int ceiling = 1;
	do
	{
		sorted = TRUE;
		
		for (unsigned int i = 0; i < vector->count - ceiling; ++i)
			if (ordered(vector->items[i], vector->items[i + 1]) == FALSE)
			{
				void* itemCopy = vector->items[i];
				vector->items[i] = vector->items[i + 1];
				vector->items[i + 1] = itemCopy;

				sorted = FALSE;
			}

		++ceiling;

	} while (!sorted);
}

void freeVector(Vector* vector)
{
	// Free each element
	for (unsigned int index = 0; index < vector->count; ++index)
		vector->freeItem(vector->items[index]);

	// Free the list of references
	free(vector->items);

	// Free the vector structure itself
	free(vector);
}

int addElement(Vector* vector, void* item)
{
	if (!vector)
		return ALLOCATION_ERROR;

	if (vector->count == vector->capacity)
	{
		// Maximum capacity reached
		vector->capacity *= RESIZE_SCALE;
		void** newItems = (void**)realloc(vector->items, vector->capacity);

		if (newItems)
			vector->items = newItems;
		else
			return ALLOCATION_ERROR;  // A larger memory sequence was not found
	}

	vector->items[vector->count++] = item;

	return DONE;
}

int removeElement(Vector* vector, unsigned int position)
{
	if (!vector)
		return ALLOCATION_ERROR;

	if (position < 0 || position >= vector->count)
		return OUT_OF_RANGE;

	// Free the element's memory location
	vector->freeItem(vector->items[position]);

	// Shift all the other items one spot to the left
	for (unsigned int index = position; index < vector->count - 1; ++index)
	{
		vector->items[index] = vector->items[index + 1];
	}

	--(vector->count);

	return DONE;
}

int updateElement(Vector* vector, void* item, unsigned int position)
{
	if (!vector)
		return ALLOCATION_ERROR;

	if (position < 0 || position >= vector->count)
		return OUT_OF_RANGE;

	// Free the previous element
	vector->freeItem(vector->items[position]);

	// Reference the new element
	vector->items[position] = item;

	return DONE;
}

void* getFromPosition(Vector* vector, unsigned int position)
{
	if (position < 0 || position >= vector->count)
		return NULL;

	return vector->items[position];
}

unsigned int getCount(Vector* vector)
{
	return vector->count;
}

void** getItems(Vector* vector)
{
	return vector->items;
}

void removeStartingFrom(Vector* vector, unsigned int startingPosition)
{
	for (unsigned int index = startingPosition; index < vector->count; ++index)
		vector->freeItem(vector->items[index]);
	vector->count = startingPosition;
}