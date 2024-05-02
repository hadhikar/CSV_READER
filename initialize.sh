#!/bin/bash

EXTENSIONS=(
    "ms-python.python"
    "ms-python.black-formatter"
    "donjayamanne.python-environment-manager"
    "ms-python.debugpy"
    "njpwerner.autodocstring"
    "KevinRose.vsc-python-indent"
    "Mukundan.python-docs"
)

#install the extensions using the vscode cli
for EXT in "${EXTENSIONS[@]}"
do
    code --install-extension $EXT
done

PYTHON_CMD=$(which python3 || which python || echco "")

if [ -z $PYTHON_CMD ]; then
    echo "Python not found"
    exit 1
fi

# Check the exisiting Virtual Environment and create a new one if not found
if [ ! -d ".venv" ]; then
    echo "Creating Virtual Environment"
    $PYTHON_CMD -m venv .venv
else
    echo "Virtual Environment already exists"
fi

# Activate the Virtual Environment
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
else
    echo "Virtual Environment not found"
    exit 1
fi

# Install the required packages
echo "Installing the required packages"
python -m pip install --upgrade pip

if [ -f "requirements.txt" ]; then
    python -m pip install -r requirements.txt
else
    echo "requirements.txt not found"
    exit 1
fi

# Pre-commit install and add to git hooks
pip install pre-commit
pre-commit install
pre-commit autoupdate

# Make the run_black.sh executable
chmod +x run_black.sh

# Add the current directory to the PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:${pwd}"

echo "Initialization complete"
