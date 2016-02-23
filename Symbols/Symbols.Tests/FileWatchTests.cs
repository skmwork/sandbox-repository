using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Symbols.Core;

namespace Symbols.Tests
{
    [TestClass]
    public class FileWatchTests
    {
        [TestMethod]
        public void FilesTest()
        {
            const string inputDir = @"in";
            const string outputPath = @"out\res.txt";
            if (Directory.Exists(inputDir))
            {
                Directory.GetFiles(inputDir).ToList().ForEach(File.Delete);
            }
            if (File.Exists(outputPath))
            {
                File.Delete(outputPath);
            }
            var processor = new FileProcessor(inputDir, outputPath);
            var watcher = new FileWatcherByEvents(processor);
            watcher.Start();
            File.WriteAllText(Path.Combine(inputDir, "hello.txt"),"hello world");
            File.WriteAllText(Path.Combine(inputDir, "hello2.txt"), "hello world");
            File.WriteAllText(Path.Combine(inputDir, "repeata.txt"), "aaaaaaaaaaaaaaaaaaaaaaa");
            File.WriteAllText(Path.Combine(inputDir, "repeata2.txt"), "aaaaaaaaaaaaaaaaaaaaaaa");
            while (processor.FilesCount != 4)
            {
            }
            var result = File.ReadAllText(outputPath);
            Assert.IsTrue(result.Contains(
                "a:23\r\nl:3\r\no:2\r\n :1\r\nd:1"));
        }

    }
}
