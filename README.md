
**How to run it:**
1. Ensure you have the required library installed:
   ```bash
   sudo apt install python3-psutil

2. To run the code
   `python3 health_monitor.py`

The program will give the current status of terminal and append the data automatically to a `system_health.log` file.


## 2. Automated System Backup
A Bash automation script that safely compresses and archives server directories. It creates a .tar.gz backup file labeled with a precise timestamp to prevent accidental data overwriting.

**How to run it:**

1. Ensure that the script is executable
   `chmod +x backup_manager.sh`

2. Execute the code
   `./backup_manager.sh`

The script will compress the target directory and save it into a newly created `system_backups` folder.
