
#!/bin/bash

# Update and install necessary packages for Python and distutils
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-distutils

# Upgrade pip and install virtualenv if not installed
pip install --upgrade pip
pip install virtualenv

# Create a virtual environment
virtualenv venv
source venv/bin/activate

# Install required Python packages
pip install -r requirements.txt

# Inform the user about activation of the virtual environment
echo "Setup complete! Activate your environment with 'source venv/bin/activate'."
