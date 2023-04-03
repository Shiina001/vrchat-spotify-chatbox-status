@echo off
echo "Installing required modules"
python -m pip install -r requirements.txt
cls
echo "Running the script..."
python vrchat-spotify-chatbox-status/main.py
pause