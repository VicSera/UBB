#include "ItemRepository.h"

ItemRepository* createRepository(unsigned int initialSize)
{
	ItemRepository* repository = (ItemRepository*)malloc(sizeof(ItemRepository));
	repository->maxSize = initialSize;
	repository->count = 0;
	repository->items = (Item*)malloc(initialSize * sizeof(Item));

	return repository;
}

int addItem(ItemRepository* itemRepository, Item* item)
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

	itemRepository->items[itemRepository->count] = *item;
	++(itemRepository->count);

	return 0;
}

int deleteItem(ItemRepository* itemRepository, unsigned int catalogueNumber)
{
	unsigned int itemIndex = getIndexById(itemRepository, catalogueNumber);

	if (itemIndex == -1)
	{
		// the given catalogueNumber does not exist
		return -1;
	}

	// Shift all the other items one spot to the left
	for (unsigned int index = itemIndex; index < itemRepository->count - 1; ++index)
	{
		itemRepository[index] = itemRepository[index + 1];
	}

	--(itemRepository->count);

	return 0;
}

Item* getById(ItemRepository* itemRepository, unsigned int catalogueNumber)
{
	for (unsigned int iterator = 0; iterator < itemRepository->count; ++iterator)
	{
		if (itemRepository->items[iterator].catalogueNumber == catalogueNumber)
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
		if (itemRepository->items[iterator].catalogueNumber == catalogueNumber)
		{
			return iterator;
		}
	}

	return -1;
}
