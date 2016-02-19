using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Triangle.Core;

namespace Triangle.Tests
{
    [TestClass]
    public class RigntTriangleTests
    {

        #region CountArea
        [TestMethod]
        public void RightTriangleCountAreaTest1()
        {
            Assert.AreEqual(new RightTriangle(3, 4, 5).Area, 6, 0);
        }
        [TestMethod]
        public void RightTriangleCountAreaTest2()
        {
            Assert.AreEqual(new RightTriangle(5, 4, 3).Area, 6, 0);
        }
        [TestMethod]
        public void RightTriangleCountAreaTest3()
        {
            Assert.AreEqual(new RightTriangle(4, 5, 3).Area, 6, 0);
        }
        #endregion

        #region ParamsAreNotRightTriangle
        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Случай не прямоугольного треугольника неверно обработан")]
        public void ParamsAreNotRightTriangleTest1()
        {
            new RightTriangle(4, 5, 8);
        }
        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Случай не прямоугольного треугольника неверно обработан")]
        public void ParamsAreNotRightTriangleTest2()
        {
            new RightTriangle(5, 5, 5);
        }
        #endregion
    }
}
