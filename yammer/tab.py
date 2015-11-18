from courseware.tabs import CourseTab


class YammerTab(CourseTab):
    """A new course tab."""

    name = "yammer"
    title = "Yammer"
    view_name = "yammer"
    tab_id = "yammer"
    priority = 50
    type = "yammer"

    @classmethod
    def is_enabled(cls, course, user=None):
        """Returns true if this tab is enabled."""
        return True

    @classmethod
    def validate(cls, tab_dict, raise_error=True):

        return True
