#pragma once

#include <stdlib.h>
#include "common.h"

#define INITIAL_SIZE 10
#define RESIZE_SCALE 2

typedef void (*FreeFunction)(void*);
typedef void* (*CopyFunction)(void*);
typedef int (*ComparisonFunction)(void*, void*);

typedef struct _Vector 
{
	void** items;
	unsigned int count, capacity;
	FreeFunction freeItem;
	CopyFunction copyItem;
} Vector;

Vector* createVector(FreeFunction freeFunction, CopyFunction copyFunction);

Vector* copyVector(Vector* vector);

void sort(Vector* vector, ComparisonFunction);

void freeVector(Vector* vector);

int addElement(Vector* vector, void* item);

int removeElement(Vector* vector, unsigned int position);

int updateElement(Vector* vector, void* item, unsigned int position);

void* getFromPosition(Vector* vector, unsigned int position);

unsigned int getCount(Vector* vector);

void** getItems(Vector* vector);

void removeStartingFrom(Vector* vector, unsigned int startingPosition);