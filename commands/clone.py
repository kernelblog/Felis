import os
import ssl
import sys
import tarfile
import urllib.request
import zipfile


def download_file(file_url, file_type):
    context = ssl._create_unverified_context()
    print("\nDownloading tool...")
    data = urllib.request.urlopen(file_url, context=context).read()

    file_name = "tool" + file_type
    with open(file_name, 'wb') as file:
        file.write(data)

    if file_type == ".zip":
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall()
    elif file_type == ".tar.gz":
        with tarfile.open(file_name, "r:gz") as tar_ref:
            tar_ref.extractall()

    os.remove(file_name)
    print("\nThe tool was successfully downloaded and extracted.")


def call(args):
    has_url = len(args) > 2
    if not has_url:
        print("\nPlease provide a URL!\n")
        sys.exit(0)

    file_url = args[2]
    file_extension = file_url.split('.')[-1]
    if file_extension in ["zip", "git", "deb", "tar.gz"]:
        download_file(file_url, f".{file_extension}")
    else:
        print("\nUnsupported file type. Please use a .zip, .deb, .tar.gz file, or a git repository.\n")
