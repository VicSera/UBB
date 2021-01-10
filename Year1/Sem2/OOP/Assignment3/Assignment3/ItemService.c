#include "ItemService.h"

ItemService* createService(ItemRepository* repository)
{
	ItemService* service = (ItemService*)malloc(sizeof(ItemService));
	service->repository = repository;

	return service;
}

void freeService(ItemService* itemService)
{
	freeRepository(itemService->repository);
	free(itemService);
}

int serviceAddItem(ItemService* itemService, unsigned int catalogueNumber, char* state, char* type, unsigned int value)
{
	Item* newItem = createItem(catalogueNumber, state, type, value);

	int errorCode = addItem(itemService->repository, newItem);

	if (errorCode != DONE)
		freeItem(newItem);

	return errorCode;
}

int serviceUpdateItem(ItemService* itemService, unsigned int catalogueNumber, char* state, char* type, unsigned int value)
{
	Item* updatedItem = createItem(catalogueNumber, state, type, value);

	int errorCode = updateItem(itemService->repository, updatedItem);

	if (errorCode != DONE)
		freeItem(updatedItem);

	return errorCode;
}

int serviceDeleteItem(ItemService* itemService, unsigned int catalogueNumber)
{
	return removeItem(itemService->repository, catalogueNumber);
}

Vector* serviceGetItems(ItemService* itemService)
{
	return getAllItemsCopy(itemService->repository);
}

Vector* serviceGetFilteredItems(ItemService* itemService, FilterFunction filter, void* filterParameter)
{	
	// Get a copy of all the items
	Vector* vector = getAllItems(itemService->repository);
	Vector* filteredVector = createVector(freeItem, copyItem);

	for (unsigned int index = 0; index < vector->count; ++index)
	{
		// Call the filter function with 
		if (filter(vector->items[index], filterParameter))
			addElement(filteredVector, copyItem(vector->items[index]));
	}

	return filteredVector;
}

int filterByType(Item* item, char* type)
{
	if (strcmp(item->type, type) == 0)
		return TRUE;
	return FALSE;
}

int filterByTypeLength(Item* item, unsigned int* maxLength)
{
	if (strlen(item->type) >= maxLength)
		return FALSE;
	return TRUE;
}

int filterByMaxValue(Item* item, unsigned int* maxValue)
{
	return item->value < *maxValue;
}

int serviceUndo(ItemService* itemService)
{
	return undo(itemService->repository);
}

int serviceRedo(ItemService* itemService)
{
	return redo(itemService->repository);
}