#include "ItemRepository.h"

ItemRepository* createRepository()
{
	ItemRepository* repository = (ItemRepository*)malloc(sizeof(ItemRepository));
	
	if (!repository)
		return NULL;

	repository->itemVector = createVector(freeItem, copyItem);

	// Initialize the state vector and state id used for the undo/redo functionality
	repository->stateVector = createVector(freeVector, copyVector);
	repository->stateId = 0;
	addElement(repository->stateVector, copyVector(repository->itemVector));

	return repository;
}

void freeRepository(ItemRepository* itemRepository)
{
	freeVector(itemRepository->itemVector);
	freeVector(itemRepository->stateVector);
	free(itemRepository);
}

int addItem(ItemRepository* itemRepository, Item* item)
{
	if (findPosition(itemRepository->itemVector, item->catalogueNumber) != NOT_FOUND)
		return ALREADY_EXISTS;

	int exitCode = addElement(itemRepository->itemVector, (void*)item);

	if (exitCode == DONE)
		registerChanges(itemRepository);

	return exitCode;
}

int updateItem(ItemRepository* itemRepository, Item* item)
{
	unsigned int position = findPosition(itemRepository->itemVector, item->catalogueNumber);

	if (position == NOT_FOUND)
		return NOT_FOUND;

	int exitCode = updateElement(itemRepository->itemVector, (void*)item, position);

	if (exitCode == DONE)
		registerChanges(itemRepository);

	return exitCode;
}

int removeItem(ItemRepository* itemRepository, unsigned int catalogueNumber)
{
	unsigned int position = findPosition(itemRepository->itemVector, catalogueNumber);

	if (position == NOT_FOUND)
		return NOT_FOUND;

	int exitCode = removeElement(itemRepository->itemVector, position);

	if (exitCode == DONE)
		registerChanges(itemRepository);

	return exitCode;
}

Vector* getAllItems(ItemRepository* itemRepository)
{
	return itemRepository->itemVector;
}

Vector* getAllItemsCopy(ItemRepository* itemRepository)
{
	return copyVector(itemRepository->itemVector);
}

static int findPosition(Vector* itemVector, unsigned int id)
{
	Item** items = getItems(itemVector);
	for (unsigned int index = 0; index < itemVector->count; ++index)
		if (items[index]->catalogueNumber == id)
			return index;
	return NOT_FOUND;
}

static void registerChanges(ItemRepository* itemRepository)
{
	++itemRepository->stateId;

	// Remove any states that could've been restored by using redo, which will be unaccessible
	removeStartingFrom(itemRepository->stateVector, itemRepository->stateId);

	addElement(itemRepository->stateVector, copyVector(itemRepository->itemVector));
}

int undo(ItemRepository* itemRepository)
{
	if (itemRepository->stateId == 0)
		return OUT_OF_RANGE;

	--itemRepository->stateId;

	// Discard the currend list of items
	freeVector(itemRepository->itemVector);

	// Restore the previous state
	itemRepository->itemVector = copyVector(getItems(itemRepository->stateVector)[itemRepository->stateId]);

	return DONE;
}

int redo(ItemRepository* itemRepository)
{
	if (itemRepository->stateId == getCount(itemRepository->stateVector) - 1)
		return OUT_OF_RANGE;

	++itemRepository->stateId;

	// Discard the currend list of items
	freeVector(itemRepository->itemVector);

	// Restore the previous state
	itemRepository->itemVector = copyVector(getItems(itemRepository->stateVector)[itemRepository->stateId]);

	return DONE;
}

