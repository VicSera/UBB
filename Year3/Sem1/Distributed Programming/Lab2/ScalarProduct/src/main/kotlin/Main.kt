import kotlinx.coroutines.asCoroutineDispatcher
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import java.util.concurrent.Executors
import java.util.concurrent.locks.Condition
import java.util.concurrent.locks.ReentrantLock
import kotlin.concurrent.withLock

val mutex = ReentrantLock()
val condition: Condition = mutex.newCondition()

var lastProduct: Int? = null

fun main() {

    val vector1 = listOf(1, 2, 3, 4, 5)
    val vector2 = listOf(3, 5, 1, 4, 2)

    val dispatcher = Executors.newFixedThreadPool(2).asCoroutineDispatcher()

    runBlocking {
        launch(dispatcher) {
            producer(vector1, vector2)
        }
        launch(dispatcher) {
            consumer(vector1.size)
        }
    }

}

fun producer(vector1: List<Int>, vector2: List<Int>) {
    println("Started producer")
    vector1.zip(vector2).forEach {
        mutex.withLock {
            println("Producer got lock")
            while (lastProduct != null)
                condition.await()

            println("Producer computed ${it.first} x ${it.second} = ${it.first * it.second}")
            lastProduct = it.first * it.second

            condition.signalAll()
            println("Producer released lock")
        }
    }
}

fun consumer(count: Int) {
    println("Started consumer")
    var sum = 0
    repeat(count) {
        mutex.withLock {
            println("Consumer got lock")
            while (lastProduct == null)
                condition.await()

            println("Consumer added ${lastProduct}. New sum is ${sum + lastProduct!!}")
            sum += lastProduct!!
            lastProduct = null

            condition.signalAll()
            println("Consumer released lock")
        }
    }

    println(sum)
}
