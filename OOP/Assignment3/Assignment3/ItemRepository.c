#include "ItemRepository.h"

ItemRepository* createRepository(unsigned int initialSize)
{
	ItemRepository* repository = (ItemRepository*)malloc(sizeof(ItemRepository));
	repository->maxSize = initialSize;
	repository->count = 0;
	repository->items = (Item**)malloc(initialSize * sizeof(Item*));

	return repository;
}

void freeRepository(ItemRepository* itemRepository)
{
	for (unsigned int i = 0; i < itemRepository->count; ++i)
		freeItem(itemRepository->items[i]);
	free(itemRepository->items);
	free(itemRepository);
}

int add(ItemRepository* itemRepository, Item* item)
{
	Item* itemWithSameId = getById(itemRepository, item->catalogueNumber);

	// Check id unicity
	if (itemWithSameId)
	{
		// There is already a number with this id
		return -1;
	}

	// Check if number of items exceeds limit
	if (itemRepository->count >= itemRepository->maxSize)
	{
		// Maximum capacity reached
		return -2;
	}

	itemRepository->items[itemRepository->count] = item;
	++(itemRepository->count);

	return 0;
}

int update(ItemRepository* itemRepository, Item* item)
{
	unsigned int existingIndex = getIndexById(itemRepository, item->catalogueNumber);

	if (existingIndex == -1)
	{
		// There is no existing value to update
		return -1;
	}

	free(itemRepository->items[existingIndex]);
	itemRepository->items[existingIndex] = item;
	return 0;
}

int removeItem(ItemRepository* itemRepository, unsigned int catalogueNumber)
{
	unsigned int itemIndex = getIndexById(itemRepository, catalogueNumber);

	if (itemIndex == -1)
	{
		// the given catalogueNumber does not exist
		return -1;
	}

	// Free the used memory
	free(itemRepository->items[itemIndex]);

	// Shift all the other items one spot to the left
	for (unsigned int index = itemIndex; index < itemRepository->count - 1; ++index)
	{
		itemRepository->items[index] = itemRepository->items[index + 1];
	}

	--(itemRepository->count);

	return 0;
}

Item* getById(ItemRepository* itemRepository, unsigned int catalogueNumber)
{
	for (unsigned int iterator = 0; iterator < itemRepository->count; ++iterator)
	{
		if (itemRepository->items[iterator]->catalogueNumber == catalogueNumber)
		{
			return itemRepository->items + iterator;
		}
	}

	return 0;
}

unsigned int getIndexById(ItemRepository* itemRepository, unsigned int catalogueNumber)
{
	for (unsigned int iterator = 0; iterator < itemRepository->count; ++iterator)
	{
		if (itemRepository->items[iterator]->catalogueNumber == catalogueNumber)
		{
			return iterator;
		}
	}

	return -1;
}