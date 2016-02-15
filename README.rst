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

    pip install -r requirements.txt
    python setup.py install

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

Open your browser to http://127.0.0.1:8888
Enjoy !
