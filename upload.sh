#!/bin/sh
if [ $# -ne 4 ]; then
    echo "Usage: $0 <remote_user> <remote_host> <remote_path> <local_folder>"
    exit 1
fi
REMOTE_USER=$1
REMOTE_HOST=$2
REMOTE_PATH=$3
LOCAL_FOLDER=$4
sftp $REMOTE_USER@$REMOTE_HOST <<EOF
put -r $LOCAL_FOLDER/* $REMOTE_PATH
bye
EOF
echo "Folder copied successfully to $REMOTE_HOST:$REMOTE_PATH"