using System;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Text.RegularExpressions;

namespace HttpClientApplication
{
    public class HttpClient
    {
        private static int BUFFER_LIMIT = 10000;
        
        private EndPoint _server;
        private Socket _client;
        private string _host;
        private string _path;

        public bool Connected => _client.Connected;

        public HttpClient(string url)
        {
            var parts = url.Split('/');
            _host = parts[0];
            _path = string.Join("/", parts.Skip(1));
            
            _client = new Socket(SocketType.Stream, ProtocolType.Tcp);
            _server = new DnsEndPoint(_host, 80);
        }

        public void Connect(Action onConnected)
        {
            _client.BeginConnect(_server, result =>
            {
                _client.EndConnect(result);
                onConnected();
            }, _client);
        }

        public void Get(Action onRequested)
        {
            var request = Encoding.ASCII.GetBytes($"GET /{_path} HTTP/1.1\r\nHost: {_host}\r\nContent-length: 0\r\n\r\n");

            _client.BeginSend(request, 0, request.Length, SocketFlags.None, result =>
            {
                _client.EndSend(result);
                onRequested();
            }, _client);
        }

        public void Receive(Action<string> onReceived)
        {
            var buffer = new byte[BUFFER_LIMIT];

            _client.BeginReceive(buffer, 0, BUFFER_LIMIT, SocketFlags.None, result =>
            {
                _client.EndReceive(result);
                onReceived(ExtractContentLength(buffer));
            }, null);
        }

        public void Dispose()
        {
            _client.Shutdown(SocketShutdown.Both);
            _client.Close();
        }

        private static string ExtractContentLength(byte[] bytes)
        {
            var regex = new Regex("(Content-Length: [0-9]+)", RegexOptions.Compiled);
            
            var httpResponse = Encoding.ASCII.GetString(bytes);
            var match = regex.Match(httpResponse);

            return match.Value;
        }
    }
}