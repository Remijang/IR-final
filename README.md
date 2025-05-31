# WM Final Project

## MinerU Environment Setup

### Build the Environment

```bash
conda create -n mineru 'python=3.12' -y
conda activate mineru
python -m pip install "magic-pdf[full]"
```

### Download the Models

```bash
python MinerU/scripts/download_models_hf.py
```
