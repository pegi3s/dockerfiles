# Common Issues

When running Docker images in Windows, using the Ubuntu app, the following issues must be taken into account.

<details>
<summary><b>White Spaces in the Path</b></summary>

When running the Ubuntu app in a Windows operating system, the path to the project's directory should not have white spaces. This can be easily avoided when the `<windows_username>` does not have blanks. If the `<windows_username>` has white spaces, the easiest solution is to create a new user in that computer without white spaces. Alternatively, try using single quotes around folder names that have white spaces, for instance /mnt/c/Users/'my account'/Documents/Docker that works most of the times.

</details>

<details>
<summary><b>File Extensions</b></summary>

If you have created the text configuration files or the data files (FASTA files, for instance) using Windows applications (Notepad, for instance), it is likely that the files have the `.txt` extension. Therefore, it is advisable to, using the Ubuntu app, go to the project’s directory (for instance by typing, cd `/mnt/c/Users/<windows_username>/Documents/Project`) and then type `ls`. This Linux command will list the name of all files under that directory. If the name of the text configuration files or the data files ends in `.txt`, the full name of the file (including the extension) must be typed in the Docker command that you want to run. Some Docker images may not accept a text configuration file or data file with the `.txt` extension. In those cases, simply use the `mv` command to change the file name (for instance `mv name.txt name`).

</details>

<details>
<summary><b>Line Endings</b></summary>

Text files created on DOS/Windows machines have different line endings than Unix/Linux files:

- DOS/Windows: carriage return and line feed (`\r\n`)
- Unix/Linux: just line feed (`\n`)

Some Docker images may not run because of this difference. There are two simple solutions for this issue:

### Option 1: Using dos2unix

1. Install dos2unix:

   ```bash
   sudo apt-get install dos2unix
   ```

2. Convert the file:

   ```bash
   dos2unix name.txt
   ```

### Option 2: Using sed

Convert line endings with sed:

```bash
sed -i 's/\r$//' name.txt
```

</details>

<details>
<summary><b>End of File Considerations</b></summary>

Some Docker image applications read the lines, one by one, from a text file, as a set of instructions. In computers with a Linux operating system, if there is an extra blank line after the last valid instruction, the application will try to process the blank line as if it were a valid instruction, leading to all sort of problems. Unexpectedly, when using the Windows Ubuntu app, an extra blank line is required at the end of the file in order for the application to be able to read the last valid instruction.

</details>
