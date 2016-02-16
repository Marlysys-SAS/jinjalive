========================
Jinja Live documentation
========================

Welcome to Jinja Live documentation!

Jinja Live (jinjalive v0.1.0) is a project created by Marlysys.

JinjaLive can be used to test your Jinja templates.
It renders a Jinja template with given variables to a rendered output. As simple as that !

Requirements
============

- `Python <https://www.python.org/>`_.
- `Bower <http://bower.io/#install-bower>`_.

``python`` should be present on your system, but ``bower`` requires ``nodejs``.
Here is the full procedure to install bower for Ubuntu:

.. code-block:: shell

    sudo apt-get update
    sudo apt-get install nodejs npm
    sudo npm install -g bower
    sudo ln -s /usr/bin/nodejs /usr/bin/node
    
Installation
============

Go to project directory:

.. code-block:: shell

    cd jinjalive

Install bower requirements:

.. code-block:: shell

    bower install

Install Python requirements and jinjalive package:

.. code-block:: shell

    sudo pip install -r requirements.txt
    sudo python setup.py build
    sudo python setup.py install

.. note::

    If you want to host the Jinjalive web application behind Apache, please use WSGI.
    
    .. code-block:: shell

        sudo apt-get update
        sudo apt-get install apache2 libapache2-mod-wsgi
        sudo a2enmod wsgi
        
    Here is a sample Apache virtualhost:
    
    .. code-block:: xml

        <VirtualHost *:80>
    
            WSGIDaemonProcess jinjalive threads=5
            WSGIScriptAlias /jinja /usr/local/lib/python2.7/dist-packages/jinjalive/jinjalive.wsgi
        
            <Directory /usr/local/lib/python2.7/dist-packages/jinjalive>
                WSGIProcessGroup jinjalive
                WSGIApplicationGroup %{GLOBAL}
                WSGIScriptReloading On
                Require all granted
            </Directory>
        
            ErrorLog ${APACHE_LOG_DIR}/jinjalive.error.log
            CustomLog ${APACHE_LOG_DIR}/jinjalive.access.log combined
        
        </VirtualHost>
        
Test your installation:

.. code-block:: shell

    cd tools/test
    ./00_test_all.sh

Command-line usage
==================

Given a context file and a template file, jinjalive will generate the output file:

.. code-block:: shell

    jinjalive -cf <context_file> -tf <template_file> -of <output_file>

Web application
===============

Launch the server with:

.. code-block:: shell

    jinjalive-server

Open your browser to http://<your_ip_address>:8888
Enjoy !
