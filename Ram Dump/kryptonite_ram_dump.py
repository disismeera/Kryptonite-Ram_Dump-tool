    import shutil
    from pathlib import Path
    import hashlib
    import datetime
    import subprocess
    import os


    current_time = datetime.datetime.now().time()
    Time = current_time.strftime("%H_%M")


    def md5_hash_string(input_string):
        md5_hash = hashlib.md5()
        md5_hash.update(input_string.encode("utf-8"))
        return md5_hash.hexdigest()


    MD5 = md5_hash_string(Time)


    def get_os_name():
        if os.name == "posix":
            return "Linux"
        elif os.name == "nt":
            return "Windows"

    selected_platform = get_os_name()

    if selected_platform == "Windows":
        folder_path = Path(f"{MD5}")
        folder_path.mkdir(parents=True, exist_ok=True)
        cmd_command = f"winpmem.exe {MD5}.raw"
        startup_info = subprocess.STARTUPINFO()
        startup_info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startup_info.wShowWindow = subprocess.SW_HIDE

        completed_process = subprocess.run(
            cmd_command,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            startupinfo=startup_info,
        )

        source_file_path = f"{MD5}.raw"
        destination_folder = f"{MD5}"
        shutil.move(source_file_path, destination_folder)
        script_path = "test.ps1"
        completed_process = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass","-File", script_path], shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        current_folder_path = "Test.txt"
        new_folder_name = f"{MD5}.txt"
        parent_directory = os.path.dirname(current_folder_path)
        new_folder_path = os.path.join(parent_directory, new_folder_name)
        os.rename(current_folder_path, new_folder_path)
        source_file_path = f"{MD5}.txt"
        destination_folder = f"{MD5}"
        shutil.move(source_file_path, destination_folder)


    else:
        current_directory = os.getcwd()
        folder_path = f"{current_directory}/{MD5}"
        os.makedirs(folder_path, exist_ok=True)
        module_name = "lime"
        check_module_command = ["lsmod"]
        completed_process = subprocess.run(
            check_module_command, capture_output=True, text=True
        )

        if module_name in completed_process.stdout:
            # Unload the module
            unload_command = ["sudo", "rmmod", module_name]
            subprocess.run(unload_command)

        # Load the module
        load_command = [
            "sudo",
            "insmod",
            "./Kali.ko",
            f"path={current_directory}/{MD5}/{MD5}.mem",
            "format=raw",
        ]
        subprocess.run(load_command)
        
