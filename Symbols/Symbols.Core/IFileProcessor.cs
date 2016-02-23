namespace Symbols.Core
{
    public interface IFileProcessor
    {
        string OutputPath { get; }
        string OutputDir { get; }
        string InputDir { get; }
        int FilesCount { get; }
        int FileOriginalCount { get; }
    
        void Process();
    }
}