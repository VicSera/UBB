#pragma once

#include "ItemRepository.h"
#include <stdio.h>
#include <assert.h>

void runRepositoryTests();

void addItem_uniqueId_addOk();

void addItem_duplicateId_addFail();

void removeItem_existingId_removeOk();

void removeItem_idNotFound_removeFail();

void updateItem_existingId_updateOk();

void updateItem_idNotFound_updateFail();

void undo_addItem_lengthReverts();

void undo_withoutChanges_undoFail();

void redo_addItem_lengthReverts();

void redo_withoutChanges_redoFail();