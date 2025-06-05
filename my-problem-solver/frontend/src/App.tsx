// frontend/src/App.tsx
import { useState, type FormEvent } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';         // Import remark-math
import rehypeKatex from 'rehype-katex';       // Import rehype-katex

import 'katex/dist/katex.min.css';          // Import KaTeX CSS
import './App.css';

interface RetrievedDocument {
  filename: string;
  content: string; // Markdown content
}

interface DocumentResponse {
  documents: RetrievedDocument[];
}

interface HistoryItem {
  id: string;
  query: string;
  documents: RetrievedDocument[]; // Update this to use RetrievedDocument
  timestamp: Date;
}


// Helper function to extract title from Markdown (simple version)
// const extractMarkdownTitle = (markdown: string): string => {
//   if (!markdown) return "Untitled Document";
//   const match = markdown.match(/^\s*#{1,2}\s+(.*)/m);
//   if (match && match[1]) {
//     return match[1].trim();
//   }
//   return markdown.substring(0, 50).split('\n')[0] + (markdown.length > 50 ? '...' : '');
// };

function App() {
  const [problem, setProblem] = useState<string>('');
  const [documents, setDocuments] = useState<RetrievedDocument[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [hasSearched, setHasSearched] = useState<boolean>(false);
  const [selectedDocumentIndex, setSelectedDocumentIndex] = useState<number | null>(null);
  const [queryHistory, setQueryHistory] = useState<HistoryItem[]>([]); // New state for history

  // New state for related problems
  const [relatedProblems, setRelatedProblems] = useState<RetrievedDocument[]>([]);
  const [isLoadingRelatedProblems, setIsLoadingRelatedProblems] = useState<boolean>(false);
  const [selectedRelatedProblemIndex, setSelectedRelatedProblemIndex] = useState<number | null>(null);
  const [relatedProblemsError, setRelatedProblemsError] = useState<string | null>(null);



  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const currentProblemQuery = problem.trim();

    if (!currentProblemQuery) {
      setError('Please enter a problem.');
      setDocuments([]);
      setHasSearched(false);
      setSelectedDocumentIndex(null);
      return;
    }

    setIsLoading(true);
    setError(null);
    setDocuments([]);
    setSelectedDocumentIndex(null);

    // Also reset related problems on new search
    setRelatedProblems([]);
    setSelectedRelatedProblemIndex(null);
    setRelatedProblemsError(null);

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

      // After successfully fetching main documents, fetch similar problems
      // Don't await this if you want UI to update with main docs first,
      // then related problems load in. If they must load together, await it.
      // For a better UX, fetch them in parallel or sequentially without blocking UI too much.
      // For this example, sequential fetch:
      await fetchSimilarProblems(currentProblemQuery);

    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('An unknown error occurred.');
      }
      console.error("Failed to fetch documents:", err);
      setDocuments([]);
      setHasSearched(false);
    } finally {
      setIsLoading(false);
    }
  };

  const fetchSimilarProblems = async (problemQuery: string) => {
    setIsLoadingRelatedProblems(true);
    setRelatedProblemsError(null);
    setRelatedProblems([]); // Clear previous related problems
    setSelectedRelatedProblemIndex(null); // Clear selected related problem

    try {
      const response = await fetch('/api/similar-problems', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ problem: problemQuery }), // Assuming it takes the same 'problem' key
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
      }

      const data: DocumentResponse = await response.json();
      setRelatedProblems(data.documents);
    } catch (err) {
      if (err instanceof Error) {
        setRelatedProblemsError(err.message);
      } else {
        setRelatedProblemsError('An unknown error occurred while fetching related problems.');
      }
      console.error("Failed to fetch similar problems:", err);
    } finally {
      setIsLoadingRelatedProblems(false);
    }
  };


  const handleSelectDocument = (index: number) => {
    setSelectedDocumentIndex(index);
  };

  const handleReturnToList = () => {
    setSelectedDocumentIndex(null);
  };

  const handleHistoryItemClick = async (historyItem: HistoryItem) => {
    setProblem(historyItem.query); // Update the textarea with the historical query
    setDocuments(historyItem.documents);
    setSelectedDocumentIndex(null); // Reset to show document list
    setHasSearched(true); // Ensure split view is active
    setError(null); // Clear any previous errors
    // Optionally, scroll to top of document list or selected document if one was auto-selected

    // Reset and re-fetch related problems for the historical query
    setRelatedProblems([]);
    setSelectedRelatedProblemIndex(null);
    setRelatedProblemsError(null);
    if (historyItem.query) { // Ensure there's a query to fetch for
      await fetchSimilarProblems(historyItem.query);
    }

  };

    const handleSelectRelatedProblem = (index: number) => {
      setSelectedRelatedProblemIndex(index);
      // Optionally, if selecting a related problem should clear selection of main document:
      // setSelectedDocumentIndex(null);
    };

    const handleReturnToRelatedProblemList = () => {
      setSelectedRelatedProblemIndex(null);
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
        <div className="documents-section"> {/* This is the main right pane */}
          
          {/* Upper Part: Retrieved Documents */}
          <div className="retrieved-documents-pane">
            {isLoading && <p className="loading-message">Loading documents...</p>}
            {!isLoading && documents.length === 0 && !error && !isLoadingRelatedProblems && (
              <p>No documents found for your query.</p>
            )}
            {!isLoading && error && <p className="error-message">Error fetching documents: {error}</p>}

            {/* Document List View */}
            {!isLoading && !error && documents.length > 0 && selectedDocumentIndex === null && (
              <div className="document-list-container">
                <h2>Retrieved Documents</h2>
                <ul className="document-title-list">
                  {documents.map((doc, index) => (
                    <li key={`doc-${index}`} onClick={() => handleSelectDocument(index)}>
                      {doc.filename}
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {/* Selected Document View */}
            {!isLoading && !error && selectedDocumentIndex !== null && documents[selectedDocumentIndex] && (
              <div className="selected-item-view"> {/* Generic class for selected item */}
                <button onClick={handleReturnToList} className="return-button">
                  ← Back to Document List
                </button>
                <h3 className="selected-item-filename">{documents[selectedDocumentIndex].filename}</h3>
                <div className="document-content">
                  <ReactMarkdown remarkPlugins={[remarkGfm, remarkMath]} rehypePlugins={[rehypeKatex]}>
                    {documents[selectedDocumentIndex].content}
                  </ReactMarkdown>
                </div>
              </div>
            )}
          </div>

          {/* Divider (optional) */}
          {(!isLoading || !isLoadingRelatedProblems) && (documents.length > 0 || relatedProblems.length > 0) && <hr className="pane-divider" />}

          {/* Lower Part: Related Problems */}
          <div className="related-problems-pane">
            {isLoadingRelatedProblems && <p className="loading-message">Loading related problems...</p>}
            {!isLoadingRelatedProblems && relatedProblemsError && (
              <p className="error-message">Error fetching related problems: {relatedProblemsError}</p>
            )}
            {!isLoadingRelatedProblems && !relatedProblemsError && relatedProblems.length === 0 && !isLoading && documents.length > 0 && (
              <p>No related problems found.</p>
            )}

            {/* Related Problem List View */}
            {!isLoadingRelatedProblems && !relatedProblemsError && relatedProblems.length > 0 && selectedRelatedProblemIndex === null && (
              <div className="document-list-container"> {/* Re-use class or make specific */}
                <h2>Related Problems</h2>
                <ul className="document-title-list"> {/* Re-use class or make specific */}
                  {relatedProblems.map((rp, index) => (
                    <li key={`rp-${index}`} onClick={() => handleSelectRelatedProblem(index)}>
                      {rp.filename}
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {/* Selected Related Problem View */}
            {!isLoadingRelatedProblems && !relatedProblemsError && selectedRelatedProblemIndex !== null && relatedProblems[selectedRelatedProblemIndex] && (
              <div className="selected-item-view"> {/* Generic class for selected item */}
                <button onClick={handleReturnToRelatedProblemList} className="return-button">
                  ← Back to Related Problems List
                </button>
                <h3 className="selected-item-filename">{relatedProblems[selectedRelatedProblemIndex].filename}</h3>
                <div className="document-content">
                  <ReactMarkdown remarkPlugins={[remarkGfm, remarkMath]} rehypePlugins={[rehypeKatex]}>
                    {relatedProblems[selectedRelatedProblemIndex].content}
                  </ReactMarkdown>
                </div>
              </div>
            )}
          </div>
        </div>
      )}

    </div>
  );
}

export default App;