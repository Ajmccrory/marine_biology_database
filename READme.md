# Marine Biology Database Midterm

## Required

Python3.x
Ubuntu
MySQL

## Setup
```bash
# in terminal
cd ~/enviornments
python3 -m venv Marine-bio-venv # or whatever name you'll remember
pip install --upgrade pip
pip install -r requirements.txt
cd # back into project directory afterwards
```
### in mysql in terminal
```bash
sudo systemctl start mysql
mysql -u root -p
 # Login
```

### in project
 In app/config.py change yourusername and yourpassword to the systems uername and password


 ### Common Errors
 If there is an issue with permissions with logging in 
 run
 ```bash
 sudo systemctl status mysql
 # ensure server is running
 exit;
 mysql -u root -p
 ALTER 'your username'@'localhost' IDENTIFIED WITH 'your password' BY 'mysql_native_password';
 FLUSH PRIVLEGES;
 ```

