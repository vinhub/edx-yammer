from django.shortcuts import get_object_or_404, render_to_response
from rest_framework.generics import GenericAPIView


class YammerView(GenericAPIView):

    def get(self, request, course_id):

        print "inside yammer get"
        context = {}
        return render_to_response("yammer/yammer.html", context)
