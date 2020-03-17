#pragma once

#include <assert.h>
#include "ItemService.h"

void runServiceTests();

void serviceAddItem_uniqueId_addOk();

void serviceAddItem_existingId_addFail();

void serviceDeleteItem_existingId_deleteOk();

void serviceDeleteItem_idNotFound_deleteFail();

void serviceUpdateItem_existingId_updateOk();

void serviceUpdateItem_idNotFound_updateFail();