
#!/bin/bash

# Update and install necessary packages for Python and setuptools
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Upgrade setuptools to avoid issues with deprecated methods in Python 3.12
pip install --upgrade setuptools==65.5.0  # Ensure we use a compatible version
pip install --upgrade wheel

# Upgrade pip and install virtualenv if not installed
pip install --upgrade pip
pip install virtualenv

# Create a virtual environment
virtualenv venv
source venv/bin/activate

# Install required Python packages, forcing the use of pre-built numpy binaries
pip install numpy==1.24.3 --only-binary=:all:  # Force the installation from pre-built binaries
pip install -r requirements.txt

# Inform the user about activation of the virtual environment
echo "Setup complete! Activate your environment with 'source venv/bin/activate'."
