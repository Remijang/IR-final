// frontend/src/App.tsx
import { useState, type FormEvent, useEffect } from 'react';
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
  const [selectedImage, setSelectedImage] = useState<File | null>(null);
  const [imagePreviewUrl, setImagePreviewUrl] = useState<string | null>(null); // For image preview

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
    const currentProblemText = problem.trim();

    if (!problem.trim() && !selectedImage) {
      setError('Please enter a problem.');
      setDocuments([]);
      setHasSearched(false);
      setSelectedDocumentIndex(null);

      setRelatedProblems([]);
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

    let requestBody: BodyInit;
    let requestHeaders: HeadersInit = {};
    let endpoint: string;
    let effectiveQueryForHistory = currentProblemText;

    if (selectedImage) {
      // Image query (potentially with text) - use FormData
      const formData = new FormData();
      formData.append('image', selectedImage);
      formData.append('problem_text', currentProblemText); // Backend handles if it's empty

      requestBody = formData;
      // DO NOT set Content-Type for FormData, browser does it.
      endpoint = '/api/retrieve-documents-by-image';
      effectiveQueryForHistory = `Image: ${selectedImage.name}${currentProblemText ? ` + Text: ${currentProblemText}` : ''}`;
    } else {
      // Text-only query - use JSON
      requestBody = JSON.stringify({ problem: currentProblemText });
      requestHeaders['Content-Type'] = 'application/json';
      endpoint = '/api/retrieve-documents';
      // effectiveQueryForHistory is already currentProblemText
    }

    try {
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: requestHeaders,
        body: requestBody,
      });

      if (!response.ok) {
        let errorData;
        try {
          errorData = await response.json();
        } catch (e) {
          // If response is not JSON, use text
          const textError = await response.text();
          errorData = { error: textError || `HTTP error! status: ${response.status}` };
        }
        throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
      }

      const data: DocumentResponse = await response.json();
      setDocuments(data.documents);
      setHasSearched(true);



      const newHistoryItem: HistoryItem = {
        id: crypto.randomUUID(),
        query: effectiveQueryForHistory, // Use the combined query description for history
        documents: data.documents,
        timestamp: new Date(),
      };
      setQueryHistory(prevHistory => [newHistoryItem, ...prevHistory.slice(0, 9)]);

      // Fetch similar problems based on the original text or a placeholder if only image
      // The backend would need to decide how to handle `problem` for similar problems if it was image-based.
      // For simplicity, we'll pass the original text problem, or a generic placeholder if only image.
      // Ideally, the backend OCRs and then that text is used for similar problems too.
      // This part might need refinement based on backend capabilities.
      const queryForSimilar = problem.trim() || (selectedImage ? `[Image: ${selectedImage.name}]` : "[Empty Query]");
      await fetchSimilarProblems(queryForSimilar);


    } catch (err) {
      // ... error handling ...
    } finally {
      setIsLoading(false);
    }
  };

    // Optional: Clean up object URL when component unmounts or image changes
  useEffect(() => {
    return () => {
      if (imagePreviewUrl) {
        URL.revokeObjectURL(imagePreviewUrl);
      }
    };
  }, [imagePreviewUrl]);


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

  const handleImageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files[0]) {
      const file = event.target.files[0];
      setSelectedImage(file);
      setImagePreviewUrl(URL.createObjectURL(file)); // Create a temporary URL for preview
    } else {
      setSelectedImage(null);
      setImagePreviewUrl(null);
    }
  };

  const clearImage = () => {
    setSelectedImage(null);
    setImagePreviewUrl(null);
    // If you have a file input ref, you might want to clear its value:
    // if (fileInputRef.current) fileInputRef.current.value = "";
  };




  const appContainerClass = `app-container ${hasSearched ? 'searched-layout' : 'initial-layout'}`;

  return (
    <div className={appContainerClass}>
      <div className="problem-section">
        <h2>Problem Document Retriever</h2>
        <form onSubmit={handleSubmit} className="problem-form">
          <textarea
            value={problem}
            onChange={(e) => setProblem(e.target.value)}
            placeholder="Enter your problem text (optional with image)..."
            rows={hasSearched ? 8 : 4} // Adjust rows
            className="problem-input"
          />

          <div className="file-input-container">
            <label htmlFor="image-upload" className="file-upload-label">
              {selectedImage ? `Selected: ${selectedImage.name}` : "Upload Image (Optional)"}
            </label>
            <input
              type="file"
              id="image-upload"
              accept="image/png, image/jpeg, image/gif, image/webp" // Specify accepted image types
              onChange={handleImageChange}
              style={{ display: 'none' }} // Hide default input, style the label
            />
            {selectedImage && imagePreviewUrl && (
              <div className="image-preview-container">
                <img src={imagePreviewUrl} alt="Preview" className="image-preview" />
                <button type="button" onClick={clearImage} className="clear-image-button">
                  Remove Image
                </button>
              </div>
            )}
          </div>

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