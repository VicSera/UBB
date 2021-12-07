# Parallelized HTTP GET-Request sender
## Strategies (implement `IRequestStrategy` ([code](Strategy/IRequestStrategy.cs)))
* Callback-driven: `CallbackStrategy` ([code](Strategy/CallbackStrategy.cs))
    * uses simple `HttpClient`s that provide a Connect, Get and Receive method
    which accept callbacks for when the async call is finished.
    * example output:
        ```
        Request to www.cs.ubbcluj.ro/~rlupsa/edu/pdp/progs/srv-begin-end.cs got: Content-Length: 3593
        Request to www.cs.ubbcluj.ro/~rlupsa/edu/pdp/progs/srv-task.cs got: Content-Length: 4735
        Request to www.cs.ubbcluj.ro/~ilazar/ma/ got: Content-Length: 2461013
        Request to www.cs.ubbcluj.ro/~ilazar/ got: Content-Length: 1812749
        Callback Strategy took 81.36 milliseconds to complete
        ```
* Task-driven: `TaskStrategy` ([code](Strategy/TaskStrategy.cs))
    * uses `TaskHttpClient`s that wrap the Connect, Get and Receive methods 
    from `HttpClient` inside `Task`s. The Task API is used to wait for each task to finish.
    * example output:
        ```
        Request to www.cs.ubbcluj.ro/~rlupsa/edu/pdp/progs/srv-begin-end.cs got: Content-Length: 3593
        Request to www.cs.ubbcluj.ro/~rlupsa/edu/pdp/progs/srv-task.cs got: Content-Length: 4735
        Request to www.cs.ubbcluj.ro/~ilazar/ got: Content-Length: 1812749
        Request to www.cs.ubbcluj.ro/~ilazar/ma/ got: Content-Length: 2461013
        Task Strategy took 185.9109 milliseconds to complete
        ```
* Async-Await-driven: `AsyncAwaitStrategy` ([code](Strategy/AsyncAwaitStrategy.cs))
    * uses the same `TaskHttpClient` as `TaskStrategy`, but instead uses the built-in
    `async`/`await` mechanism from C#. 
    * example output:
        ```
        Request to www.cs.ubbcluj.ro/~ilazar/ma/ got: Content-Length: 2461013
        Request to www.cs.ubbcluj.ro/~rlupsa/edu/pdp/progs/srv-begin-end.cs got: Content-Length: 3593
        Request to www.cs.ubbcluj.ro/~rlupsa/edu/pdp/progs/srv-task.cs got: Content-Length: 4735
        Request to www.cs.ubbcluj.ro/~ilazar/ got: Content-Length: 1812749
        Async-Await Strategy took 48.8035 milliseconds to complete
        ```

## Hardware specifications:
* CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
* RAM: 64.0 GB