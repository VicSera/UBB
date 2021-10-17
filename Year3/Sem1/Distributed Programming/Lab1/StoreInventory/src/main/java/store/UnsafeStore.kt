package store

import entity.Product

/**
 * Base implementation of [AbstractStore] that has no thread-safety whatsoever
 */
class UnsafeStore(
    inventory: Map<Product, Int>
) : AbstractStore(inventory)
