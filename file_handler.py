"""
GTP-002: File Handler Module
This module handles file operations and system commands
WARNING: This file intentionally contains command injection and insecure file operation vulnerabilities
"""

import os
import subprocess
import pickle
import yaml

class FileHandler:
    """Handles file operations"""
    
    def __init__(self):
        # SECURITY ISSUE: Hardcoded sensitive path
        self.backup_dir = "/var/backups/sensitive_data"
        self.admin_key = "FileHandler_AdminKey_987654321"
    
    def read_file(self, filename):
        """
        SECURITY ISSUE: Path traversal vulnerability
        No validation of file path allows directory traversal attacks
        """
        with open(filename, 'r') as f:
            return f.read()
    
    def execute_backup(self, backup_name):
        """
        SECURITY ISSUE: Command injection vulnerability
        User input directly passed to shell command
        """
        command = f"tar -czf /backups/{backup_name}.tar.gz /data"
        os.system(command)
    
    def compress_files(self, directory, output_file):
        """
        SECURITY ISSUE: Command injection via subprocess
        """
        cmd = f"zip -r {output_file} {directory}"
        subprocess.call(cmd, shell=True)
    
    def delete_old_logs(self, days):
        """
        SECURITY ISSUE: Command injection in find command
        """
        command = "find /var/log -type f -mtime +" + str(days) + " -delete"
        os.system(command)
    
    def process_user_file(self, user_input):
        """
        SECURITY ISSUE: eval() with user input - CRITICAL
        """
        result = eval(user_input)
        return result
    
    def load_config_unsafe(self, config_path):
        """
        SECURITY ISSUE: Unsafe YAML load
        """
        with open(config_path, 'r') as f:
            config = yaml.load(f)  # Should use yaml.safe_load()
        return config
    
    def deserialize_data(self, data_file):
        """
        SECURITY ISSUE: Unsafe pickle deserialization
        """
        with open(data_file, 'rb') as f:
            data = pickle.load(f)  # Pickle can execute arbitrary code
        return data
    
    def run_diagnostic(self, host):
        """
        SECURITY ISSUE: Command injection via ping
        """
        cmd = f"ping -c 4 {host}"
        output = subprocess.check_output(cmd, shell=True)
        return output.decode()

def execute_system_command(user_command):
    """
    SECURITY ISSUE: Direct execution of user-provided commands
    """
    # Extremely dangerous - executes any command user provides
    result = os.popen(user_command).read()
    return result

def process_uploaded_file(filepath, destination):
    """
    SECURITY ISSUE: No validation of file type or content
    """
    os.system(f"mv {filepath} {destination}")

def extract_archive(archive_path):
    """
    SECURITY ISSUE: Zip slip vulnerability
    No path validation when extracting archives
    """
    import zipfile
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall("/tmp/extracted")  # No validation of file paths in zip

def run_migration(migration_file):
    """
    SECURITY ISSUE: Executing untrusted SQL files
    """
    cmd = f"mysql -u root -pRootPass123! < {migration_file}"
    os.system(cmd)

class LogManager:
    """Manages application logs"""
    
    def __init__(self):
        # SECURITY ISSUE: World-writable log directory
        self.log_dir = "/tmp/app_logs"
        os.makedirs(self.log_dir, mode=0o777, exist_ok=True)
    
    def tail_log(self, log_file, lines):
        """
        SECURITY ISSUE: Command injection in tail command
        """
        cmd = f"tail -n {lines} {log_file}"
        output = subprocess.run(cmd, shell=True, capture_output=True)
        return output.stdout.decode()
    
    def grep_log(self, pattern, log_file):
        """
        SECURITY ISSUE: Command injection in grep
        """
        command = f"grep '{pattern}' {log_file}"
        result = os.popen(command).read()
        return result

# SECURITY ISSUE: Hardcoded encryption key
BACKUP_ENCRYPTION_KEY = "BackupKey123456789012345678901234"

def backup_database(db_name):
    """
    SECURITY ISSUE: Command injection + hardcoded password
    """
    password = "DBBackupPass@2024"
    cmd = f"mysqldump -u admin -p{password} {db_name} > /backups/{db_name}.sql"
    os.system(cmd)

print("[FILE_HANDLER] File handler module loaded with insecure file operations")
