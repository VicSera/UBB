#pragma once
#define _CRT_SECURE_NO_WARNINGS
#include <string.h>
#include <crtdbg.h>
#include <stdlib.h>
#include "common.h"

typedef struct _Item
{
	unsigned int catalogueNumber;
	char* state;
	char* type;
	unsigned int value;
} Item;

Item* createItem(unsigned int catalogueNumber, char* state, char* type, unsigned int value);

void freeItem(Item* item);

unsigned int getItemId(Item* item);

Item* copyItem(Item* item);

int orderedByName(Item* firstItem, Item* secondItem);

int orderedByNameReverse(Item* firstItem, Item* secondItem);