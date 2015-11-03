from courseware.tabs import EnrolledTab
from django.utils.translation import ugettext_noop
from django.conf import settings


class YammerTab(EnrolledTab):
    """A new course tab."""

    name = "yammer"
    title = ugettext_noop("Yammer")
    view_name = "yammer_tab"
    is_default = True
    is_hideable = True

    @classmethod
    def is_enabled(cls, course, user=None):
        """Returns true if this tab is enabled."""
        return True
