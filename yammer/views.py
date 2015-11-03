from django.shortcuts import render_to_response
from rest_framework.generics import GenericAPIView


class YammerTabView(GenericAPIView):

    def get(self, request, course_id):

        context = {}

        return render_to_response("yammer/yammer.html", context)

