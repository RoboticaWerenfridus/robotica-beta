import subprocess

def install_library(library_name):

    try:

        # Check if the library is already installed

        __import__(library_name)

        print(f"{library_name} is already installed.")

    except ImportError:

        # Install the library using pip

        print(f"Installing {library_name}...")

        subprocess.check_call(['pip', 'install', library_name])

        print(f"{library_name} has been successfully installed.")

# Install bluedot library

install_library('bluedot')

# Install tkinter library

install_library('tk')

# Install Flask library

install_library('Flask')

# Install YAML library

install_library('pyyaml')
