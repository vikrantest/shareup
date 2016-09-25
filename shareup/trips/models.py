import os
import uuid
import time
from datetime import datetime

from django.db import models

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q, Sum
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.conf import settings as my_settings
from django.core.exceptions import *
from common.utils import *
from common.models import Basetable
from mongoengine import *




class Trips(Document):
	trip_id = StringField(max_length=50,null=True,blank=True)
	glob_trip_id = StringField(max_length=50,null=True,blank=True)
	trip_account =  ReferenceField('BookingAccounts', null=True,blank=True)
	address_details =  ReferenceField('Locations', null=True,blank=True)
	address_meta_text = StringField(null=True,blank=True)
	package_meta_data = StringField(null=True,blank=True)
	start_time = IntField()
	duration = StringField(max_length=500,null=True,blank=True)
	customer = ReferenceField('Customer', null=True,blank=True)


	def __unicode__(self):
		return self.trip_id
