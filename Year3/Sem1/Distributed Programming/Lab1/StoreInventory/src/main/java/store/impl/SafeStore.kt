package store.impl

import entity.Product
import entity.Sale
import exception.InventoryException
import exception.MoneyException
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock

/**
 * Extension of [BaseStore] that uses a single mutex to wrap each read/write operation on the store data
 */
class SafeStore(
    inventory: Map<Product, Int>
) : BaseStore(inventory) {
    private val mutex = Mutex()

    override suspend fun registerSale(sale: Sale) {
        val profit = sale.product.unitPrice * sale.quantity

        mutex.withLock {
            val previousQuantity = inventory.getValue(sale.product)
            inventory[sale.product] = previousQuantity - sale.quantity
            money += profit
            registeredSales.add(sale)
        }
    }

    override suspend fun checkState() {
        var testMoney = 0f
        val testInventory = initialInventory.toMutableMap()

        mutex.withLock {
            registeredSales.forEach { sale ->
                testMoney += sale.product.unitPrice * sale.quantity
                testInventory[sale.product] = testInventory.getValue(sale.product) - sale.quantity
            }

            if (testMoney != money)
                throw MoneyException(money, testMoney)

            testInventory.forEach { (product, quantity) ->
                if (inventory.getValue(product) != quantity)
                    throw InventoryException(product, inventory.getValue(product), quantity)
            }
        }
    }
}
