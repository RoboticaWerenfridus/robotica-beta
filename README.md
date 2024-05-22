 # Robotica Beta
These are all the files for a non-normal robot, created on the WF Robotics group!

These are all the explanations of the following types of files:

## File Types
SR - School Robot, these are for a robot with a Motor Controller and custom settings, change if needed! Warning these are not supported on a NON-Motor Controller robot

C-CT (Controller-CT) - This is controller using a Xbox Controller, supported for Motor Controller & Normal

TK (Tkinter) - Using this you can control the robot on a window on the robot itself (Pi)

WEB (web) - Control of robot using website! REQUIRES WIFI CONNECTION

AUDIO-TTS (text to speech) - This is used to send command by Microphone! For more info check the README file in the folder

BORED-GAMES - Fun python games to play if you are bored!
> [!CAUTION]
> Some files are marked beta, these files are not finished and may have bugs and glitches that may destroy your device.
## Linux Installation
-
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
>sudo apt upgrade```
>Note: This may require a internet connection

Then you may execute any of our programs and Enjoy!

>[!TIP]
>Update your Python version to `Python3.9` and create a `SE Envoirment` for no bugs and issues with future updates.
