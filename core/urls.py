# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

from tastypie.api import Api

from remote import resources

v1_api = Api(api_name="v1")

v1_api.register(resources.EmployeeResource())
v1_api.register(resources.AreaResource())
v1_api.register(resources.DepartmentResource())
v1_api.register(resources.PositionResource())
v1_api.register(resources.CategoryResource())
v1_api.register(resources.ProfessionResource())
v1_api.register(resources.SpecialtyResource())

urlpatterns = [url(r"^api/", include(v1_api.urls))]
