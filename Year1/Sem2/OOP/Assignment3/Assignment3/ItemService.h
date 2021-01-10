#pragma once
#define _CRT_SECURE_NO_WARNINGS

#include "ItemRepository.h"
#include <string.h>

typedef int (*FilterFunction)(Item* item, void* filterParameter);

typedef struct _ItemService
{
	ItemRepository* repository;
} ItemService;

ItemService* createService(ItemRepository* repository);

void freeService(ItemService* itemService);

int serviceAddItem(ItemService* itemService, unsigned int catalogueNumber, char* state, char* type, unsigned int value);

int serviceDeleteItem(ItemService* itemService, unsigned int catalogueNumber);

int serviceUpdateItem(ItemService* itemService, unsigned int catalogueNumber, char* state, char* type, unsigned int value);

Vector* serviceGetItems(ItemService* itemService);

Vector* serviceGetFilteredItems(ItemService* itemService, FilterFunction filter, void* filterParameter);

int filterByType(Item* item, char* type);

int filterByTypeLength(Item* item, unsigned int* maxLength);

int filterByMaxValue(Item* item, unsigned int* maxValue);

int serviceUndo(ItemService* itemService);

int serviceRedo(ItemService* itemService);