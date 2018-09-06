# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from tastypie import fields
from tastypie.resources import ModelResource, ALL

from . import models


class DepartmentResource(ModelResource):
    class Meta:
        queryset = models.Department.objects.using("int").all()
        resource_name = "departments"
        allowed_methods = ("get",)
        include_resource_uri = False
        max_limit = None
        filtering = {"id": ALL, "name": ALL}

    def dehydrate_id(self, bundle):
        return bundle.data["id"].strip()

    def dehydrate_name(self, bundle):
        return bundle.data["name"].strip().title()


class EmployeeResource(ModelResource):

    department = fields.ForeignKey(DepartmentResource, "department", full=True, null=True)

    class Meta:
        queryset = models.Employee.objects.using("rh").select_related("department")
        resource_name = "employees"
        allowed_methods = ("get",)
        include_resource_uri = False
        max_limit = None
        filtering = {"cid": ALL, "name": ALL, "surname1": ALL, "surname2": ALL}

    def dehydrate_name(self, bundle):
        return bundle.data["name"].title()

    def dehydrate_surname1(self, bundle):
        return bundle.data["surname1"].title()

    def dehydrate_surname2(self, bundle):
        return bundle.data["surname2"].title()

    def dehydrate_id(self, bundle):
        return bundle.data["id"].strip()

    def dehydrate_fid(self, bundle):
        return bundle.data["fid"].strip()

    def dehydrate_cid(self, bundle):
        return bundle.data["cid"].strip()
