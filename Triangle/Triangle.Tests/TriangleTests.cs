using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Triangle.Tests
{
    /// <summary>
    /// Summary description for UnitTest1
    /// </summary>
    [TestClass]
    public class TriangleTests
    {
        #region CountArea
        [TestMethod]
        public void CountAreaTest1()
        {
            Assert.AreEqual(new Core.Triangle(3, 4, 5).Area, 6, 0);
        }
        [TestMethod]
        public void CountAreaTest2()
        {
            Assert.AreEqual(new Core.Triangle(5, 4, 3).Area, 6, 0);
        }
        [TestMethod]
        public void CountAreaTest3()
        {
            Assert.AreEqual(new Core.Triangle(4, 5, 3).Area, 6, 0);
        }

        [TestMethod]
        public void CountAreaTest4()
        {
            new Core.Triangle(4, 5, 6);
        }

        #region PerimeterTests
        [TestMethod]
        public void PerimeterTest1()
        {
            Assert.AreEqual(new Core.Triangle(3, 4, 5).Semiperimeter, 6, 0);
        }
        [TestMethod]
        public void PerimeterTest2()
        {
            Assert.AreNotEqual(12, new Core.Triangle(3, 8, 5).Semiperimeter);
        }
        #endregion
        #endregion
    }
}
