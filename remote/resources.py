# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from tastypie import fields
from tastypie.resources import ModelResource, ALL

from . import models


class AreaResource(ModelResource):
    class Meta:
        queryset = models.Area.objects.using("int").all()
        resource_name = "areas"
        allowed_methods = ("get",)
        include_resource_uri = False
        max_limit = None
        filtering = {"id": ALL, "name": ALL}

    def dehydrate_id(self, bundle):
        return bundle.data["id"].strip()

    def dehydrate_name(self, bundle):
        return bundle.data["name"].strip().upper()


class DepartmentResource(ModelResource):
    class Meta:
        queryset = models.Department.objects.using("rh").all()
        resource_name = "departments"
        allowed_methods = ("get",)
        include_resource_uri = False
        filtering = {"id": ALL, "name": ALL}

    def dehydrate_id(self, bundle):
        return bundle.data["id"].strip()

    def dehydrate_name(self, bundle):
        return bundle.data["name"].strip().upper()


class CategoryResource(ModelResource):
    class Meta:
        queryset = models.Category.objects.using("rh").all()
        resource_name = "categories"
        allowed_methods = ("get",)
        include_resource_uri = False
        filtering = {"id": ALL, "desc_category_di": ALL}

    def dehydrate_id(self, bundle):
        return bundle.data["id"].strip()

    def dehydrate_description(self, bundle):
        return bundle.data["description"].upper()


class SpecialtyResource(ModelResource):
    class Meta:
        queryset = models.Specialty.objects.using("rh").all()
        resource_name = "specialties"
        allowed_methods = ("get",)
        include_resource_uri = False
        filtering = {"id": ALL, "name": ALL}

    def dehydrate_id(self, bundle):
        return bundle.data["id"].strip()

    def dehydrate_name(self, bundle):
        return bundle.data["name"].upper()


class ProfessionResource(ModelResource):

    specialty = fields.ForeignKey(SpecialtyResource, "specialty", full=True, null=True)

    class Meta:
        queryset = models.Profession.objects.using("rh").select_related("specialty")
        resource_name = "professions"
        allowed_methods = ("get",)
        include_resource_uri = False
        filtering = {"id": ALL, "name": ALL}

    def dehydrate_id(self, bundle):
        return bundle.data["id"].strip()

    def dehydrate_name(self, bundle):
        return bundle.data["name"].upper()


class PositionResource(ModelResource):
    class Meta:
        queryset = models.Position.objects.using("rh").all()
        resource_name = "positions"
        allowed_methods = ("get",)
        include_resource_uri = False
        filtering = {"id": ALL, "name": ALL}

    def dehydrate_id(self, bundle):
        return bundle.data["id"].strip()

    def dehydrate_name(self, bundle):
        return bundle.data["name"].upper()


class EmployeeResource(ModelResource):

    area = fields.ForeignKey(AreaResource, "area", full=True, null=True)
    department = fields.ForeignKey(DepartmentResource, "department", full=True, null=True)

    category = fields.ForeignKey(CategoryResource, "category", full=True, null=True)
    position = fields.ForeignKey(PositionResource, "position", full=True, null=True)
    profession = fields.ForeignKey(ProfessionResource, "profession", full=True, null=True)

    class Meta:
        queryset = models.Employee.objects.using("rh").select_related(
            "area", "department", "category", "position", "profession", "profession__specialty"
        )
        resource_name = "employees"
        allowed_methods = ("get",)
        include_resource_uri = False
        filtering = {"cid": ALL, "name": ALL, "surname1": ALL, "surname2": ALL}

    def dehydrate_name(self, bundle):
        return bundle.data["name"].upper()

    def dehydrate_surname1(self, bundle):
        return bundle.data["surname1"].upper()

    def dehydrate_surname2(self, bundle):
        return bundle.data["surname2"].upper()

    def dehydrate_id(self, bundle):
        return bundle.data["id"].strip()

    def dehydrate_fid(self, bundle):
        return bundle.data["fid"].strip()

    def dehydrate_cid(self, bundle):
        return bundle.data["cid"].strip()

    def dehydrate_address(self, bundle):
        return bundle.data["address"].strip()

    def dehydrate_city(self, bundle):
        return bundle.data["city"].strip()

    def dehydrate_region(self, bundle):
        return bundle.data["region"].strip()

    def dehydrate_postal_code(self, bundle):
        return bundle.data["postal_code"].strip()

    def dehydrate_country(self, bundle):
        return bundle.data["country"].strip()
