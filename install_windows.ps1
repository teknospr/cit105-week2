# Installer for Windows (PowerShell)

Write-Host "Creating virtual environment (.venv) and installing dependencies..."

# Use python or python3 if python is not available
$python = "python"
try {
    & $python --version > $null 2>&1
} catch {
    $python = "python3"
}

if (-not (Get-Command $python -ErrorAction SilentlyContinue)) {
    Write-Error "Python was not found on PATH. Please install Python 3 and try again."
    exit 1
}

# Create venv
& $python -m venv .venv

# Activate venv for this PowerShell session
$activateScript = Join-Path -Path ".venv\Scripts" -ChildPath "Activate.ps1"
if (Test-Path $activateScript) {
    Write-Host "Activating virtual environment..."
    . $activateScript
} else {
    Write-Warning "Activation script not found at $activateScript. You can activate manually: .\.venv\Scripts\Activate.ps1"
}

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Installation complete. To run the app: streamlit run app.py"
