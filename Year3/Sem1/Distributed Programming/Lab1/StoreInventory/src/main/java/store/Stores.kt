package store

import entity.Product
import store.impl.DumbSafeStore
import store.impl.SafeStore
import store.impl.UnsafeStore

/**
 * Factory class for instantiating different implementations of [Store]
 */
class Stores {
    companion object {
        fun new(storeType: StoreType, inventory: Map<Product, Int>): Store {
            return when(storeType) {
                StoreType.UNSAFE -> UnsafeStore(inventory)
                StoreType.MUTEX_WRAPS_EVERYTHING -> DumbSafeStore(inventory)
                StoreType.MUTEX_WHEN_NECESSARY -> SafeStore(inventory)
            }
        }
    }
}
