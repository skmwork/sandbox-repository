using System;
using System.Collections.Generic;
using System.Configuration;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NLog;
using Symbols.Core;

namespace Symbols.Console
{
    class Program
    {
        private static Logger logger = LogManager.GetCurrentClassLogger();
        static void Main(string[] args)
        {
            var inputDir = ConfigurationManager.AppSettings["InputDir"];         
            var outputPath = ConfigurationManager.AppSettings["OutputPath"];
            var watcher = new FileWatcherByEvents(new FileProcessor( inputDir, outputPath));
            watcher.Start();
            logger.Info("Для выхода нажмите ESC");
            do
            {
                while (!System.Console.KeyAvailable)
                {
                }
            } while (System.Console.ReadKey(true).Key != ConsoleKey.Escape);
        }
    }
}
