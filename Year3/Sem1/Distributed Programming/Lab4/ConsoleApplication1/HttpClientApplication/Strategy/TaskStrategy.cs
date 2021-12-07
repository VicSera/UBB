using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Threading.Tasks;

namespace HttpClientApplication.Strategy
{
    public class TaskStrategy: IRequestStrategy
    {
        public void PerformRequests(string[] urls)
        {
            var tasks = urls.Select(CreateTask);

            Task.WhenAll(tasks).Wait();
        }

        private static Task CreateTask(string url)
        {
            var client = new TaskHttpClient(url);

            client.Connect().Wait();
            client.Get().Wait();
            var response = client.Receive().Result;
            
            Console.WriteLine($"Request to {url} got: {response}");
            client.Dispose();
            
            return Task.CompletedTask;
        }

        public override string ToString()
        {
            return "Task Strategy";
        }
    }
}