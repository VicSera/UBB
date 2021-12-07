using System;

namespace HttpClientApplication.Strategy
{
    public class CallbackStrategy: IRequestStrategy
    {
        public void PerformRequests(string[] urls)
        {
            var countdown = urls.Length;
            foreach (var url in urls)
            {
                var client = new HttpClient(url);
                client.Connect(() => client.Get(() => client.Receive(response =>
                {
                    Console.WriteLine($"Request to {url} got: {response}");
                    client.Dispose();
                    --countdown;
                })));
            }
            
            while (countdown != 0) {}
        }

        public override string ToString()
        {
            return "Callback Strategy";
        }
    }
}