.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.document_hide_summary
==============================================================================

Adds a Document view template that hides the summary (description).

Features
--------

- uninstalls cleanly



Documentation
-------------

After you activate this add-on, every page ("Document" content type)
on your site will have a new Display menu choice "Hide Summary".


Translations
------------

This product has not been translated.



Installation
------------

Install collective.document_hide_summary by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.document_hide_summary


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.document_hide_summary/issues
- Source Code: https://github.com/collective/collective.document_hide_summary



License
-------

The project is licensed under the GPLv2.
