#include "ServiceTests.h"

void runServiceTests()
{
	serviceAddItem_uniqueId_addOk();
	serviceAddItem_existingId_addFail();
	serviceDeleteItem_existingId_deleteOk();
	serviceDeleteItem_idNotFound_deleteFail();
	serviceUpdateItem_existingId_updateOk();
	serviceUpdateItem_idNotFound_updateFail();
}

void serviceAddItem_uniqueId_addOk()
{
	ItemRepository* repository = createRepository();
	ItemService* service = createService(repository);

	assert(DONE == serviceAddItem(service, 1, "a", "a", 1));

	freeService(service);
}

void serviceAddItem_existingId_addFail()
{
	ItemRepository* repository = createRepository();
	ItemService* service = createService(repository);

	serviceAddItem(service, 1, "a", "a", 1);
	assert(ALREADY_EXISTS == serviceAddItem(service, 1, "b", "b", 2));

	freeService(service);
}

void serviceDeleteItem_existingId_deleteOk()
{
	ItemRepository* repository = createRepository();
	ItemService* service = createService(repository);

	serviceAddItem(service, 1, "a", "a", 1);
	assert(DONE == serviceDeleteItem(service, 1));

	freeService(service);
}

void serviceDeleteItem_idNotFound_deleteFail()
{
	ItemRepository* repository = createRepository();
	ItemService* service = createService(repository);

	assert(NOT_FOUND == serviceDeleteItem(service, 1));

	freeService(service);
}

void serviceUpdateItem_existingId_updateOk()
{
	ItemRepository* repository = createRepository();
	ItemService* service = createService(repository);

	serviceAddItem(service, 1, "a", "a", 1);
	assert(DONE == serviceUpdateItem(service, 1, "b", "b", 2));

	freeService(service);
}

void serviceUpdateItem_idNotFound_updateFail()
{
	ItemRepository* repository = createRepository();
	ItemService* service = createService(repository);

	assert(NOT_FOUND == serviceUpdateItem(service, 1, "b", "b", 2));

	freeService(service);
}