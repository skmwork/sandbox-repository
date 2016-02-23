using Symbols.Core;
using System;
using System.Linq;

namespace Symbols.Console
{
    class Program
    {
        static void Main()
        {
            try
            {
                System.Console.WriteLine("Введите путь к папке");
                var inputDir = System.Console.ReadLine();
                using (var watcher = new FileWatcherByEvents(inputDir))
                {
                    watcher.StatisticsWasUpdated += s =>
                    {
                        System.Console.Clear();
                        System.Console.WriteLine("Производится отслеживание папки {0}\r\nLastUpdate: {1}\r\n{2}",
                            watcher.InputDir
                            , DateTime.Now.ToString("G")
                            , string.Join("\r\n", s.Select(x => "'" + x.Key + "'  :   " + x.Value).ToArray()));
                        System.Console.WriteLine("Для выхода нажмите ESC");
                    };
                    watcher.Start();
                    WaitEsc();
                }
            }
            catch (Exception e)
            {
                System.Console.WriteLine(e);
                System.Console.WriteLine("Для выхода нажмите ESC");
                WaitEsc();            
            }

        }

        static void WaitEsc()
        {
            do
            {
                while (!System.Console.KeyAvailable)
                {
                }
            } while (System.Console.ReadKey(true).Key != ConsoleKey.Escape);
        }
    }
}
