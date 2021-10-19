package store.impl

import entity.Product
import entity.Sale
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock

/**
 * Extension of [BaseStore] that uses a single mutex to wrap each operation
 */
class DumbSafeStore(
    inventory: Map<Product, Int>
) : BaseStore(inventory) {
    private val mutex = Mutex()

    override suspend fun registerSale(sale: Sale) {
        mutex.withLock {
            super.registerSale(sale)
        }
    }

    override suspend fun checkState() {
        mutex.withLock {
            super.checkState()
        }
    }
}
