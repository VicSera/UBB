#pragma once

#include "Vector.h"
#include "Item.h"
#include <assert.h>

void createVector_empty_length0();

void copyVector_sameLength();

void copyVector_removeElement_changesNotShared();

void addElement_lengthChanged();

void removeElement_lengthChanged();

void removeElement_outOfBounds_exitCodeOutOfRange();

void runVectorTests();
