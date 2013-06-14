#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import sys
from fabric.api import *
from fabric.contrib import *
from cuisine import *

def env_tfutils():
    env.use_ssh_config = True
    env.user = 'root'

@task
def install_pdsh():
    '''Installs Parallel Distributed Shell'''
    env_tfutils()
    if dir_exists('/opt/pdsh-2.26'):
        print 'pdsh-2.26 is already installed.'
        exit(1)
    #package_update()
    #select_package('apt')
    package_ensure('build-essential')
    dir_ensure('/root/source')
    with cd('/root/source'):
        run('wget http://pdsh.googlecode.com/files/pdsh-2.26.tar.bz2')
        run('tar jxvf pdsh-2.26.tar.bz2')
    with cd('/root/source/pdsh-2.26'):
        run('./configure --prefix=/opt/pdsh-2.26 \
                         --without-rsh --with-ssh \
                         --with-dshgroups=/opt/pdsh-2.26/dshgroups')
        run('make')
        run('make install')
    with cd('/root'):
        file_append('.bashrc', 'export PATH=/opt/pdsh-2.26/bin:$PATH')
