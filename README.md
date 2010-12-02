How To Install
--------------

Using Virtualenv
================

Checkout the source, then do the following from the top most source directory:

    virtualenv env
    env/bin/python setup.py develop

Now you can run script from `env/bin/towxr`:

    env/bin/towxr -i input.csv -o output.wxr

Using Buildout
==============

Checkout the source and change into the repo directory

    buildout init
    buildout

Now you can run the script from `bin/towxr`

    bin/towxr -i input.csv -o output.wxr
