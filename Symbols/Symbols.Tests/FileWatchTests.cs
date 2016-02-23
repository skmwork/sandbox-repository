using Microsoft.VisualStudio.TestTools.UnitTesting;
using Symbols.Core;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Symbols.Tests
{
    [TestClass]
    public class FileWatchTests
    {
        [TestMethod]
        public void FilesTest1()
        {
            const string inputDir = @"in";
            var watcher = new FileWatcherByEvents(inputDir);
            if (Directory.Exists(watcher.InputDir))
            {
                Directory.GetFiles(watcher.InputDir).ToList().ForEach(File.Delete);
            }
            File.WriteAllText(Path.Combine(inputDir, "repeata.txt"), "aaaaaaaaaaaaaaaaaaaaaaa");
            File.WriteAllText(Path.Combine(inputDir, "hello.txt"), "hello world");
            File.WriteAllText(Path.Combine(inputDir, "hello2.txt"), "hello world");
            File.WriteAllText(Path.Combine(inputDir, "hello2.scv"), "there are chars");
            File.WriteAllText(Path.Combine(inputDir, "repeata2.txt"), "aaaaaaaaaaaaaaaaaaaaaaa");
            File.WriteAllText(Path.Combine(inputDir, "empty.txt"), string.Empty);
            File.WriteAllText(Path.Combine(inputDir, "b.txt"), "b");
            var result = new Dictionary<char, int>();
            watcher.StatisticsWasUpdated += s =>
            {
                result = s;
            };
            watcher.Start();
            var start = DateTime.Now;
            while (watcher.FilesInStatistics < 3)
            {
                if (DateTime.Now - start > TimeSpan.FromSeconds(30))
                {
                    throw new TimeoutException();
                }
            }
            Assert.IsNotNull(result);
            Assert.IsTrue(result.SequenceEqual(new Dictionary<char, int> { { 'a', 23 }, { 'l', 3 }, { 'o', 2 }, { ' ', 1 }, { 'b', 1 } }));
        }

        [TestMethod]
        public void FilesTest2()
        {
            const string inputDir = @"in";
            var watcher = new FileWatcherByEvents(inputDir);
            if (Directory.Exists(watcher.InputDir))
            {
                Directory.GetFiles(watcher.InputDir).ToList().ForEach(File.Delete);
            }
            var result = new Dictionary<char, int>();
            watcher.StatisticsWasUpdated += s =>
            {
                result = s;
            };
            watcher.Start();
            File.WriteAllText(Path.Combine(inputDir, "hello.txt"), "hello world");
            File.WriteAllText(Path.Combine(inputDir, "hello2.txt"), "hello world");
            File.WriteAllText(Path.Combine(inputDir, "repeata.txt"), "");
            File.WriteAllText(Path.Combine(inputDir, "repeata2.txt"), "aaaaaaaaaaaaaaaaaaaaaaa");
            File.WriteAllText(Path.Combine(inputDir, "empty.txt"), string.Empty);          
            File.WriteAllText(Path.Combine(inputDir, "hello2.scv"), "there are chars");
            File.WriteAllText(Path.Combine(inputDir, "b.txt"), "b");
            var start = DateTime.Now;
            while (watcher.FilesInStatistics < 3)
            {
                if (DateTime.Now - start > TimeSpan.FromSeconds(30))
                {
                    throw new TimeoutException();
                }
            }
            Assert.IsNotNull(result);
            Assert.IsTrue(result.SequenceEqual(new Dictionary<char, int> { { 'a', 23 }, { 'l', 3 }, { 'o', 2 }, { ' ', 1 }, { 'b', 1 } }));
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Параметр null неверно обработан")]
        public void NullParamsTest1()
        {
            new FileWatcherByEvents(null);
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Параметр null неверно обработан")]
        public void EmptyParamsTest1()
        {
            new FileWatcherByEvents(string.Empty);
        }
    }
}
