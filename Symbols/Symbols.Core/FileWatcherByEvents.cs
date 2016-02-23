using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace Symbols.Core
{
    public class FileWatcherByEvents
    {
        private readonly FileSystemWatcher _watcher;

        public int FilesInStatistics { get; private set; }

        public string InputDir { get; private set; }

        private readonly SymbolStatistics _stats;

        public event Action<Dictionary<char, int>> StatisticsWasUpdated;

        public FileWatcherByEvents(string inDir)
        {
            if (string.IsNullOrEmpty(inDir))
            {
                throw new ArgumentException("Путь к папке с файлами не задан");
            }
            InputDir = Path.GetFullPath(inDir);
            if (!Directory.Exists(InputDir))
            {
                Directory.CreateDirectory(InputDir);
            }
            _stats = new SymbolStatistics();
            _watcher = new FileSystemWatcher(InputDir) { EnableRaisingEvents = true };
        }

        public void Start()
        {
            Directory.GetFiles(InputDir, "*.txt").Select(x=>File.ReadAllText(x,Encoding.UTF8)).ToList().ForEach(_stats.AddStatistic);
            OnStatisticsWasUpdated();           
            _watcher.Created += WatcherOnCreated;
        }

        private void WatcherOnCreated(object sender, FileSystemEventArgs fileSystemEventArgs)
        {
            if (Path.GetExtension(fileSystemEventArgs.Name) != ".txt")
            {
                return;
            }
            FilesInStatistics = _stats.Md5List.Count;
            _stats.AddStatistic(File.ReadAllText(fileSystemEventArgs.FullPath, Encoding.UTF8));
            if (FilesInStatistics != _stats.Md5List.Count)
            {
                OnStatisticsWasUpdated();
            }
        }

        private void OnStatisticsWasUpdated()
        {
            var result = _stats.Top5Symbols;
            if (StatisticsWasUpdated != null)
            {
                StatisticsWasUpdated(result);
            }
            FilesInStatistics = _stats.Md5List.Count;
        }

        public void Stop()
        {
            _watcher.Created -= WatcherOnCreated;
        }
    }
}
