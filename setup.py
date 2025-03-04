# combined_setup.py
import sys
from cx_Freeze import setup, Executable
import os

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("Launcher.py", base=base, target_name="Launcher.exe"),
    Executable("package_manager.py", base=base, target_name="Package_manager.exe"),
    Executable("SRS_Recover.py", base=base, target_name="SRS_Recover.exe"),
    # Commenting out Verifier.py for now
    # Executable("Verifier.py", base=base, target_name="Verifier.exe")
]

site_packages_path = os.path.join(sys.prefix, 'Lib', 'site-packages')

setup(
    name="SRS Tools",
    version="1.0",
    description="SRS Tools Collection",
    options={
        'build_exe': {
            'packages': [
                'discord', 'bs4', 'asyncio', 'pyperclip', 'requests', 'httpx', 'certifi', 'ssl', 'queue', 'time', 'threading', 'os'
            ],
            'include_files': [
                site_packages_path
            ],
        }
    },
    executables=executables,
)