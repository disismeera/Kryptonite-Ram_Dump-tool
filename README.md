# Kryptonite RAM Dump

Kryptonite RAM Dump is a Python script designed to facilitate the collection of RAM memory data for forensic analysis on Windows and Linux-based operating systems, specifically Kali Linux and Parrot OS. This tool utilizes the `winpmem` utility on Windows platforms and custom kernel modules (`Kali.ko` or `Parrot.ko`) on Linux platforms to perform the memory acquisition process.

## Video Demo: 
https://youtu.be/UFOAm4n3zrU

## Features

- Automated RAM memory acquisition for forensic analysis.
- Support for both Windows and Linux (Kali Linux and Parrot OS).
- Option to choose between `Kali.ko` and `Parrot.ko` kernel modules based on the user's operating system.

## Prerequisites

Before using the Kryptonite RAM Dump tool, ensure you have the following prerequisites installed:

- Python 3.x
- `winpmem.exe` (for Windows platform)
- Kernel module (`Kali.ko` for Kali Linux or `Parrot.ko` for Parrot OS) compiled and available for loading

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/cyph3rryx/kryptonite-ram-dump.git
cd kryptonite-ram-dump
```

2. Depending on your operating system, navigate to the `kryptonite-ram-dump` directory and modify the `load_command` in the script accordingly:

   For Kali Linux:

   ```python
   load_command = [
       "sudo",
       "insmod",
       "./Kali.ko",
       f"path={current_directory}/{MD5}/{MD5}.mem",
       "format=raw",
   ]
   ```

   For Parrot OS:

   ```python
   load_command = [
       "sudo",
       "insmod",
       "./Parrot.ko",
       f"path={current_directory}/{MD5}/{MD5}.mem",
       "format=raw",
   ]
   ```
NOTE: You can find the both ./Kali.ko and ./Parrot.ko in the repository itself

3. Run the script:

   On Windows:

   ```bash
   python kryptonite_ram_dump.py
   ```

   On Linux:

   ```bash
   python3 kryptonite_ram_dump.py
   ```

4. The script will automatically acquire the RAM memory data and organize it in a directory named with the current timestamp and MD5 hash.
