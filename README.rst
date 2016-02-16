=======================
JinjaLive documentation
=======================

Welcome to JinjaLive documentation!

JinjaLive is a project created by Marlysys.

JinjaLive can be used to test your Jinja templates.
It renders a Jinja template with given variables to a rendered output. As simple as that !

.. contents::


Installation
============

JinjaLive is available on ``pip``:

.. code-block:: bash

    pip install jinjalive

Usage
=====

Command-line usage
------------------

Given a context file and a template file, JinjaLive will generate the output file:

.. code-block:: bash

    jinjalive -cf <context_file> -tf <template_file> -of <output_file>

Web application
---------------

Launch the JinjaLive server with:

.. code-block:: bash

    jinjalive-server

Open your browser to ``http://<your_ip_address>:8888``

Tests
=====

JinjaLive embeds unittests to ensure both functionnalities coverage but also Python code quality.

The test suite can be launched with ``tox``:

.. code-block:: bash

    cd jinjalive
    sudo pip install -r test-requirements.txt
    tox


Apache configuration (optional)
===============================

If you want to serve the JinjaLive web application behind Apache, please use WSGI.

.. code-block:: bash

    sudo apt-get update
    sudo apt-get install apache2 libapache2-mod-wsgi
    sudo a2enmod wsgi
    
Here is a sample Apache virtualhost:

.. code-block:: apacheconf

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

Your JinjaLive web application is now available under ``http://<your_ip_address>/jinja``.

Contributing
============

Requirements
------------

JinjaLive needs the following requirements:

- `Python <https://www.python.org/>`_.
- `Bower <http://bower.io/#install-bower>`_.

Nowadays, ``python`` should ever be present on your system, but ``bower`` usually requires proper installation.

``bower`` requires ``nodejs``. Here is the full procedure to install bower for Ubuntu:

.. code-block:: bash

    sudo apt-get update
    sudo apt-get install nodejs npm
    sudo npm install -g bower
    sudo ln -s /usr/bin/nodejs /usr/bin/node
    
Go to project directory:

.. code-block:: bash

    cd jinjalive

Install bower requirements:

.. code-block:: bash

    bower install

Install Python requirements and JinjaLive package with a virtualenv:

.. code-block:: bash

    mkvirtualenv jinjalive
    pip install -r requirements.txt
    python setup.py develop
    