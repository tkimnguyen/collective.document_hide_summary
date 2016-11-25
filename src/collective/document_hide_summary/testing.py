# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.document_hide_summary


class CollectiveDocumentViewNoDescriptionLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.document_hide_summary)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.document_hide_summary:default')


COLLECTIVE_DOCUMENT_HIDE_SUMMARY_FIXTURE = CollectiveDocumentViewNoDescriptionLayer()


COLLECTIVE_DOCUMENT_HIDE_SUMMARY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_DOCUMENT_HIDE_SUMMARY_FIXTURE,),
    name='CollectiveDocumentViewNoDescriptionLayer:IntegrationTesting'
)


COLLECTIVE_DOCUMENT_HIDE_SUMMARY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_DOCUMENT_HIDE_SUMMARY_FIXTURE,),
    name='CollectiveDocumentViewNoDescriptionLayer:FunctionalTesting'
)


COLLECTIVE_DOCUMENT_HIDE_SUMMARY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_DOCUMENT_HIDE_SUMMARY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveDocumentViewNoDescriptionLayer:AcceptanceTesting'
)
