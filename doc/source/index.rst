.. raw:: html

 <a href="https://github.com/futuregrid/teefaa"
     class="visible-desktop"><img
    style="position: absolute; top: 40px; right: 0; border: 0;"
    src="https://s3.amazonaws.com/github/ribbons/forkme_right_gray_6d6d6d.png"
    alt="Fork me on GitHub"></a>


Welcome to Cloudmesh Teefaa!
====================

.. sidebar:: Table of Contents

  .. toctree::
   :maxdepth: 2

   usersguide
   adminguide
   license


Cloudmesh Teefaa is a set of deployment scripts for system provisioning with 
focus on  baremetal provisioning. It is designed to be simple, flexible, programable. 

Requirements
------------------------

FG Teefaa requires:

* Python, version 2.7
* Python Modules

  - Fabric, version 1.6
  - Cuisine, version 0.6
  - PyYAML, version 3.10

* Squashfs-tools (for creating snapshots of Operating System)
* Bittorrent Sync (for high-speed multiple Baremetal Provisioning)
* Torque Resource Manager (for scheduing Baremetal Provisioning)

* System requirements
  - pxeboot
  - IPMI 


Simple Design
-------------

* Scripts for handling Shell commands are written in Fabric and Cuisine.
* Configuration files are written in YAML format, allowing the the configuration
  files to be readable.
* Each script is associated with four directories::

    |-- fabfile/EXAMPLE.py
    |-- ymlfile/EXAMPLE
    |           |-- config1.yml
    |           `-- config2.yml
    |-- private/EXAMPLE
    |           `-- dir1
    |               |-- file1
    |               `-- file2
    `-- share/EXAMPLE
              `-- dir1
                  |-- file1
                  `-- file2

This structure enables a simple separation and concurrent development. Hence, users 
can work on multile projects and multiple versions of teefaa. For example, 
while one person is developing EXAMPLE, another person can start developing EXAMPLE2.

Instalation
------------------------

The code can be downloaded from 

* https://github.com/futuregrid/teefa

The release version can be installed via::

    pip install futuregird-teefaa


Support
-------

If you run into problems, please use our 
help form at `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`_.
 
Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

