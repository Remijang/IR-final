// frontend/src/App.tsx
import { useState, type FormEvent, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

import 'katex/dist/katex.min.css';
import './App.css';

interface RetrievedDocument {
  filename: string;
  content: string;
}

interface DocumentResponse {
  documents: RetrievedDocument[];
}

interface HistoryItem {
  id: string;
  query: string;
  documents: RetrievedDocument[];
  timestamp: Date;
}

type InputMode = 'text' | 'image';


function App() {
  const [inputMode, setInputMode] = useState<InputMode>('text');
  const [problem, setProblem] = useState<string>('');
  const [selectedImage, setSelectedImage] = useState<File | null>(null);
  const [imagePreviewUrl, setImagePreviewUrl] = useState<string | null>(null);
  const [isOcrLoading, setIsOcrLoading] = useState<boolean>(false);
  const [ocrError, setOcrError] = useState<string | null>(null);


  const [documents, setDocuments] = useState<RetrievedDocument[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [hasSearched, setHasSearched] = useState<boolean>(false);
  const [selectedDocumentIndex, setSelectedDocumentIndex] = useState<number | null>(null);
  const [queryHistory, setQueryHistory] = useState<HistoryItem[]>([]);

  // related problems
  const [relatedProblems, setRelatedProblems] = useState<RetrievedDocument[]>([]);
  const [isLoadingRelatedProblems, setIsLoadingRelatedProblems] = useState<boolean>(false);
  const [selectedRelatedProblemIndex, setSelectedRelatedProblemIndex] = useState<number | null>(null);
  const [relatedProblemsError, setRelatedProblemsError] = useState<string | null>(null);



  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const currentProblemText = problem.trim();

    if (!currentProblemText) {
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

    // reset related problems
    setRelatedProblems([]);
    setSelectedRelatedProblemIndex(null);
    setRelatedProblemsError(null);

    const requestBody = JSON.stringify({ problem: currentProblemText });
    const requestHeaders: HeadersInit = { 'Content-Type': 'application/json' };
    const endpoint = '/api/retrieve-documents';

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
        query: currentProblemText,
        documents: data.documents,
        timestamp: new Date(),
      };
      setQueryHistory(prevHistory => [newHistoryItem, ...prevHistory.slice(0, 9)]);

      const queryForSimilar = problem.trim() || (selectedImage ? `[Image: ${selectedImage.name}]` : "[Empty Query]");
      await fetchSimilarProblems(queryForSimilar);


    } catch (err) {
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    const currentPreviewUrl = imagePreviewUrl;
    return () => {
      if (currentPreviewUrl) {
        URL.revokeObjectURL(currentPreviewUrl);
      }
    };
  }, [imagePreviewUrl]);



  const fetchSimilarProblems = async (problemQuery: string) => {
    setIsLoadingRelatedProblems(true);
    setRelatedProblemsError(null);
    setRelatedProblems([]);
    setSelectedRelatedProblemIndex(null);

    try {
      const response = await fetch('/api/similar-problems', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ problem: problemQuery }),
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
    setProblem(historyItem.query);
    setDocuments(historyItem.documents);
    setSelectedDocumentIndex(null);
    setHasSearched(true);
    setError(null);

    setRelatedProblems([]);
    setSelectedRelatedProblemIndex(null);
    setRelatedProblemsError(null);
    if (historyItem.query) {
      await fetchSimilarProblems(historyItem.query);
    }

  };

  const handleSelectRelatedProblem = (index: number) => {
    setSelectedRelatedProblemIndex(index);
  };

  const handleReturnToRelatedProblemList = () => {
    setSelectedRelatedProblemIndex(null);
  };

  const clearImage = () => {
    setSelectedImage(null);
    if (imagePreviewUrl) {
      URL.revokeObjectURL(imagePreviewUrl);
    }
    setImagePreviewUrl(null);
    setOcrError(null);
  };

  const handleImageSelectionForOCR = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (isOcrLoading) return; // Prevent change during OCR
    clearImage();
    if (event.target.files && event.target.files[0]) {
      const file = event.target.files[0];
      setSelectedImage(file);
      setImagePreviewUrl(URL.createObjectURL(file));
    }
  };

  const processImageWithOCR = async () => {
    if (!selectedImage) return;

    setIsOcrLoading(true);
    setOcrError(null);
    setProblem('');

    const formData = new FormData();
    formData.append('image', selectedImage);

    try {
      const response = await fetch('/api/ocr-image', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        let errorData;
        try {
            errorData = await response.json();
        } catch(e){
            const textError = await response.text();
            errorData = { error: textError || `OCR request failed with status: ${response.status}` };
        }
        throw new Error(errorData.error || `OCR request failed`);
      }

      const data: { ocr_text: string } = await response.json();
      setProblem(data.ocr_text);
      setInputMode('text');
    } catch (err) {
      if (err instanceof Error) {
        setOcrError(err.message);
      } else {
        setOcrError('An unknown error occurred during OCR processing.');
      }
      console.error("OCR failed:", err);
    } finally {
      setIsOcrLoading(false);
    }
  };


  const appContainerClass = `app-container ${hasSearched ? 'searched-layout' : 'initial-layout'}`;

  return (
    <div className={appContainerClass}>
      <div className="problem-section">
        <h2>Problem Document Retriever</h2>
        <div className="input-mode-selector">
          <button
            onClick={() => { setInputMode('text'); clearImage(); }}
            className={inputMode === 'text' ? 'active' : ''}
            disabled={isOcrLoading}
          >
            Enter Text
          </button>
          <button
            onClick={() => { setInputMode('image'); setProblem(''); }}
            className={inputMode === 'image' ? 'active' : ''}
            disabled={isOcrLoading}
          >
            Upload Image for OCR
          </button>
        </div>

        <form onSubmit={handleSubmit} className="problem-form">
          {inputMode === 'text' && (
            <textarea
              value={problem}
              onChange={(e) => setProblem(e.target.value)}
              placeholder="Enter your problem or edit OCR result..."
              rows={hasSearched ? 8 : 6}
              className="problem-input"
              disabled={isOcrLoading}
            />
          )}

          {inputMode === 'image' && (
            <div className="file-input-area">
              <div className="file-input-container">
                <label htmlFor="image-upload" className="file-upload-label">
                  {selectedImage ? `Selected: ${selectedImage.name}` : "Choose an Image"}
                </label>
                <input
                  type="file"
                  id="image-upload"
                  accept="image/png, image/jpeg, image/gif, image/webp"
                  onChange={handleImageSelectionForOCR}
                  style={{ display: 'none' }}
                  disabled={isOcrLoading}
                />
              </div>
              {imagePreviewUrl && (
                <div className="image-preview-container">
                  <img src={imagePreviewUrl} alt="Preview" className="image-preview" />
                  <button
                    type="button"
                    onClick={processImageWithOCR}
                    className="ocr-button"
                    disabled={!selectedImage || isOcrLoading}
                  >
                    {isOcrLoading ? 'Processing OCR...' : 'Get Text from Image (OCR)'}
                  </button>
                  <button
                    type="button"
                    onClick={clearImage}
                    className="clear-image-button"
                    disabled={isOcrLoading}
                  >
                    Remove Image
                  </button>
                </div>
              )}
              {ocrError && <p className="error-message ocr-error-message">{ocrError}</p>}
            </div>
          )}

          {inputMode === 'text' &&
          <button
            type="submit"
            disabled={isLoading || isOcrLoading || (inputMode === 'text' && !problem.trim())}
            className="submit-button"
          >
            {isLoading ? 'Retrieving...' : 'Retrieve Documents'}
          </button>}
        </form>

        {error && <p className="error-message">Error: {error}</p>}
        {isLoading && !hasSearched && <p className="loading-message">Loading...</p>}

        {/* History Section */}
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
        <div className="documents-section"> {/* right pane */}
          
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
              <div className="selected-item-view">
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
              <div className="document-list-container">
                <h2>Related Problems</h2>
                <ul className="document-title-list">
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
              <div className="selected-item-view">
                <button onClick={handleReturnToRelatedProblemList} className="return-button">
                  ← Back to Related Problems List
                </button>
                <h3 className="selected-item-filename">
                  <ReactMarkdown>
                    {relatedProblems[selectedRelatedProblemIndex].filename}
                  </ReactMarkdown>
                </h3>
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