import os
import time

# specify the directory to monitor and the log file name
watch_directory = "/Users/mohamed-elbadri/Desktop/TestPython"
log_file = "changes.log"

# create a dictionary to store the current state of the files in the directory
current_files = {}

# loop indefinitely to monitor the directory for changes
while True:
    # get a list of the files in the directory
    files = os.listdir(watch_directory)
    
    # check for new files or changes in existing files
    for file in files:
        # if the file is not already in the current_files dictionary, log it as a new file
        if file not in current_files:
            with open(log_file, "a") as f:
                f.write(f"New file detected: {file}\n")
            current_files[file] = os.path.getmtime(os.path.join(watch_directory, file))
        # if the file is already in the current_files dictionary, check if it has been modified
        else:
            mtime = os.path.getmtime(os.path.join(watch_directory, file))
            if mtime != current_files[file]:
                with open(log_file, "a") as f:
                    f.write(f"File modified: {file}\n")
                current_files[file] = mtime
    
    # check for deleted files
    for file in list(current_files):
        if file not in files:
            with open(log_file, "a") as f:
                f.write(f"File deleted: {file}\n")
            del current_files[file]
    
    # wait for a short amount of time before checking for changes again
    time.sleep(1)

