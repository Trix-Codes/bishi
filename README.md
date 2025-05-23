# Bishi Command

Bishi is a lightweight Linux command-line utility that lets you quickly "flag" files for later reference. With Bishi, you can mark important files and easily access them whenever you need to, making it an ideal tool for managing frequently used files.
## Overview

Bishi works by marking (or "flagging") files specified by the user, allowing fast access later. Once a file is flagged, you can retrieve or unflag it using simple commands. This tool is perfect for developers, system administrators, or anyone who wants a quick shortcut to frequently used files.

## Usage

Below are the available commands and flags for Bishi:

### 1. Open Most-Recently Flagged File

Simply run the command without any flags to open the file that was most recently flagged:

```
$ bishi
```
### 2. Open A Flagged File By Index

You can open a specific flagged file by referencing its index:
- Using the `-t` flag:
    ```
    $ bishi -t <Index>
    ```
- Alternatively, using the `-target` flag:
    ```
    $ bishi -target <Index>
    ```
Example: If you have two flagged files: `file1.txt` (index 0) and `file2.txt` (index 1), then running:

    $ bishi -t 1
opens `file2.txt`

### 3. List Flagged Files

You can list the flagged files along with their indexes:
- To list all flagged files, use:
    ```
    $ bishi -ls all
    ```
    or simply
    ```
    $ bishi -ls a
    ```
    Example Output:
    ```
    0   :   file1.txt
    1   :   file2.txt
    ```
- To list the last flagged file, use:
    ```
    $ bishi -ls last
    ```
    or simply
    ```
    $ bishi -ls l
    ```
    Example Output:
    ```
    1   :   file2.txt
    ```
### 4. Flag a File
To flag a file (or file path), you can use either of the following commands:

    $ bishi -f <file or file path>
or

    $ bishi -flag <file or file path>

### 5. Unflag Files
Bishi allows you to unflag files through various commands:
- Unflag all flagged files:
    ```
    $ bishi -uf all
    ```
    or
    ```
    $ bishi -unflag all
    ```
- Unflag a file by its index:
    ```
    $ bishi -uf <Index>
    ```
    or
    ```
    $ bishi -unflag <Index>
    ```
- Unflag a file by specifying its file name or path:
    ```
    $ bishi -uf <file or file path>
    ```
    or
    ```
    $ bishi -unflag <file or file path>
    ```
### 6. Opening a file through another command
You can open a flagged file through any editor of your choice or through another command too. For example:
- Opening a file with index 1 with neovim:
    ```
    $ bishi -o nvim#1
    ```
    or
    ```
    $ bishi -open nvim#1
    ```
- Running a file with index 1 in python:
    ```
    $ bishi -o python3#1
    ```
    or
    ```
    $ bishi -open python3#1
    ```
### 7. Setting Bishi to open flagged files with other editors/programs/commands by default
By default, bishi opens flagged files with the `xdg-open` command. However, you can set it to open flagged files using a different program/editor/command.
- Syntax:
    ```
    bishi -default <opener>
    ```
    or
    ```
    bishi -do <opener>
    ```
  - For example, to make bishi open flagged files in VS Code by default, run:
    ```
    bishi -default code
    ```
    or
    ```
    bishi -do code
    ```
### 8. Restore `bishi` to default settings
If you want to restore the default settings to the `bishi` command, you can.
- To restore default settings:
    ```
    bishi -restore True
    ```
- To not restore that (It's weird that you want to run this command but okay):
    ```
    bishi -restore False
    ```
    (This literally doesn't change anything)

    



## Installation 
Follow these steps to install Bishi on your Linux system:
##### 1. Use the `git clone` command to download the bishi package like this :
    git clone https://github.com/Trix-Codes/bishi

    cd bishi/

##### 2. Run the following commands step by step :
- Creating a Path to move the Packages to:
    ```
    sudo mkdir /bishicom
    ```
- Making the path executable:
    ```
    echo 'export PATH="/bishicom:$PATH"' >> ~/.bashrc
    ```
    or, if you use zsh:
    ```
    echo 'export PATH="/bishicom:$PATH"' >> ~/.zshrc
    ```
- Now add the `.bashrc` or `.zshrc` file to the source:
    ```
    source ~/.bashrc
    ```
    or, if you use zsh:
    ```
    source ~/.zshrc
    ```
- Now make bishi an executable:
    ```
    chmod +x bishi
    ```
- Now move the packages to the executable path
    ```
    sudo mv bishi bishit.json father.py /bishicom
    ```
- All done! You can now use bishi!
