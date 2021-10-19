import exception.CheckStateException
import kotlinx.coroutines.*
import store.StoreType
import store.Stores
import util.MockDataUtil
import java.util.concurrent.Executors
import kotlin.system.measureTimeMillis

fun main() {
    val storeTypes = listOf(StoreType.MUTEX_WRAPS_EVERYTHING, StoreType.MUTEX_WHEN_NECESSARY)
    val threadCounts = listOf(5, 20, 50)
    storeTypes.forEach { storeType ->
        threadCounts.forEach { threadCount ->
            val duration = benchmark(threadCount, storeType)
            println("$storeType with $threadCount threads finished in $duration milliseconds")
        }
    }
}

fun benchmark(numberOfThreads: Int, storeType: StoreType): Long {
    val products = MockDataUtil.generateProducts(200)
    val inventory = MockDataUtil.generateInventory(products, 200, 400)
    val sales = MockDataUtil.generateSales(inventory)

    val store = Stores.new(storeType, inventory)
    val dispatcher = Executors.newFixedThreadPool(numberOfThreads).asCoroutineDispatcher()

    return measureTimeMillis {
        runBlocking {
//            withContext(dispatcher) {
//                coroutineScope {
                    sales.forEach {
                        launch(dispatcher) {
                            store.registerSale(it)
                            try {
                                store.checkState()
                            } catch (exception: CheckStateException) {
                                println(exception.toString())
                            }
                        }
//                    }
//                }
            }
        }
    }
}


