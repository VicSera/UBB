#include "SortedSetIterator.h"
#include <exception>

using namespace std;

SortedSetIterator::SortedSetIterator(const SortedSet& m) : set(m)
{
	currentIndex = 0;
}


void SortedSetIterator::first() {
	currentIndex = 0;
}


void SortedSetIterator::next() {
	if (!valid())
		throw exception();
	++currentIndex;
}


TElem SortedSetIterator::getCurrent()
{
	if (!valid())
		throw exception();
	return set.elements[currentIndex];
}

bool SortedSetIterator::valid() const {
	return currentIndex < set.count;
}

