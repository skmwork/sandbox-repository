using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NLog;

namespace Symbols.Core
{
    public class FileWatcherByEvents
    {
        public IFileProcessor Processor { get; private set; }
        private FileSystemWatcher _watcher;

        public FileWatcherByEvents(IFileProcessor processor)
        {
            Processor = processor;
            _watcher = new FileSystemWatcher(processor.InputDir) { EnableRaisingEvents = true };
        }

        public void Start()
        {
            _watcher.Created += (sender, args) => Processor.Process();
        }

    }
}
