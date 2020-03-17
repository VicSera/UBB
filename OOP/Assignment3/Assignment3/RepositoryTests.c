#include "RepositoryTests.h"

void runRepositoryTests()
{
	addItem_uniqueId_addOk();
	addItem_duplicateId_addFail();
	removeItem_existingId_removeOk();
	removeItem_idNotFound_removeFail();
	updateItem_existingId_updateOk();
	updateItem_idNotFound_updateFail();
	undo_addItem_lengthReverts();
	undo_withoutChanges_undoFail();
	redo_addItem_lengthReverts();
	redo_withoutChanges_redoFail();
}

void addItem_uniqueId_addOk()
{
	ItemRepository* repository = createRepository();
	Item* item = createItem(1, "a", "a", 1);

	assert(DONE == addItem(repository, item));

	freeRepository(repository);
}

void addItem_duplicateId_addFail()
{
	ItemRepository* repository = createRepository();
	Item* item = createItem(1, "a", "a", 1);

	addItem(repository, item);
	assert(ALREADY_EXISTS == addItem(repository, item));

	freeRepository(repository);
}

void removeItem_existingId_removeOk()
{
	ItemRepository* repository = createRepository();
	Item* item = createItem(1, "a", "a", 1);

	addItem(repository, item);
	assert(DONE == removeItem(repository, item->catalogueNumber));

	freeRepository(repository);
}

void removeItem_idNotFound_removeFail()
{
	ItemRepository* repository = createRepository();

	assert(NOT_FOUND == removeItem(repository, 1));

	freeRepository(repository);
}

void updateItem_existingId_updateOk()
{
	ItemRepository* repository = createRepository();
	Item* item = createItem(1, "a", "a", 1);
	Item* itemUpdate = createItem(1, "b", "b", 2);

	addItem(repository, item);
	assert(DONE == updateItem(repository, itemUpdate));

	freeRepository(repository);
}

void updateItem_idNotFound_updateFail()
{
	ItemRepository* repository = createRepository();
	Item* item = createItem(1, "a", "a", 1);

	assert(NOT_FOUND == updateItem(repository, item));

	freeItem(item);
	freeRepository(repository);
}

void undo_addItem_lengthReverts()
{
	ItemRepository* repository = createRepository();
	Item* item = createItem(1, "a", "a", 1);

	addItem(repository, item);
	undo(repository);

	assert(getCount(repository->itemVector) == 0);

	freeRepository(repository);
}

void undo_withoutChanges_undoFail()
{
	ItemRepository* repository = createRepository();

	assert(OUT_OF_RANGE == undo(repository));

	freeRepository(repository);
}

void redo_addItem_lengthReverts()
{
	ItemRepository* repository = createRepository();
	Item* item = createItem(1, "a", "a", 1);

	addItem(repository, item);
	undo(repository);
	redo(repository);

	assert(getCount(repository->itemVector) == 1);

	freeRepository(repository);
}

void redo_withoutChanges_redoFail()
{
	ItemRepository* repository = createRepository();

	assert(OUT_OF_RANGE == redo(repository));

	freeRepository(repository);
}