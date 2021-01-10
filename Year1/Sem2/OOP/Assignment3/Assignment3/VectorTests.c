#include "VectorTests.h"

void runVectorTests()
{
	createVector_empty_length0();
	copyVector_sameLength();
	copyVector_removeElement_changesNotShared();
	addElement_lengthChanged();
	removeElement_lengthChanged();
	removeElement_outOfBounds_exitCodeOutOfRange();
}

void createVector_empty_length0()
{
	Vector* vector = createVector(NULL, NULL);

	assert(getCount(vector) == 0);

	freeVector(vector);
}

void copyVector_sameLength()
{
	Vector* vector = createVector(freeItem, copyItem);
	Item* item = createItem(1, "a", "a", 1);

	addElement(vector, item);
	Vector* vectorCopy = copyVector(vector);

	assert(getCount(vector) == 1 && getCount(vectorCopy) == 1);

	freeVector(vector);
	freeVector(vectorCopy);
}

void copyVector_removeElement_changesNotShared()
{
	Vector* vector = createVector(freeItem, copyItem);
	Item* item = createItem(1, "a", "a", 1);

	addElement(vector, item);
	Vector* vectorCopy = copyVector(vector);

	removeElement(vectorCopy, 0);

	assert(getCount(vector) == 1 && getCount(vectorCopy) == 0);

	freeVector(vector);
	freeVector(vectorCopy);
}

void addElement_lengthChanged()
{
	Vector* vector = createVector(freeItem, copyItem);
	Item* item = createItem(1, "a", "a", 1);

	addElement(vector, item);

	assert(getCount(vector) == 1);

	freeVector(vector);
}

void removeElement_lengthChanged()
{
	Vector* vector = createVector(freeItem, copyItem);
	Item* item = createItem(1, "a", "a", 1);

	addElement(vector, item);
	removeElement(vector, 0);

	assert(getCount(vector) == 0);

	freeVector(vector);
}

void removeElement_outOfBounds_exitCodeOutOfRange()
{
	Vector* vector = createVector(freeItem, copyItem);
	
	assert(removeElement(vector, 0) == OUT_OF_RANGE);

	freeVector(vector);
}



