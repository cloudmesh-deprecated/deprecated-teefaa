Make a snapshot of a remote system
============

Prerequisites
------------

* SSH Login to the remote system.
* Sudo on the remote system.
* 130~140% of system size for /tmp to process the snapshot creation. 
  You can check the size df command.::

       df -h

       Filesystem      Size  Used Avail Use% Mounted on
       /dev/sda2       9.2G  2.1G  6.7G  24% /
       udev            237M  4.0K  237M   1% /dev
       tmpfs            99M  220K   99M   1% /run
       none            5.0M     0  5.0M   0% /run/lock
       none            246M     0  246M   0% /run/shm

  In this example, system size is 2.1G. The /tmp is a part of 
  root(/) partition. Meaning there needs to be 2.1*140/100 = 2.94G 
  available on the same partition /dev/sda2.


Write Teefaafile.yml
--------------------

Create a directory for teefaa and write Teefaafile.yml.
This example is for a machine named host1 which is 
running Ubuntu-12.04 LTS.::

     mkdir -p teefaa/host1
     cd teefaa/host1
     vi Teefaafile.yml

::

     # Teefaafile.yml

     snapshot_config:
       hostname: host1
       snapshot_path: .teefaa/host1-2014-01-20.squashfs
       os:
         distro: ubuntu
         ver: 12.04

     ssh_config: .teefaa/ssh_config
     
And then, Write ssh_config::

     mkdir .teefaa
     vi .teefaa/ssh_config
     
::

     Host host1
       Hostname <ip address>
       User <username>
       UserKnownHostsFile /dev/null
       StrictHostKeyChecking no
       PasswordAuthentication no
       IdentityFile <path to ssh private key>
       IdentitiesOnly yes
       LogLevel FATAL

Execute teefaa make-snapshot. ::

     teefaa make-snapshot

It will take a while to finish this.

Notes about the system size
---------------------------
As you can see, Teefaa uses ssh and transfer the system image over the network. 
If your system is big, it will take very long. We strongly recommend you 
sepalately have your large data on a different partition and save/transfer 
data in another way.

If you have large data and want to exclude the directories, you can exclude them by
adding exclude option on the Teefaafile.yml like this. ::

     snapshot_config:
       hostname: host1
       snapshot_path: .teefaa/host1-2014-01-20.squashfs
       os:
         distro: ubuntu
         ver: 12.04
       exclude:
         - /path/to/large/dir1
         - /path/to/large/dir2


