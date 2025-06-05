// frontend/src/App.tsx
import React, { useState, type FormEvent } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';         // Import remark-math
import rehypeKatex from 'rehype-katex';       // Import rehype-katex

import 'katex/dist/katex.min.css';          // Import KaTeX CSS
import './App.css';

interface DocumentResponse {
  documents: string[];
}

interface HistoryItem {
  id: string; // Unique ID for key prop and easier management
  query: string;
  documents: string[];
  timestamp: Date;
}


// Helper function to extract title from Markdown (simple version)
const extractMarkdownTitle = (markdown: string): string => {
  if (!markdown) return "Untitled Document";
  const match = markdown.match(/^\s*#{1,2}\s+(.*)/m);
  if (match && match[1]) {
    return match[1].trim();
  }
  return markdown.substring(0, 50).split('\n')[0] + (markdown.length > 50 ? '...' : '');
};

function App() {
  const [problem, setProblem] = useState<string>('');
  const [documents, setDocuments] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [hasSearched, setHasSearched] = useState<boolean>(false);
  const [selectedDocumentIndex, setSelectedDocumentIndex] = useState<number | null>(null);
  const [queryHistory, setQueryHistory] = useState<HistoryItem[]>([]); // New state for history


  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const currentProblemQuery = problem.trim(); // Use a trimmed version for history

    if (!currentProblemQuery) {
      setError('Please enter a problem.');
      setDocuments([]);
      setHasSearched(false);
      setSelectedDocumentIndex(null);
      return;
    }

    setIsLoading(true);
    setError(null);
    setDocuments([]); // Clear current documents
    setSelectedDocumentIndex(null);

    try {
      const response = await fetch('/api/retrieve-documents', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ problem: currentProblemQuery }), // Send trimmed query
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
      }

      const data: DocumentResponse = await response.json();
      setDocuments(data.documents); // Set current documents for display
      setHasSearched(true);

      // Add to history
      const newHistoryItem: HistoryItem = {
        id: crypto.randomUUID(), // Generate a unique ID
        query: currentProblemQuery,
        documents: data.documents,
        timestamp: new Date(),
      };
      // Add to the beginning of the array so newest is on top
      setQueryHistory(prevHistory => [newHistoryItem, ...prevHistory.slice(0, 9)]); // Keep last 10 items
                                                                                  // Adjust slice(0, X) for max history items

    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('An unknown error occurred.');
      }
      console.error("Failed to fetch documents:", err);
      // Do not setHasSearched(false) here if you want to keep the layout,
      // but maybe clear documents or show an error in the document pane.
      // For now, let's keep it simple:
      setDocuments([]); // Clear documents on error
      setHasSearched(false); // Or true if you want to show error in right pane
    } finally {
      setIsLoading(false);
    }
  };

  const handleSelectDocument = (index: number) => {
    setSelectedDocumentIndex(index);
  };

  const handleReturnToList = () => {
    setSelectedDocumentIndex(null);
  };

  const handleHistoryItemClick = (historyItem: HistoryItem) => {
    setProblem(historyItem.query); // Update the textarea with the historical query
    setDocuments(historyItem.documents);
    setSelectedDocumentIndex(null); // Reset to show document list
    setHasSearched(true); // Ensure split view is active
    setError(null); // Clear any previous errors
    // Optionally, scroll to top of document list or selected document if one was auto-selected
  };


  const appContainerClass = `app-container ${hasSearched ? 'searched-layout' : 'initial-layout'}`;

  return (
    <div className={appContainerClass}>
      <div className="problem-section">
        <h1>Problem Document Retriever</h1>
        <form onSubmit={handleSubmit} className="problem-form">
          <textarea
            value={problem}
            onChange={(e) => setProblem(e.target.value)}
            placeholder="Enter your problem here..."
            rows={hasSearched ? 10 : 4}
            className="problem-input"
          />
          <button type="submit" disabled={isLoading} className="submit-button">
            {isLoading ? 'Retrieving...' : 'Retrieve Documents'}
          </button>
        </form>
        {error && <p className="error-message">Error: {error}</p>}
        {isLoading && !hasSearched && <p className="loading-message">Loading...</p>}
                {/* History Section - Placed within problem-section */}
        {queryHistory.length > 0 && (
          <div className="history-section">
            <h2>Query History</h2>
            <ul className="history-list">
              {queryHistory.map((item) => (
                <li
                  key={item.id}
                  onClick={() => handleHistoryItemClick(item)}
                  className="history-item"
                >
                  <span className="history-query-text">
                    {item.query.length > 60 ? `${item.query.substring(0, 60)}...` : item.query}
                  </span>
                  <span className="history-timestamp">
                    {item.timestamp.toLocaleTimeString()}
                  </span>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>

      {hasSearched && (
        <div className="documents-section">
          {isLoading && <p className="loading-message">Loading documents...</p>}
          
          {!isLoading && documents.length === 0 && !error && (
            <p>No documents found for your query.</p>
          )}

          {!isLoading && documents.length > 0 && selectedDocumentIndex === null && (
            <div className="document-list-container">
              <h2>Retrieved Documents:</h2>
              <ul className="document-title-list">
                {documents.map((doc, index) => (
                  <li key={index} onClick={() => handleSelectDocument(index)}>
                    {extractMarkdownTitle(doc)}
                  </li>
                ))}
              </ul>
            </div>
          )}

          {!isLoading && selectedDocumentIndex !== null && documents[selectedDocumentIndex] && (
            <div className="selected-document-view">
              <button onClick={handleReturnToList} className="return-button">
                ← Back to List
              </button>
              <div className="document-content">
                <ReactMarkdown
                  remarkPlugins={[remarkGfm, remarkMath]} // Add remarkMath
                  rehypePlugins={[rehypeKatex]}         // Add rehypeKatex
                >
                  {documents[selectedDocumentIndex]}
                </ReactMarkdown>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;