using System;
using System.Threading.Tasks;

namespace HttpClientApplication
{
    public class TaskHttpClient
    {
        private HttpClient _client;
        
        public TaskHttpClient(string url)
        {
            _client = new HttpClient(url);
        }

        public Task Connect() => Task.Run(() =>
        {
            var completion = new TaskCompletionSource<object>();

            _client.Connect(() => completion.TrySetResult(null));

            return completion.Task;
        });
        
        public Task Get() => Task.Run(() =>
        {
            var completion = new TaskCompletionSource<object>();

            _client.Get(() => completion.TrySetResult(null));

            return completion.Task;
        });
        
        public Task<string> Receive() => Task.Run(() =>
        {
            var completion = new TaskCompletionSource<string>();

            _client.Receive(result => completion.TrySetResult(result));

            return completion.Task;
        });

        public void Dispose() => _client.Dispose();
    }
}