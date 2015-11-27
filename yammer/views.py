from edxmako.shortcuts import render_to_response
from edxmako.paths import add_lookup, lookup_template
from rest_framework.generics import GenericAPIView
from opaque_keys.edx.keys import CourseKey
from courseware.courses import get_course_with_access


class YammerView(GenericAPIView):

    def get(self, request, course_id):

        course_key = CourseKey.from_string(course_id)
        course = get_course_with_access(request.user, "load", course_key)
        user = request.user
        add_lookup('main', '/edx/app/edxapp/edx-platform/lms/djangoapps/yammer/templates')
        context = {
            "course": course,
            "user_info": {
                "username": user.username,
            },
            "user": user
        }
        return render_to_response("yammer/yammer.html", context, {}, "main")
