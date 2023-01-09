import os
import shutil

def cd(args):
    # Change the current working directory
    if len(args) != 1:
        print("Usage: cd directory")
        return
    os.chdir(args[0])

def ls(args):
    # List the contents of the current working directory
    # Check for additional options
    show_hidden = False
    show_details = False
    if "-a" in args:
        show_hidden = True
    if "-l" in args:
        show_details = True

    # Get the list of files and directories
    entries = os.listdir(".")

    # Filter out hidden files and directories
    if not show_hidden:
        entries = [e for e in entries if not e.startswith(".")]

    # Print the entries
    for entry in entries:
        if show_details:
            # Get the details of the entry
            stat = os.stat(entry)
            permissions = oct(stat.st_mode)[-3:]
            num_links = stat.st_nlink
            owner = stat.st_uid
            group = stat.st_gid
            size = stat.st_size
            modified_time = stat.st_mtime
            # Print the details
            print(f"{permissions} {num_links} {owner} {group} {size} {modified_time} {entry}")
        else:
            # Print the entry name
            print(entry)

def mkdir(args):
    # Create a new directory
    if len(args) != 1:
        print("Usage: mkdir directory")
        return
    os.mkdir(args[0])

def rmdir(args):
    # Remove a directory
    if len(args) != 1:
        print("Usage: rmdir directory")
        return
    shutil.rmtree(args[0])

def touch(args):
    # Create a new file
    if len(args) != 1:
        print("Usage: touch file")
        return
    with open(args[0], "w"):
        pass

def rm(args):
    # Remove a file
    if len(args) != 1:
        print("Usage: rm file")
        return
    os.remove(args[0])

def cp(args):
    # Copy a file
    if len(args) != 2:
        print("Usage: cp source destination")
        return
    shutil.copy(args[0], args[1])

def sort(args):
    # Sort the lines of a file
    if len(args) != 1:
        print("Usage: sort file")
        return
    with open(args[0], "r") as f:
        lines = f.readlines()
    lines.sort()
    with open(args[0], "w") as f:
        f.writelines(lines)


def mv(args):
    # Move a file
    if len(args) != 2:
        print("Usage: mv source destination")
        return
    shutil.move(args[0], args[1])

def cat(args):
    # Concatenate files
    if len(args) < 1:
        print("Usage: cat file [file...]")
        return
    for file in args:
        with open(file, "r") as f:
            print(f.read())

def grep(args):
    # Search for a pattern in a file
    if len(args) != 2:
        print("Usage: grep pattern file")
        return
    pattern = args[0]
    file = args[1]
    with open(file, "r") as f:
        for line in f:
            if pattern in line:
                print(line)

def find(args):
    # Search for a file or directory
    if len(args) != 2:
        print("Usage: find name directory")
        return
    name = args[0]
    directory = args[1]
    for root, dirs, files in os.sort(args):
    # Sort the lines of a file
      if len(args) != 1:
          print("Usage: sort file")
          return
      with open(args[0], "r") as f:
          lines = f.readlines()
      lines.sort()
      with open(args[0], "w") as f:
          f.writelines(lines)

def uniq(args):
    # Remove duplicate lines from a file
    if len(args) != 1:
        print("Usage: uniq file")
        return
    with open(args[0], "r") as f:
        lines = f.readlines()
    with open(args[0], "w") as f:
        for line in lines:
            if line not in f:
                f.write(line)

def wc(args):
    # Count the lines, words, and characters in a file
    if len(args) != 1:
        print("Usage: wc file")
        return
    lines = 0
    words = 0
    characters = 0
    with open(args[0], "r") as f:
        for line in f:
            lines += 1
            words += len(line.split())
            characters += len(line)
    print(f"{lines} {words} {characters} {args[0]}")

def head(args):
    # Display the first few lines of a file
    if len(args) != 2:
        print("Usage: head [-n lines] file")
        return
    if args[0] == "-n":
        num_lines = int(args[1])
        file = args[2]
    else:
        num_lines = 10
        file = args[0]
    with open(file, "r") as f:
        for i, line in enumerate(f):
            if i == num_lines:
                break
            print(line)

def tail(args):
    # Display the last few lines of a file
    if len(args) != 2:
        print("Usage: tail [-n lines] file")
        return
    if args[0] == "-n":
        num_lines = int(args[1])
        file = args[2]
    else:
        num_lines = 10
        file = args[0]
    with open(file, "r") as f:
        lines = f.readlines()
    for line in lines[-num_lines:]:
        print(line)

def diff(args):
    # Compare the contents of two files
    if len(args) != 2:
        print("Usage: diff file1 file2")
        return
    with open(args[0], "r") as f1:
        lines1 = f1.readlines()
    with open(args[1], "r") as f2:
        lines2 = f2.readlines()
    for line1, line2 in zip(lines1, lines2):
        if line1 != line2:
            print(f"{args[0]}: {line1}", end="")
            print(f"{args[1]}: {line2}", end="")

def tar(args):
    # Create a tar archive
    if len(args) < 1:
        print("Usage: tar file [file...]")
        return
    import tarfile
    with tarfile.open("archive.tar", "w") as tar:
        for file in args:
            tar.add(file)

def gunzip(args):
    # Decompress a gzip archive
    if len(args) != 1:
        print("Usage: gunzip file")
        return
    import gzip
    with gzip.open(args[0], "rb") as f_in:
        with open(args[0][:-3], "wb") as f_out:
            f_out.write(f_in.read())

def chmod(args):
    # Change the permissions of a file or directory
    if len(args) != 2:
        print("Usage: chmod mode file")
        return
    mode = int(args[0], 8)
    file = args[1]
    os.chmod(file, mode)

while True:
    # Display a prompt
    cwd = os.getcwd()
    print(f"{cwd} $ ", end="")

    # Read a command
    command = input()

    # Parse the command and arguments
    tokens = command.split()
    if not tokens:
        continue
    cmd = tokens[0]
    args = tokens[1:]

    # Execute the command
    if cmd == "cd":
        cd(args)
    elif cmd == "ls":
        ls(args)
    elif cmd == "mkdir":
        mkdir(args)
    elif cmd == "rmdir":
        rmdir(args)
    elif cmd == "touch":
        touch(args)
    elif cmd == "rm":
        rm(args)
    elif cmd == "cp":
        cp(args)
    elif cmd == "mv":
        mv(args)
    elif cmd == "cat":
        cat(args)
    elif cmd == "grep":
        grep(args)
    elif cmd == "find":
        find(args)
    elif cmd == "sort":
        sort(args)
    elif cmd == "uniq":
        uniq(args)
    elif cmd == "wc":
        wc(args)
    elif cmd == "head":
        head(args)
    elif cmd == "tail":
        tail(args)
    elif cmd == "diff":
        diff(args)
    elif cmd == "tar":
        tar(args)
    elif cmd == "gunzip":
        gunzip(args)
    elif cmd == "chmod":
        chmod(args)
    elif cmd == "exit":
        break
    else:
        print("Unknown command")

