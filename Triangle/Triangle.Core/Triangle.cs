using System;
using System.Collections.Generic;
using System.Linq;

namespace Triangle.Core
{
    public class Triangle
    {

        public double A { get; private set; }

        public double B { get; private set; }

        public double C { get; private set; }

        
        public Triangle(double a, double b, double c)
        {
            var exceptionMessages = new Dictionary<string, double>();
            if (a <= 0)
            {
                exceptionMessages.Add("a", a);
            }
            if (b <= 0)
            {
                exceptionMessages.Add("b", b);
            }
            if (c <= 0)
            {
                exceptionMessages.Add("c", c);
            }

            if (exceptionMessages.Any())
            {
                throw new ArgumentException("Стороны должны быть больше 0 (" + string.Join(", ", exceptionMessages.Select(x => x.Key + " : " + x.Value)) + ")");
            }
            if (a + b < c || a + c < b || b + c < a)
            {
                throw new ArgumentException(string.Format("Cумма двух сторон треугольника должна быть больше третьей стороны"));
            }
            A = a;
            B = b;
            C = c;
            Semiperimeter = (A + B + C) / 2;
        }

        public bool IsRightTriangle
        {
            get
            {
                if (A > B && A > B)
                {
                    return CheckRightTriangle(A, B, C);
                }
                if (B > C)
                {
                    return CheckRightTriangle(B, A, C);
                }
                if (C > B)
                {
                    return CheckRightTriangle(C, A, B);
                }
                return false;
            }
        }

        private bool CheckRightTriangle(double hyp, double cat1, double cat2)
        {
            return Math.Abs(Math.Pow(hyp, 2) - (Math.Pow(cat1, 2) + Math.Pow(cat2, 2))) < 0.000000000001;
        }

        public double Semiperimeter { get; private set; }

        public virtual double Area
        {
            get { return Math.Pow(Semiperimeter * (Semiperimeter - A) * (Semiperimeter - B) * (Semiperimeter - C), 0.5); }
        }
    }
}
