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
from mongoengine import *




class Basetable(Document):
	obj_key = StringField(max_length=32, unique=True, blank=True)
	deleted_on = IntField(null=True, blank=True)
	created_on = IntField()
	updated_on = IntField()
	meta = {'allow_inheritance': True}

	class Meta:
		abstract = True

	def save(self, *args, **kwargs):
		self.updated_on = local_unixtime()
		if not self.created_on:
			self.created_on = local_unixtime()
		

		if not self.obj_key:
			self.obj_key = generate_random_alphanumeric(16)
			success = False
			failures = 0
			while not success:
				try:
					super(Basetable, self).save(*args, **kwargs)
				except IntegrityError:
					failures += 1
					if failures > 15: # or some other arbitrary cutoff point at which things are clearly wrong
						raise
					else:
						# looks like a collision, try another random value
						self.obj_key = generate_random_alphanumeric(16)
				else:
					 success = True
		else:
			super(Basetable, self).save(*args, **kwargs)

	def get_created_on(self):
		return self.created_on

	def get_updated_on(self):
		return self.updated_on

	def get_deleted_on(self):
		return self.deleted_on







class Location(Basetable):
	loc_name = StringField(max_length=500,null=True,blank=True)
	address1 = StringField(max_length=500,null=True,blank=True)
	address2 = StringField(max_length=500,null=True,blank=True)
	city = StringField(max_length=100,null=True, blank=True)
	state = StringField(max_length=100, null=True,blank=True)
	country = StringField(max_length=100,null=True, blank=True)
	zip_code = StringField(max_length=16,null=True)
	laitudet = FloatField(null=True,blank=True)
	longitude = FloatField(null=True,blank=True)
	coordinates = PointField()
	zoom = IntField(null=True)
	resolved = BooleanField(default=False)
	raw = StringField(max_length=10000,null=True,blank=True)

	
	def __unicode__(self):
		return self.address1 or ''

	def get_address_text(self):

		short_address = self.venue
		long_address = self.venue
		return {'short_address': short_address, 'long_address': long_address}





