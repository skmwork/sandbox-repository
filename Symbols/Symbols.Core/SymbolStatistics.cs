using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using NLog;

namespace Symbols.Core
{
    internal class SymbolStatistics
    {

        public Dictionary<char, int> Statistics { get; private set; }
        private static Logger _logger = LogManager.GetCurrentClassLogger();

        internal SymbolStatistics()
        {
            Statistics = new Dictionary<char, int>();
            Md5List = new List<string>();
        }

        public void AddStatistic(string input)
        {
            if (string.IsNullOrEmpty(input))
            {
                return;
            }
            using (MD5 md5Hash = MD5.Create())
            {
                var md5 = GetMd5Hash(md5Hash, input);
                if (Md5List.Contains(md5))
                {
                    return;
                }
                Md5List.Add(md5);
            }
            input.ToCharArray().ToList().ForEach(x =>
            {
                if (!Statistics.ContainsKey(x))
                {
                    Statistics.Add(x, 1);
                    return;
                }
                Statistics[x] += 1;
            });
            _logger.Info("Статистика по оригинальному файлу обновлена");
            
        }

        public Dictionary<char, int> Top5Symbols
        {
            get { return Statistics.OrderByDescending(x => x.Value).ThenBy(v => v.Key).Take(5).ToDictionary(x => x.Key, v => v.Value); }
        }

        public List<string> Md5List { get; private set; }

        static string GetMd5Hash(MD5 md5Hash, string input)
        {

            // Convert the input string to a byte array and compute the hash.
            byte[] data = md5Hash.ComputeHash(Encoding.UTF8.GetBytes(input));

            // Create a new Stringbuilder to collect the bytes
            // and create a string.
            StringBuilder sBuilder = new StringBuilder();

            // Loop through each byte of the hashed data 
            // and format each one as a hexadecimal string.
            for (int i = 0; i < data.Length; i++)
            {
                sBuilder.Append(data[i].ToString("x2"));
            }

            // Return the hexadecimal string.
            return sBuilder.ToString();
        }

    }
}
