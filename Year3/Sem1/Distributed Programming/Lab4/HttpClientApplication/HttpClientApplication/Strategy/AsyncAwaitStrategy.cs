using System;
using System.Linq;
using System.Threading.Tasks;

namespace HttpClientApplication.Strategy
{
    public class AsyncAwaitStrategy: IRequestStrategy
    {
        public void PerformRequests(string[] urls)
        {
            var tasks = urls.Select(url => Task.Run(() => CreateTask(url)));

            Task.WhenAll(tasks).Wait();
        }

        private static async Task CreateTask(string url)
        {
            var client = new TaskHttpClient(url);

            await client.Connect();
            await client.Get();
            var response = await client.Receive();
            
            Console.WriteLine($"Request to {url} got: {response}");
            
            client.Dispose();
        }

        public override string ToString()
        {
            return "Async-Await Strategy";
        }
    }
}