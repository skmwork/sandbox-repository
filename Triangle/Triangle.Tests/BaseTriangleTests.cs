using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Triangle.Tests
{
    /// <summary>
    /// Summary description for TriangleBase
    /// </summary>
    [TestClass]
    public class BaseTriangleTests
    {
        #region NegativeParams
        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Отрицательный параметр неверно обработан")]
        public void NegativeParamsTest1()
        {
            new Core.Triangle(4, 5, -3);
        }
        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Отрицательный параметр неверно обработан")]
        public void NegativeParamsTest2()
        {
            new Core.Triangle(-4, -5, -3);
        }
        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Отрицательный параметр неверно обработан")]
        public void NegativeParamsTest3()
        {
            new Core.Triangle(4, -5, -3);
        }
        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Отрицательный параметр неверно обработан")]
        public void NegativeParamsTest4()
        {
            new Core.Triangle(-3, 2, 2);
        }
        #endregion

        #region BadParams
        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Сумма двух сторон должны быть больше третьей стороны")]
        public void ParamsAreNotTriangleTest()
        {
            new Core.Triangle(3, 1, 8);
        }
        #endregion

        #region ZeroParams
        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Параметр 0 неверно обработан")]
        public void ZeroParamsTest1()
        {
            new Core.Triangle(4, 5, 0);

        }
        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Параметр 0 неверно обработан")]
        public void ZeroParamsTest2()
        {
            new Core.Triangle(4, 2, 0);

        }
        [TestMethod]
        [ExpectedException(typeof(ArgumentException), "Параметр 0 неверно обработан")]
        public void ZeroParamsTest3()
        {
            new Core.Triangle(0, 2, 2);
        }
        #endregion


    }
}
