package store

import entity.Product

class Stores {
    companion object {
        fun new(storeType: StoreType, inventory: Map<Product, Int>): Store {
            return when(storeType) {
                StoreType.UNSAFE -> UnsafeStore(inventory)
                StoreType.DUMB_SAFE -> DumbSafeStore(inventory)
                StoreType.SMART_SAFE -> throw NotImplementedError("Smart safe store not implemented")
            }
        }
    }
}
