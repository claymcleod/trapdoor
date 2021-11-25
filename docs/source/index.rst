Trapdoor Documentation
======================

Trapdoor is billed as a "turn-key configuration file management for Python packages".
It's intended to be a simple, plug-and-play system for creating, manipulating, and
reading configuration for your Python command line tool. Because the project values
simplicity, not all use-cases will be implemented.

Getting Started
---------------

The simplest usage of Trapdoor is just to initialize a Trapdoor instance with a 
store name (here, we use "trapdoor-test", which will create a config file at
:code:`~/.trapdoor-test/config.toml`).

.. code-block:: python

   from trapdoor import Trapdoor

   t = Trapdoor('trapdoor-test')
   t.set('some.nested.key.hello', 'world')

This will create a configuration TOML file at :code:`~/.trapdoor-test/config.toml` with
the following contents:

.. code:: toml

   [meta]
   created-at = 2021-11-22T23:30:58.762331
   updated-at = 2021-11-22T23:30:59.252702

   [some.nested.key]
   hello = "world"


.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`