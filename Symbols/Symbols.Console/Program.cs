using System;
using System.Collections.Generic;
using System.Configuration;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NLog;
using NLog.Fluent;
using Symbols.Core;

namespace Symbols.Console
{
    class Program
    {
        private static Logger _logger = LogManager.GetCurrentClassLogger();
        static void Main(string[] args)
        {
            try
            {
                System.Console.WriteLine("Введите путь к папке");
                var inputDir = System.Console.ReadLine();
                var watcher = new FileWatcherByEvents(inputDir);
                System.Console.WriteLine("Производится отслеживание папки {0}", watcher.InputDir);
                watcher.StatisticsWasUpdated += s =>
                {
                    System.Console.Clear();
                    System.Console.WriteLine("Производится отслеживание папки {0}\r\nLastUpdate: {1}\r\n{2}", watcher.InputDir
                        , DateTime.Now.ToString("G")
                        , string.Join("\r\n", s.Select(x => x.Key + ":" + x.Value).ToArray()));
                    System.Console.WriteLine("Для выхода нажмите ESC");
                };
                watcher.Start();
                do
                {
                    while (!System.Console.KeyAvailable)
                    {
                    }
                } while (System.Console.ReadKey(true).Key != ConsoleKey.Escape);
                watcher.Stop();
            }
            catch (Exception e)
            {
                _logger.Error(e);
                System.Console.WriteLine("Для выхода введите любой символ");
                System.Console.Read();
            }

        }
    }
}
