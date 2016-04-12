This folder contains the nikola configuration and references for content and themes of c3w.at and is all you need to set up your local copy of the site.

Installation and documentation of nikola can be found at https://getnikola.com/


To initialize the content and theme git submodules use::

   git submodule init
   git submodule update

To build the site::

    nikola build

To see it::

    nikola serve -b

or to automatically rebuild the site on local changes use::

    nikola auto

To check all available commands::

    nikola help
