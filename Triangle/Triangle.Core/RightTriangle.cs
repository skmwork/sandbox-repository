using System;

namespace Triangle.Core
{
    public class RightTriangle : Triangle
    {

        public RightTriangle(double a, double b, double c)
            : base(a, b, c)
        {
            if (!IsRightTriangle)
            {
                throw new ArgumentException("Треугольник не является прямоугольным");
            }
        }

        public override double Area
        {
            get
            {
                if (A > B && A > B)
                {
                    return CountArea(B, C);
                }
                if (B > C)
                {
                    return CountArea(A, C);
                }
                return CountArea(A, B);
            }
        }

        private double CountArea(double cat1, double cat2)
        {
            return 0.5 * cat1 * cat2;
        }
    }
}
