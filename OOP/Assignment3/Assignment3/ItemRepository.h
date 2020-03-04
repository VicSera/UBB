#pragma once
#include "Item.h"

typedef struct _ItemRepository 
{
	Item* items;
	unsigned int count;
	unsigned int maxSize;
} ItemRepository;

ItemRepository* createRepository(unsigned int initialSize);

int addItem(ItemRepository* itemRepository, Item* item);

int deleteItem(ItemRepository* itemRepository, unsigned int catalogueNumber);

void updateItem(ItemRepository* itemRepository, Item* item);

Item* getById(ItemRepository* itemRepository, unsigned int catalogueNumber);

unsigned int getIndexById(ItemRepository* itemRepository, unsigned int catalogueNumber);

Item* getItems(ItemRepository* itemRepository);

Item* getItemsByType(ItemRepository* itemRepository, char* type);
