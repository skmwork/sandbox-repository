using System.Collections.Generic;
using System.Linq;

namespace Symbols.Core
{
    public class SymbolStatistics
    {
        public Dictionary<char, int> Statistics { get; private set; }

        public SymbolStatistics()
        {
            Statistics = new Dictionary<char, int>();
        }

        public void AddStatistic(string input)
        {         
            input.ToCharArray().ToList().ForEach(x =>
            {
                if (!Statistics.ContainsKey(x))
                {
                    Statistics.Add(x, 1);
                    return;
                }
                Statistics[x] += 1;
            });
        }

        public Dictionary<char, int> Top5Symbols
        {
            get { return Statistics.OrderByDescending(x => x.Value).ThenBy(v => v.Key).Take(5).ToDictionary(x => x.Key, v => v.Value); }
        }

    }
}
