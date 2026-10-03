# CIT 105 Week 2

This project contains two parts:
- Assignment 1: a Python function library with validation and docstrings
- Assignment 2: a Streamlit QR Code Generator

Repository: https://github.com/teknospr/cit105-week2

## Assignment 1 — Function Library
The file `functions.py` includes six functions:

- `celsius_to_fahrenheit(c)`
- `line_total(price, qty)`
- `initials(full_name)`
- `is_valid_url(text)`
- `truncate(text, limit=DEFAULT_TRUNCATE_LIMIT)`
- `safe_filename(text)`

Each function:
- returns a value instead of printing it
- includes a docstring
- validates bad input with clear exceptions or return values
- is designed to be reused by later code

## Assignment 2 — QR Code Generator
The app allows users to:
- enter text or a URL
- see a live character count
- customize QR size, foreground color, and border width
- generate a scannable QR code
- preview the image
- download the image as a PNG file

## Repository Structure
```text
cit105-week2/
├── functions.py
├── demo.py
├── app.py
├── SPEC.md
├── README.md
├── requirements.txt
└── assets/
    └── screenshot.png
```

## Installation (from a clean clone)

### Option A — manual steps (Windows / macOS / Linux)

```bash
git clone https://github.com/teknospr/cit105-week2.git
cd cit105-week2
python -m venv .venv
# activate the virtual environment
# Windows (PowerShell):
#   .\.venv\Scripts\Activate.ps1
# Windows (cmd.exe):
#   .venv\Scripts\activate.bat
# macOS / Linux:
#   source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

### Option B — installer scripts (recommended)
Two helper scripts are included to automate environment creation and dependency installation.

Windows (PowerShell):
- Script: `install_windows.ps1`
- Usage (open PowerShell):
  1. If required, temporarily allow running local scripts for this session:
     ```powershell
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
     ```
  2. Run the installer:
     ```powershell
     .\install_windows.ps1
     ```
  3. Activate the virtual environment if the script does not keep the shell active:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```

macOS / Linux (bash):
- Script: `install_unix.sh`
- Usage:
  ```bash
  chmod +x install_unix.sh
  ./install_unix.sh
  # or
  bash install_unix.sh
  ```

Both scripts will:
- create a `.venv` virtual environment using your system Python
- activate the virtual environment (PowerShell may exit after the script completes; see notes)
- install packages from `requirements.txt`

Notes:
- The scripts assume `python` or `python3` is available on PATH and points to a Python 3 interpreter.
- On Windows PowerShell, script execution may be blocked by policy; using `-Scope Process` changes policy only for the current session.
- If activation does not persist after running the PowerShell script, activate the venv manually as shown above.

## How to pull this repository into another local repository
If you want to bring these files into an existing local repository instead of cloning directly, you can add this repo as a remote and pull a branch or files.

1) Add as a remote and fetch:

```bash
# from inside your existing repo
git remote add cit105 https://github.com/teknospr/cit105-week2.git
git fetch cit105
```

2) Create a local branch from the remote `main`:

```bash
git checkout -b cit105-week2 cit105/main
```

3) (Optional) Merge or cherry-pick the files/commits you need from that branch into your repo's main branch.

Alternative: use sparse checkout (if you only need a subdirectory/files) or `git archive` to export files.

## Dependencies
The application uses:
- Python 3
- streamlit
- qrcode
- pillow

See `requirements.txt` for exact package versions.

## Running the Application
Use:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

## Usage
1. Enter text or a URL in the textbox.
2. Adjust the QR size, foreground color, and border width.
3. Click the button to generate the QR code.
4. Preview the result and download the PNG.

## Screenshot
Add a screenshot file at:

```text
assets/screenshot.png
```

## AI / Copilot Disclosure
GitHub Copilot was used to assist with project scaffolding and code generation. All code was reviewed and understood before submission, and the repository follows the assignment requirements and disclosure expectations.
