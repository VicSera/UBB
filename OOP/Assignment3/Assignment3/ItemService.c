#include "ItemService.h"

ItemService* createService(ItemRepository* repository)
{
	ItemService* service = (ItemService*)malloc(sizeof(ItemService));
	service->repository = repository;

	return service;
}

int addItem(ItemService* itemService, unsigned int catalogueNumber, char* state, char* type, unsigned int value)
{
	Item* newItem = (Item*)malloc(sizeof(Item));
	newItem->catalogueNumber = catalogueNumber;
	newItem->state = (char*)malloc(30 * sizeof(char));
	newItem->type = (char*)malloc(30 * sizeof(char));
	strcpy(newItem->state, state);
	strcpy(newItem->type,type);
	newItem->value = value;

	return add(itemService->repository, newItem);
}

int updateItem(ItemService* itemService, unsigned int catalogueNumber, char* state, char* type, unsigned int value)
{
	Item* updatedItem = (Item*)malloc(sizeof(Item));
	updatedItem->catalogueNumber = catalogueNumber;
	updatedItem->state = (char*)malloc(30 * sizeof(char));
	updatedItem->type = (char*)malloc(30 * sizeof(char));
	strcpy(updatedItem->state, state);
	strcpy(updatedItem->type, type);
	updatedItem->value = value;

	return update(itemService->repository, updatedItem);
}

int deleteItem(ItemService* itemService, unsigned int catalogueNumber)
{
	return removeItem(itemService->repository, catalogueNumber);
}

Item** getItems(ItemService* itemService, unsigned int* count)
{
	*count = itemService->repository->count;
	return itemService->repository->items;
}

Item** getItemsByType(ItemService* itemService, char* type, unsigned int* count)
{
	Item** items = itemService->repository->items;
	Item** filteredItems = (Item**)malloc(itemService->repository->count * sizeof(Item*));
	*count = 0;

	for (unsigned int index = 0; index < itemService->repository->count; ++index)
	{
		if (strcmp(type, items[index]->type) == 0)
			filteredItems[(*count)++] = items[index];
	}

	Item** truncatedFilteredItems = (Item**)realloc(filteredItems, *count * sizeof(Item*));

	if (!truncatedFilteredItems)
		free(filteredItems);

	return truncatedFilteredItems;
}