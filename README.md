# Retrieval System for Lecture Problems

WM 2025 Final Project Group 16
- 資工三 詹挹辰 B11902057
- 資工三 巫俋霆 B11902051
- 資工三 施廣霖 B11902072

## Overview

**DEMO SITE: https://wm2025.iceylemon.net/**

Please note that the demo site is hosted on a server without GPU acceleration, so the response time may be slow. (Live demo on 6/6 had the site hosted on laptop with GPU.) For faster performance, please run the system locally with GPU.


### Project Structure

![](project_structure.png)

The main components of the system are as follows (only the important files are listed):

- `textbook_retrieval_system/`: Contains the core implementation of the retrieval system.
    - `frontend/`: Contains the frontend implementation for the system. We used React+TypeScript+Vite for the frontend.
        - `src/`: Contains the source code for the frontend.
            - `App.tsx`: The main React application file that renders the frontend.
            - `App.css`: The main CSS file for styling the frontend.
        - `index.html`: The main HTML file for the frontend.
        - `package.json`: Lists the dependencies and scripts for the frontend.
        - `vite.config.ts/`: Configuration file for Vite, the build tool used for the frontend.
    - `backend/`: Contains the backend implementation for the system. We used Flask server for our backend.
        - `embeddings_cache/`: Directory for storing computed embeddings.
        - `parsed_output/`: Directory for storing parsed output from textbooks.
        - `app.py`: The main Flask application file that serves the API endpoints. The retrieval model is also initialized here.
        - `ocr.py`: Script for performing OCR on user query image to extract text.
        - `utils.py`: Utility functions used in the backend.
        - `requirements.txt`: Lists the Python dependencies required to run the backend.
      
- `scripts/`: Contains auxiliary scripts for downloading models and other resources.
- `demo/`: Contains the demo problems and images used for testing the retrieval system.
    - `problems.txt`: A text file containing example problems for testing the retrieval system (an example problem each line).
    - `images/`: Directory containing images of the problems for testing the retrieval system.
- `README.md`: This file, providing an overview and instructions for the system.

## Get Started

To get run the retrieval system, follow these steps:

### Environment Setup

We will be working on `textbook_retrieval_system/` directory, so please make sure you are in the correct directory.

```bash
cd textbook_retrieval_system
```

#### Frontend

Install Node.js and npm (Node Package Manager) if you haven't already. You can download them from [Node.js official website](https://nodejs.org/).


Then, install the required packages and start the development server:

```bash
cd frontend
npm install
npm run dev
```

#### Backend

We use `conda` for environment management, please ensure you have it installed. If you don't have `conda`, you can install it from [Anaconda's official website](https://www.anaconda.com/download).

Create a virtual environment and install the required packages:

```bash
cd backend
conda create -n mineru 'python=3.12' -y
conda activate mineru
python -m pip install -r requirements.txt

# Download the models needed by MinerU
python -m pip install huggingface_hub
wget https://github.com/opendatalab/MinerU/raw/master/scripts/download_models_hf.py -O download_models_hf.py
python download_models_hf.py
```

