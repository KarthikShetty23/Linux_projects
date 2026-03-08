set -e

SOURCE_DIR="$(pwd)"
BACKUP_DIR="../system_backups"
LOG_FILE="../system_backups/backup.log"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="backup_$TIMESTAMP.tar.gz"

mkdir -p "$BACKUP_DIR"

tar --exclude="$BACKUP_DIR" -czf "$BACKUP_DIR/$BACKUP_FILE" "$SOURCE_DIR"

echo "[$TIMESTAMP] Backup created: $BACKUP_FILE" >> "$LOG_FILE"

echo "Backup successful: $BACKUP_FILE"


# this programs loads the current directory with the abosulte path and along with all the fils and current time.
# it stores every information in a log file, which will keep our file safe, in case of any problems.