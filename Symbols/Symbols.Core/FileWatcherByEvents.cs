using System.IO;

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
