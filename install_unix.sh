#!/usr/bin/env bash
set -euo pipefail

echo "Creating virtual environment (.venv) and installing dependencies..."

PYTHON="python3"
if command -v python >/dev/null 2>&1; then
  PYTHON=python
fi

if ! command -v $PYTHON >/dev/null 2>&1; then
  echo "Python not found. Please install Python 3 and ensure it's on your PATH." >&2
  exit 1
fi

$PYTHON -m venv .venv

# shellcheck disable=SC1091
. .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

echo "Installation complete. To run the app: streamlit run app.py"
