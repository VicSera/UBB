using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using HttpClientApplication.Strategy;

namespace HttpClientApplication
{
    internal static class Program
    {
        public static void Main(string[] args)
        {
            var urls = new []
            {
                "www.cs.ubbcluj.ro/~rlupsa/edu/pdp/progs/srv-begin-end.cs",
                "www.cs.ubbcluj.ro/~rlupsa/edu/pdp/progs/srv-task.cs",
                "www.cs.ubbcluj.ro/~ilazar/",
                "www.cs.ubbcluj.ro/~ilazar/ma/"
            };
            
            BenchmarkStrategy(new CallbackStrategy(), urls);
            BenchmarkStrategy(new TaskStrategy(), urls);
            BenchmarkStrategy(new AsyncAwaitStrategy(), urls);
        }

        private static void BenchmarkStrategy(IRequestStrategy strategy, string[] urls)
        {
            var startTime = DateTime.Now;
            
            strategy.PerformRequests(urls);

            var endTime = DateTime.Now;
            var duration = endTime - startTime;
            
            Console.WriteLine($"{strategy} took {duration.TotalMilliseconds} milliseconds to complete");
        }
    }
}