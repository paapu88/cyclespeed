# Cycle Velocity

- A super simple app that shows two numbers in an **android** device.
    - Upper one is the current speed [km/h]
    - Lower on is the average speed during your cycling so far [km/h].
    - Average speed is recorded only when the speed is greater than 10 km/h.
    - Uses only the gps of your android device.

markus.kaukonen@student.hanken.fi

- sign
https://stackoverflow.com/questions/65988193/error-while-signing-an-kivy-app-for-the-play-store
```commandline
export P4A_RELEASE_KEYSTORE=~/keystores/mykeyfilename.keystore 
export P4A_RELEASE_KEYSTORE_PASSWD=tavallinenvaimojuttu
export P4A_RELEASE_KEYALIAS_PASSWD=tavallinenvaimojuttu
export P4A_RELEASE_KEYALIAS=mykeyaliasname 
cd ~/git/Omat/speed 
buildozer -v android release

```