package store

import entity.Product
import entity.Sale
import exception.InventoryException
import exception.MoneyException

abstract class AbstractStore(
    inventory: Map<Product, Int>
) : Store {
    var money = 0f
    protected val inventory = inventory.toMutableMap()
    protected val registeredSales: MutableList<Sale> = emptyList<Sale>().toMutableList()
    private val initialInventory: Map<Product, Int> = inventory.toMap()

    override suspend fun registerSale(sale: Sale) {
        val previousQuantity = inventory.getValue(sale.product)
        if (previousQuantity < sale.quantity)
            throw RuntimeException("Invalid sale registered.")

        inventory[sale.product] = previousQuantity - sale.quantity

        val profit = sale.product.unitPrice * sale.quantity
        money += profit

        registeredSales.add(sale)
    }

    override suspend fun checkState() {
        var testMoney = 0f
        val testInventory = initialInventory.toMutableMap()

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
