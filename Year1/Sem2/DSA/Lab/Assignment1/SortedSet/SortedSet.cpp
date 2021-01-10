#include "SortedSet.h"
#include "SortedSetIterator.h"

SortedSet::SortedSet(Relation r): relation(r) {
	capacity = 10;
    count = 0;
    elements = new TComp[capacity];
}


bool SortedSet::add(TComp elem) {
    // check element uniqueness
	if (search(elem))
	    return false;

	// check if maximum capacity was reached
	if (count == capacity)
    {
        // allocate twice the area
        capacity *= 2;
	    auto newElements = new TComp[capacity];
	    // copy the elements from the old location
	    for (int i = 0; i < count; ++i)
	        newElements[i] = elements[i];
	    // free the old location
	    delete[] elements;

	    // change the reference to the new location
	    elements = newElements;
    }

	for (int i = 0; i < count; ++i)
	    if (relation(elem, elements[i]))
        {
            // iterate the array backwards to free up the i'th position
            for (int j = count; j > i; --j)
                elements[j] = elements[j - 1];
            // place the element in the freed up spot
            elements[i] = elem;
            ++count;
            return true;
        }

	// if the relation didn't hold at any point, that means the element should be placed last
    elements[count++] = elem;
	return true;
}


bool SortedSet::remove(TComp elem) {
	for (int i = 0; i < count; ++i)
	    if (elements[i] == elem)
        {
	        // decrement element count
	        --count;
	        // move each element after the found element one spot to the left
	        for (; i < count; ++i)
	            elements[i] = elements[i + 1];
	        // notify the caller that the element was removed
	        return true;
        }
	// element wasn't found
	return false;
}


bool SortedSet::search(TComp elem) const {
	for (int i = 0; i < count; ++i)
        if (elements[i] == elem)
            return true;
	return false;
}


int SortedSet::size() const {
	return count;
}



bool SortedSet::isEmpty() const {
	return count == 0;
}

SortedSetIterator SortedSet::iterator() const {
	return SortedSetIterator(*this);
}


SortedSet::~SortedSet() {
	delete[] elements;
}


