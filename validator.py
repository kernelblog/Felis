import os
import sys

import requests


class Validator:
    @staticmethod
    def check_internet_connection():
        try:
            requests.get("http://www.google.com", timeout=5)
        except requests.ConnectionError:
            print("\nPlease check your Internet connection!\n")
            sys.exit(1)

    @staticmethod
    def check_for_updates(self):
        input_result = input("\nCheck for updates? Y/N: ")
        if input_result.lower() == "y":
            os.system(f"python3 {self.prefix}/share/felis/update.py")
