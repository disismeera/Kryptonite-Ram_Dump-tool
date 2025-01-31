# Kryptonite Plug-and-Play AutoRun Script:

The Kryptonite RAM Dump AutoRun feature provides a convenient and straightforward way to collect RAM memory data for forensic analysis. By simply plugging the USB drive into the target system, the AutoRun functionality initiates a sequence of scripts that automate the RAM Dump process. This eliminates the need for manual intervention, allowing users to easily take the RAM Dump from any Windows system after just granting the permission with a single press of the ENTER key.

## Usage

Follow these steps to utilize the Kryptonite RAM Dump AutoRun feature:

1. Insert the provided USB drive into the target system.

2. Once the USB drive is connected, the AutoRun functionality will automatically begin execution.

3. The following sequence of actions will take place:

   - The `AUTORUN.INF` file will be executed, triggering the AutoRun process.
   - The user will be prompted to grant permission for script execution by pressing the ENTER key.

4. After permission is granted, the AutoRun feature will proceed with the following steps:

   - Execute `Non_GUI.exe` to initiate RAM memory data collection.
   - Combine collected data using `combine.exe`.
   - Run `test.ps1` PowerShell script for additional processing.
   - Utilize `winpmem.exe` to capture RAM memory data.

5. The RAM Dump collection will proceed automatically, ensuring a seamless experience for users and exits once the dump is over.

## Important Note

- The Kryptonite RAM Dump AutoRun feature is designed for Windows operating systems.
- Ensure that you have the necessary permissions and legal rights before using this tool on any system.
