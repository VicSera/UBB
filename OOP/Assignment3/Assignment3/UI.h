#pragma once
#define _CRT_SECURE_NO_WARNINGS

#include "ItemService.h"
#include <stdio.h>
#include <crtdbg.h>

typedef struct _UI
{
	ItemService* itemService;
} UI;

typedef void(*commandHandler)(UI*, char**, unsigned int);

commandHandler getCommandHandler(char* command);

UI* createUI(ItemService* itemService);

void freeAllMemory(UI* ui);

void launch(UI* ui);

void parseCommand(UI* ui, char* command);

void print(Vector* itemVector);

void handleDisplay(UI* ui, char** arguments, unsigned int argumentCount);

void handleAdd(UI* ui, char** arguments, unsigned int argumentCount);

void handleRemove(UI* ui, char** arguments, unsigned int argumentCount);

void handleUpdate(UI* ui, char** arguments, unsigned int argumentCount);

void handleUndo(UI* ui, char** arguments, unsigned int argumentCount);

void handleRedo(UI* ui, char** arguments, unsigned int argumentCount);