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
        public void FilesTest1()
        {
            const string inputDir = @"in";
            const string outputPath = @"out\res.txt";

            var watcher = new FileWatcherByEvents(inputDir, outputPath);
            if (Directory.Exists(watcher.InputDir))
            {
                Directory.GetFiles(watcher.InputDir).ToList().ForEach(File.Delete);
            }
            if (File.Exists(watcher.OutputPath))
            {
                File.Delete(watcher.OutputPath);
            }
            File.WriteAllText(Path.Combine(inputDir, "hello.txt"), "hello world");
            File.WriteAllText(Path.Combine(inputDir, "hello2.txt"), "hello world");
            File.WriteAllText(Path.Combine(inputDir, "hello2.scv"), "there are chars");
            File.WriteAllText(Path.Combine(inputDir, "repeata.txt"), "aaaaaaaaaaaaaaaaaaaaaaa");
            File.WriteAllText(Path.Combine(inputDir, "repeata2.txt"), "aaaaaaaaaaaaaaaaaaaaaaa");
            File.WriteAllText(Path.Combine(inputDir, "empty.txt"), string.Empty);
            File.WriteAllText(Path.Combine(inputDir, "b.txt"), "b");
            watcher.Start();
            Assert.AreEqual(watcher.FilesInStatistics,3);
            var result = File.ReadAllText(watcher.OutputPath);
            Assert.IsTrue(result.Contains(
                "a:23\r\nl:3\r\no:2\r\n :1\r\nb:1"));
        }

        [TestMethod]
        public void FilesTest2()
        {
            const string inputDir = @"in";
            const string outputPath = @"out\res.txt";

            var watcher = new FileWatcherByEvents(inputDir, outputPath);
            if (Directory.Exists(watcher.InputDir))
            {
                Directory.GetFiles(watcher.InputDir).ToList().ForEach(File.Delete);
            }
            if (File.Exists(watcher.OutputPath))
            {
                File.Delete(watcher.OutputPath);
            }

            watcher.Start();
            File.WriteAllText(Path.Combine(inputDir, "hello.txt"), "hello world");
            File.WriteAllText(Path.Combine(inputDir, "hello2.txt"), "hello world");
            File.WriteAllText(Path.Combine(inputDir, "repeata.txt"), "aaaaaaaaaaaaaaaaaaaaaaa");
            File.WriteAllText(Path.Combine(inputDir, "repeata2.txt"), "aaaaaaaaaaaaaaaaaaaaaaa");
            File.WriteAllText(Path.Combine(inputDir, "empty.txt"), string.Empty);
             File.WriteAllText(Path.Combine(inputDir, "b.txt"), "b");
             File.WriteAllText(Path.Combine(inputDir, "hello2.scv"), "there are chars");
            while (watcher.FilesInStatistics < 3)
            {
            }
            Assert.AreEqual(watcher.FilesInStatistics, 3);
            var result = File.ReadAllText(watcher.OutputPath);
            Assert.IsTrue(result.Contains(
                "a:23\r\nl:3\r\no:2\r\n :1\r\nb:1"));
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Параметр null неверно обработан")]
        public void NullParamsTest1()
        {
            new FileWatcherByEvents(null, "adwadwd");
        }
        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Параметр null неверно обработан")]
        public void NullParamsTest2()
        {
            new FileWatcherByEvents("awdadw", null);
        }
        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Параметр null неверно обработан")]
        public void EmptyParamsTest1()
        {
            new FileWatcherByEvents(string.Empty, "adwadwd");
        }
        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Параметр null неверно обработан")]
        public void EmptyParamsTest2()
        {
            new FileWatcherByEvents("awdadw", string.Empty);
        }

    }
}
