namespace HttpClientApplication
{
    public interface IRequestStrategy
    {
        void PerformRequests(string[] urls);
    }
}