package store

import entity.Product
import entity.Sale
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock

/**
 * Implementation of [AbstractStore] that uses a single mutex to wrap each operation
 */
class DumbSafeStore(
    inventory: Map<Product, Int>
) : AbstractStore(inventory) {
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
