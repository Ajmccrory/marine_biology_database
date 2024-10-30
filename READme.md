# Marine Biology Database Midterm

A database application for managing marine biology data.

## Prerequisites

- Python 3.x
- Ubuntu
- MySQL

## Installation & Setup

### 1. Python Environment Setup
```bash
# Create and activate virtual environment
cd ~/environments
python3 -m venv marine-bio-venv
source marine-bio-venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. MySQL Setup
```bash
# Start MySQL service
sudo systemctl start mysql

# Log into MySQL
mysql -u root -p
```
## Running the application
```bash
cd {main dir of project}
python3 run.py
```
or run, run.py using the run feature in the vscode GUI
## Troubleshooting

### MySQL Authentication Issues

If you encounter permission errors when logging into MySQL, follow these steps:

```bash
# 1. Check MySQL server status
sudo systemctl status mysql

# 2. Log into MySQL
mysql -u root -p

# 3. Update authentication method
ALTER USER 'your_username'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password';
FLUSH PRIVILEGES;
```

## Running the Application

[Add instructions for starting and using the application]