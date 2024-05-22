 # Robotica Beta
These are all the files for a non-normal robot, created on the WF Robotics group!

These are all the explanations of the following types of files:

## Containers

We have sorted the files into folders, with multiple names and information contained inside them

To get files for your motor controller to control your robot check `sr-only`

If you want to control your robot using a Xbox or Playstation controller, you may need `controller-ct`

For a control panel for either Web or on the device itself, you can find this in `tk-beta` and `web-beta`

> [!CAUTION]
> Some files are marked beta, these files are not finished and may have bugs and glitches that may destroy your device.
## Linux Installation
To install the repository you may first use
```
sudo apt install --upgrade git
git clone https:/github.com/NathanSchalkwijk/robotica-beta/audio-tts-beta/
```

To install all the custom libraries, please use our custom script `libs-installer.py`
```
cd robotica-beta
sudo python libs-installer.py
```
>[!WARNING]
>If any issues occur doing any of these steps, make sure you upgrade your OS to the latest version using these commands
>```sudo apt-get update
>sudo apt upgrade
>```
>**Note:** This may require a internet connection

Then you may execute any of our programs and Enjoy!

>[!TIP]
>Update your Python version to `Python3.9` and create a `SE Envoirment` for no bugs and issues with future updates.
