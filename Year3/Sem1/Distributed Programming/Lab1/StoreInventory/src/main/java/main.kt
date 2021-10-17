import exception.CheckStateException
import kotlinx.coroutines.*
import store.StoreType
import store.Stores
import util.MockDataUtil

fun main() {
    val products = MockDataUtil.generateProducts(500)
    val inventory = MockDataUtil.generateInventory(products, 150, 300)
    val sales = MockDataUtil.generateSales(inventory)

    val store = Stores.new(StoreType.UNSAFE, inventory)

    runBlocking {
        withContext(Dispatchers.Default) {
            coroutineScope {
                sales.forEach {
                    launch {
                        store.registerSale(it)
                        try {
                            store.checkState()
                        } catch (exception: CheckStateException) {
                            println(exception.toString())
                        }
                    }
                }
            }
        }
    }

}


