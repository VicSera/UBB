using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(GradeApp.Startup))]
namespace GradeApp
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
