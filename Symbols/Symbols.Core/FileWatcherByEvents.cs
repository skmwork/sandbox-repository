using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Symbols.Core
{
    public class FileWatcherByEvents
    {
        private readonly FileSystemWatcher _watcher;

        public int FilesInStatistics { get; private set; }

        public string OutputPath { get; private set; }

        public string OutputDir { get; private set; }

        public string InputDir { get; private set; }

        private readonly SymbolStatistics _stats;

        public FileWatcherByEvents(string inDir, string outPath)
        {
            if (string.IsNullOrEmpty(inDir))
            {
                throw new ArgumentException("Путь к папке с файлами не задан");
            }
            if (string.IsNullOrEmpty(outPath))
            {
                throw new ArgumentException("Путь к файлу с результатом не задан");
            }
            InputDir = Path.GetFullPath(inDir);
            if (!Directory.Exists(InputDir))
            {
                Directory.CreateDirectory(InputDir);
            }
            OutputPath = Path.GetFullPath(outPath);
            OutputDir = Path.GetDirectoryName(OutputPath);
            if (OutputDir == null)
            {
                throw new ArgumentException("Путь к директории файла результатов задан неверно");
            }
            if (!Directory.Exists(OutputDir))
            {
                Directory.CreateDirectory(OutputDir);
            }
            _stats = new SymbolStatistics();
            _watcher = new FileSystemWatcher(InputDir) { EnableRaisingEvents = true };
        }

        public void Start()
        {
            Directory.GetFiles(InputDir, "*.txt").Select(File.ReadAllText).ToList().ForEach(_stats.AddStatistic);
            if (_stats.Md5List.Any())
            {
                WriteReport();
                FilesInStatistics = _stats.Md5List.Count;
            }
            _watcher.Created += WatcherOnCreated;
        }

        private void WatcherOnCreated(object sender, FileSystemEventArgs fileSystemEventArgs)
        {
            if (Path.GetExtension(fileSystemEventArgs.Name) != ".txt")
            {
                return;
            }
            FilesInStatistics = _stats.Md5List.Count;
            _stats.AddStatistic(File.ReadAllText(fileSystemEventArgs.FullPath));
            if (FilesInStatistics != _stats.Md5List.Count)
            {
                WriteReport();
                FilesInStatistics = _stats.Md5List.Count;
            }
        }

        public void Stop()
        {
            _watcher.Created -= WatcherOnCreated;
        }

        public void WriteReport()
        {
            var content = string.Format("LastUpdate: {0}\r\n{1}"
                , DateTime.Now.ToString("G")
                , string.Join("\r\n", _stats.Top5Symbols.Select(x => x.Key + ":" + x.Value).ToArray()));
            File.WriteAllText(OutputPath, content);
            FilesInStatistics = _stats.Md5List.Count;
        }
    }
}
