#pragma once
#define _CRT_SECURE_NO_WARNINGS

#include "Item.h"
#include "Vector.h"
#include <stdlib.h>

typedef struct _ItemRepository 
{
	Vector* itemVector;   // The current state
	Vector* stateVector;  // The past states
	unsigned int stateId;
} ItemRepository;

ItemRepository* createRepository();

void freeRepository(ItemRepository* itemRepository);

int addItem(ItemRepository* itemRepository, Item* item);

int removeItem(ItemRepository* itemRepository, unsigned int catalogueNumber);

int updateItem(ItemRepository* itemRepository, Item* item);

Vector* getAllItems(ItemRepository* itemRepository);

Vector* getAllItemsCopy(ItemRepository* itemRepository);

int undo(ItemRepository* itemRepository);

int redo(ItemRepository* itemRepository);

static void registerChanges(ItemRepository* itemRepository);