# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from collective.document_hide_summary.testing import COLLECTIVE_DOCUMENT_HIDE_SUMMARY_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.document_hide_summary is properly installed."""

    layer = COLLECTIVE_DOCUMENT_HIDE_SUMMARY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.document_hide_summary is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.document_hide_summary'))

    def test_browserlayer(self):
        """Test that ICollectiveDocumentViewNoDescriptionLayer is registered."""
        from collective.document_hide_summary.interfaces import (
            ICollectiveDocumentViewNoDescriptionLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveDocumentViewNoDescriptionLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_DOCUMENT_HIDE_SUMMARY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.document_hide_summary'])

    def test_product_uninstalled(self):
        """Test if collective.document_hide_summary is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.document_hide_summary'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveDocumentViewNoDescriptionLayer is removed."""
        from collective.document_hide_summary.interfaces import \
            ICollectiveDocumentViewNoDescriptionLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveDocumentViewNoDescriptionLayer, utils.registered_layers())
