# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from tastypie.resources import ModelResource, ALL

from . import models


class EmployeeResource(ModelResource):

    class Meta:
        queryset = models.Employee.objects.using('rh').all()
        resource_name = 'employees'
        allowed_methods = ('get',)
        include_resource_uri = False
        filtering = {
            'cid': ALL,
            'name': ALL,
            'surname1': ALL,
            'surname2': ALL,
        }

    def dehydrate_name(self, bundle):
        return bundle.data['name'].title()

    def dehydrate_surname1(self, bundle):
        return bundle.data['surname1'].title()

    def dehydrate_surname2(self, bundle):
        return bundle.data['surname2'].title()

    def dehydrate_eid(self, bundle):
        return bundle.data['eid'].strip()

    def dehydrate_fid(self, bundle):
        return bundle.data['fid'].strip()

    def dehydrate_uid(self, bundle):
        return bundle.data['uid'].strip()
