using System.Collections.Generic;
using System.Linq;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Symbols.Core;

namespace Symbols.Tests
{
    [TestClass]
    public class CharStatsTest
    {

        [TestMethod]
        public void GetStatisticTest()
        {
            var stats = new SymbolStatistics();
            stats.AddStatistic("hello world");
            Assert.AreEqual(stats.Statistics.Count, 8);
            Assert.AreEqual(stats.Top5Symbols.Count, 5);
            Assert.IsTrue(stats.Statistics.SequenceEqual(new Dictionary<char, int>() { { 'h', 1 }, { 'e', 1 }, { 'l', 3 }, { 'o', 2 }, { ' ', 1 }, { 'w', 1 }, { 'r', 1 }, { 'd', 1 } }));
            Assert.IsTrue(stats.Top5Symbols.SequenceEqual(new Dictionary<char, int>() { { 'l', 3 }, { 'o', 2 }, { ' ', 1 }, { 'd', 1 }, { 'e', 1 } }));
        }
    }
}
