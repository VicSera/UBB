package store.impl

import entity.Product

/**
 * Base implementation of [BaseStore] that has no thread-safety whatsoever
 */
class UnsafeStore(
    inventory: Map<Product, Int>
) : BaseStore(inventory)
