using System.Text;
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
        static string _inputDir = Path.GetFullPath(@"in");
        [TestInitialize]
        public void SetUp()
        {
            if (Directory.Exists(_inputDir))
            {
                Directory.GetFiles(_inputDir).ToList().ForEach(File.Delete);
                Directory.Delete(_inputDir);
            }
        }
        [TestCleanup]
        public void CleanUp()
        {
            if (Directory.Exists(_inputDir))
            {
                Directory.GetFiles(_inputDir).ToList().ForEach(File.Delete);
                Directory.Delete(_inputDir);
            }
        }

        [TestMethod]
        public void ArchiveTest1()
        {
            var watcher = new FileWatcherByEvents(_inputDir);          
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeata.txt"), "aaaaaaaaaaaaaaaaaaaaaaa");
            File.WriteAllText(Path.Combine(watcher.InputDir, "hello.txt"), "hello world");
            File.WriteAllText(Path.Combine(watcher.InputDir, "hello2.txt"), "hello world");
            File.WriteAllText(Path.Combine(watcher.InputDir, "hello2.scv"), "there are chars");
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeata2.txt"), "aaaaaaaaaaaaaaaaaaaaaaa");
            File.WriteAllText(Path.Combine(watcher.InputDir, "empty.txt"), string.Empty);
            File.WriteAllText(Path.Combine(watcher.InputDir, "b.txt"), "b");
            var result = new Dictionary<char, int>();
            watcher.StatisticsWasUpdated += s =>
            {
                result = s;
            };
            watcher.Start();
            Wait(watcher,3);
            Assert.IsNotNull(result);
            Assert.IsTrue(result.SequenceEqual(new Dictionary<char, int> { { 'a', 23 }, { 'l', 3 }, { 'o', 2 }, { ' ', 1 }, { 'b', 1 } }));
        }


        [TestMethod]
        public void EventTest()
        {
            var watcher = new FileWatcherByEvents(_inputDir);
            var result = new Dictionary<char, int>();
            watcher.StatisticsWasUpdated += s =>
            {
                result = s;
            };
            watcher.Start();
            File.WriteAllText(Path.Combine(watcher.InputDir, "hello.txt"), "hello world");
            File.WriteAllText(Path.Combine(watcher.InputDir, "hello2.txt"), "hello world");
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeata.txt"), "");
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeata2.txt"), "aaaaaaaaaaaaaaaaaaaaaaa");
            File.WriteAllText(Path.Combine(watcher.InputDir, "empty.txt"), string.Empty);
            File.WriteAllText(Path.Combine(watcher.InputDir, "hello2.scv"), "there are chars");
            File.WriteAllText(Path.Combine(watcher.InputDir, "b.txt"), "b");
            Wait(watcher,3);
            Assert.IsNotNull(result);
            Assert.IsTrue(result.SequenceEqual(new Dictionary<char, int> { { 'a', 23 }, { 'l', 3 }, { 'o', 2 }, { ' ', 1 }, { 'b', 1 } }));
        }


        [TestMethod]
        public void RussianTest()
        {
            var watcher = new FileWatcherByEvents(_inputDir);
            var result = new Dictionary<char, int>();
            watcher.StatisticsWasUpdated += s =>
            {
                result = s;
            };
            watcher.Start();
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeat_а.txt"), "ааааа", Encoding.UTF8);
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeat_б.txt"), "бббб", Encoding.UTF8);
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeat_в.txt"), "ввв", Encoding.UTF8);
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeat_г.txt"), "гг", Encoding.UTF8);
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeat_д.txt"), "д", Encoding.UTF8);
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeat_а_2.txt"), "ааааа", Encoding.UTF8);
            Wait(watcher,5);
            Assert.IsNotNull(result);
            Assert.IsTrue(result.SequenceEqual(new Dictionary<char, int> { { 'а', 5 }, { 'б', 4 }, { 'в', 3 }, { 'г', 2 }, { 'д', 1 } }));
        }


        [TestMethod]
        public void EnglishTest()
        {
            var watcher = new FileWatcherByEvents(_inputDir);
            var result = new Dictionary<char, int>();
            watcher.StatisticsWasUpdated += s =>
            {
                result = s;
            };
            watcher.Start();
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeat_a.txt"), "aaaaaaaaaa", Encoding.UTF8);
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeat_b.txt"), "bbbbbbbb", Encoding.UTF8);
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeat_c.txt"), "cccccc", Encoding.UTF8);
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeat_d.txt"), "dddd", Encoding.UTF8);
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeat_e.txt"), "ee", Encoding.UTF8);
            File.WriteAllText(Path.Combine(watcher.InputDir, "repeat_a_2.txt"), "aaaaaaaaaa", Encoding.UTF8);
            Wait(watcher,5);
            Assert.IsNotNull(result);
            Assert.IsTrue(result.SequenceEqual(new Dictionary<char, int> { { 'a', 10 }, { 'b', 8 }, { 'c', 6 }, { 'd', 4 }, { 'e', 2 } }));
        }

        private static void Wait(FileWatcherByEvents watcher, int filesCount)
        {
            var start = DateTime.Now;
            while (watcher.FilesInStatistics < filesCount)
            {
                if (DateTime.Now - start > TimeSpan.FromSeconds(30))
                {
                    throw new TimeoutException();
                }
            }
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
