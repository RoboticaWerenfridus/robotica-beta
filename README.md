 # Robotica Beta
These are all the files for a non-normal robot, created on the WF Robotics group!

Also funny additions and games can be found here! Aswel as beta items, that aren't done or released and in a beta state!

## Containers

We have sorted the files into folders, with multiple names and information contained inside them

>[!CAUTION]
>Do not edit the config files! These are off limits! Only edit of you know what you are doing! We are not responsable for any damage

>[!NOTE]
>Not all files are stored in folders and some may be found in the other repository [Robotica](https://github.com/roboticawerenfridus/robotica)

To get files for your motor controller to control your robot check `sr-only`

If you want to control your robot using a Xbox or Playstation controller, you may need `controller-ct`

For a control panel for either Web or on the device itself, you can find this in `tk-beta` and `web-beta`

> [!CAUTION]
> Some files are marked beta, these files are not finished and may have bugs and glitches that may destroy your device.

## Linux Installation
To install the repository you may first use
```
sudo apt install --upgrade git
git clone https:/github.com/roboticawerenfridus/robotica-beta/
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

>[!IMPORTANT]
>To save diskspace you may delete any files in the repository that you do not need!

>[!CAUTION]
>Do not delete these following files, these are to configure the scripts! If you move the files, please changes the `path` in the script above to the correct `config.yml` found in `robotica-beta/config/<script name>/config.yml`
