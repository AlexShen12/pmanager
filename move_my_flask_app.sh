#!/bin/bash

# ---------------------------------------------------------------------
# Script Name: move_my_flask_app.sh
# Description: Moves the 'my_flask_app' directory from Documents to Otherwork
# Author: Your Name
# Date: YYYY-MM-DD
# ---------------------------------------------------------------------

# Define variables for source and destination directories
SOURCE_DIR="/Users/kabirgrewal/Documents/my_flask_app"
DESTINATION_PARENT_DIR="/Users/kabirgrewal/SolarWinds/genz/Otherwork"
DESTINATION_DIR="$DESTINATION_PARENT_DIR/my_flask_app"

# Function to display messages
function echo_info() {
    echo -e "\033[1;34m[INFO]\033[0m $1"
}

function echo_success() {
    echo -e "\033[1;32m[SUCCESS]\033[0m $1"
}

function echo_error() {
    echo -e "\033[1;31m[ERROR]\033[0m $1"
}

# 1. Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo_error "Source directory '$SOURCE_DIR' does not exist. Exiting."
    exit 1
fi

echo_info "Source directory '$SOURCE_DIR' found."

# 2. Check if the destination parent directory exists; if not, create it
if [ ! -d "$DESTINATION_PARENT_DIR" ]; then
    echo_info "Destination parent directory '$DESTINATION_PARENT_DIR' does not exist. Creating it..."
    mkdir -p "$DESTINATION_PARENT_DIR"
    if [ $? -ne 0 ]; then
        echo_error "Failed to create destination parent directory '$DESTINATION_PARENT_DIR'. Exiting."
        exit 1
    fi
    echo_success "Destination parent directory '$DESTINATION_PARENT_DIR' created successfully."
else
    echo_info "Destination parent directory '$DESTINATION_PARENT_DIR' already exists."
fi

# 3. Check if the destination directory already exists
if [ -d "$DESTINATION_DIR" ]; then
    echo_error "Destination directory '$DESTINATION_DIR' already exists. Please remove it or choose a different destination."
    exit 1
fi

# 4. Move the directory
echo_info "Moving '$SOURCE_DIR' to '$DESTINATION_PARENT_DIR'..."
mv "$SOURCE_DIR" "$DESTINATION_PARENT_DIR"

# 5. Verify the move
if [ $? -eq 0 ]; then
    echo_success "Directory moved successfully to '$DESTINATION_DIR'."
else
    echo_error "Failed to move the directory. Please check permissions and try again."
    exit 1
fi

# 6. Optional: Confirm removal of source directory (if any)
# Since 'mv' typically moves the directory, the source should no longer exist.
# However, to ensure, we can check and remove if necessary.

if [ -d "$SOURCE_DIR" ]; then
    echo_info "Source directory still exists. Removing it..."
    rm -rf "$SOURCE_DIR"
    if [ $? -eq 0 ]; then
        echo_success "Source directory '$SOURCE_DIR' removed successfully."
    else
        echo_error "Failed to remove source directory '$SOURCE_DIR'. Please remove it manually."
    fi
else
    echo_info "Source directory '$SOURCE_DIR' no longer exists."
fi

# End of Script




