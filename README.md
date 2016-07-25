# plant-phone
by Katherine Erickson and Marielle Foster

- Building a phone that works using VoIP
- Speaker, buttons, microphone, wifi and lcd screen
- Raspberry Pi 2


# Setup

### Pi OS

Add various aliases to ~/.bashrc.


Set up wireless:
https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md


Switch keyboard language:
https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=80127


Install Vim:

```
sudo apt-get install vim
```


### Sound

See http://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Install_supporting_packages

```
sudo apt-get update
sudo apt-get install mplayer
sudo apt-get upgrade
sudo apt-get install alsa-utils  # Already installed. Suggested doing the below step.
sudo apt-get -f install
sudo apt-get install festival
```
