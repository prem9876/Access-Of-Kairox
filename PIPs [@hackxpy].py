import os
import time

class PipInstaller:
    def __init__(self):
        self.packages = [
            "httpx[http2]",
            "requests",
            "user_agent",
            "python-cfonts",
            "telebot",
            "Topython",
            "fake_useragent",
            "pyfiglet",
            "selenium",
            "youtube-dl",
            "pysocks",
            "curl2pyreqs",
            "rich",
            "pycryptodome",
            "python-telegram-bot",
            "mechanize",
            "pafy",
            "beautifulsoup4",
            "ethan",
            "asmix"
        ]

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def install_package(self, package):
        print(f"[*] Installing: {package}")

        try:
            result = os.system(f'python -m pip install "{package}"')

            if result == 0:
                print(f"[✓] {package} installed successfully")
                return True

            else:
                print(f"[✗] Failed to install {package}")
                return False

        except Exception as e:
            print(f"[✗] Error installing {package}: {e}")
            return False


    def run_installation(self):
        self.clear_screen()

        total = len(self.packages)

        print("=" * 45)
        print("        AUTO PIP INSTALLER")
        print("=" * 45)

        print(f"\n[*] Total packages: {total}")
        time.sleep(1)

        success = 0
        failed = 0

        for number, package in enumerate(self.packages, 1):

            print("\n" + "-" * 45)
            print(f"[{number}/{total}]")

            if self.install_package(package):
                success += 1
            else:
                failed += 1

            time.sleep(0.2)


        print("\n" + "=" * 45)
        print("        INSTALL FINISHED")
        print("=" * 45)

        print(f"[✓] Successful : {success}")
        print(f"[✗] Failed     : {failed}")

        print("=" * 45)


if __name__ == "__main__":
    installer = PipInstaller()
    installer.run_installation()