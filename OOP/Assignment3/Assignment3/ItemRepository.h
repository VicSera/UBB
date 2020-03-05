#pragma once
#define _CRT_SECURE_NO_WARNINGS

#include "Item.h"
#include <stdlib.h>

typedef struct _ItemRepository 
{
	Item** items;
	unsigned int count;
	unsigned int maxSize;
} ItemRepository;

ItemRepository* createRepository(unsigned int initialSize);

int add(ItemRepository* itemRepository, Item* item);

int removeItem(ItemRepository* itemRepository, unsigned int catalogueNumber);

int update(ItemRepository* itemRepository, Item* item);

Item* getById(ItemRepository* itemRepository, unsigned int catalogueNumber);

unsigned int getIndexById(ItemRepository* itemRepository, unsigned int catalogueNumber);
