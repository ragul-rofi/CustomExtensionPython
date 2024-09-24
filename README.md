# Custom File Extension (.ragul)

## Overview
The Ragul File Project is a simple application designed to create and read custom `.ragul` file extensions. These files function like text files but contain metadata and allow for structured content organization.

## Features
- Create `.ragul` files with metadata and content.
- Read existing `.ragul` files and display their metadata and content.
- Structured format for easy readability.

## File Structure
- **create**: Function to create a `.ragul` file with optional metadata.
- **read**: Function to read a `.ragul` file, extracting metadata and content.
- **Tkinter App**: A graphical user interface (GUI) to open and display `.ragul` files.

## Usage

### Creating a .ragul File
1. Run the main Python script.
2. Choose the "create" option.
3. Enter the file name (with `.ragul` extension).
4. Add your text content.
5. Metadata is automatically generated with the creation date.

### Reading a .ragul File
1. Run the main Python script.
2. Choose the "read" option.
3. Select the `.ragul` file you want to read.
4. The metadata and content will be displayed in a message box.

## Requirements
- Python 3.x
- Tkinter (usually included with Python installations)

## Installation
1. Clone this repository or download the project files.
2. Ensure you have Python installed on your system.
3. Run the application using the command:
   ```bash
   python ragul_file_opener.py
