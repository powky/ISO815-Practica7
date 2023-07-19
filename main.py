import subprocess

def upload_file_via_lftp(local_file_path, remote_file_path, ftp_host, ftp_user, ftp_pass, ftp_port=21):
    # Construir el comando para el FTP
    lftp_command = f'lftp -u {ftp_user},{ftp_pass} -e "put {local_file_path} -o {remote_file_path}; quit" -p {ftp_port} {ftp_host}'

    # Ejecutar el comando usando subprocess
    try:
        subprocess.run(lftp_command, shell=True, check=True)
        print("Archivo cargado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al cargar: {e}")

# Usage
local_file_path = 'archivo'
remote_file_path = 'ruta'
ftp_host = 'servidor'
ftp_user = 'usuario'
ftp_pass = 'clave'

upload_file_via_lftp(local_file_path, remote_file_path, ftp_host, ftp_user, ftp_pass)