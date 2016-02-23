using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using NLog;

namespace Symbols.Core
{

    public class FileProcessor : IFileProcessor
    {

        private static Logger logger = LogManager.GetCurrentClassLogger();
        private SymbolStatistics _stats;

        public string OutputPath { get; private set; }

        public string OutputDir { get; private set; }

        public string InputDir { get; private set; }

        public int FilesCount { get; private set; }

        public int FileOriginalCount
        {
            get { return _stats.Md5List.Count; }
        }

        public FileProcessor(string inDir, string outPath)
        {
            _watchedFileNames = new List<string>();
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
        }

        private List<string> _watchedFileNames; 

        public void Process()
        {
            try
            {
                
                var files = Directory.GetFiles(InputDir, "*.txt").Where(x=>!_watchedFileNames.Contains(x));

                    files.Select(File.ReadAllText)
                    .ToList()
                    .ForEach(_stats.AddStatistic);
                File.WriteAllText(OutputPath, string.Format("LastUpdate: {0}\r\n{1}"
                    , DateTime.Now.ToString("G")
                    , string.Join("\r\n", _stats.Top5Symbols.Select(x => x.Key + ":" + x.Value).ToArray())));

                FilesCount = files.Count();
            }
            catch (Exception e)
            {
                logger.Error(e);
            }
        }


    }
}
