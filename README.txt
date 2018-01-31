This folder contains the nikola configuration and references for content and themes of c3w.at and is all you need to set up your local copy of the site.

Installation and documentation of nikola can be found at https://getnikola.com/


check out the content git repo::

   git clone git@github.com:c3wien/c3w.at-pages.git content

To build the site::

    nikola build

To see it::

    nikola serve -b

or to automatically rebuild the site on local changes use::

    nikola auto -b

