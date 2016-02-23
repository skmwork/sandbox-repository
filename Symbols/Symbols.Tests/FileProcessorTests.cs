using System;
using System.IO;
using System.Linq;
using System.Text;
using System.Collections.Generic;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Symbols.Core;

namespace Symbols.Tests
{
    /// <summary>
    /// Summary description for FileProcessorTests
    /// </summary>
    [TestClass]
    public class FileProcessorTests
    {
        [TestMethod]
        public void UniqueFilesTest()
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

            IFileProcessor processor = new FileProcessor(inputDir, outputPath);
            File.WriteAllText(Path.Combine(inputDir, "hello.txt"), "hello world");
            File.WriteAllText(Path.Combine(inputDir, "hello2.txt"), "hello world");
            File.WriteAllText(Path.Combine(inputDir, "repeata.txt"), "aaaaaaaaaaaaaaaaaaaaaaa");
            File.WriteAllText(Path.Combine(inputDir, "repeata2.txt"), "aaaaaaaaaaaaaaaaaaaaaaa");
            File.WriteAllText(Path.Combine(inputDir, "empty.txt"), "");
            processor.Process();
            var result = File.ReadAllText(outputPath);
            Assert.IsTrue(result.Contains(
                "a:23\r\nl:3\r\no:2\r\n :1\r\nd:1"));
            Assert.AreEqual(processor.FileOriginalCount, 2);
            Assert.AreEqual(processor.FilesCount, 5);
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Параметр null неверно обработан")]
        public void NullParamsTest1()
        {
            new FileProcessor(null, "adwadwd");
        }
        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Параметр null неверно обработан")]
        public void NullParamsTest2()
        {
            new FileProcessor("awdadw", null);
        }
    }
}
