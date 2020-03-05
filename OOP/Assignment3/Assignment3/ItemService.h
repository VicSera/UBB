#pragma once
#define _CRT_SECURE_NO_WARNINGS

#include "ItemRepository.h"
#include <string.h>

typedef struct _ItemService
{
	ItemRepository* repository;
} ItemService;

ItemService* createService(ItemRepository* repository);

int addItem(ItemService* itemService, unsigned int catalogueNumber, char* state, char* type, unsigned int value);

int deleteItem(ItemService* itemService, unsigned int catalogueNumber);

int updateItem(ItemService* itemService, unsigned int catalogueNumber, char* state, char* type, unsigned int value);

Item** getItems(ItemService* itemService, unsigned int* count);

Item** getItemsByType(ItemService* itemService, char* type, unsigned int* count);