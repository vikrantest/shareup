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




class BookingAccounts(Document):
	name = StringField(max_length=50,null=True,blank=True)
	useremail = EmailField(max_length=50,null=True,blank=True)
	phone_number = IntField()
	password = StringField(max_length=500,null=True,blank=True)
	address = ReferenceField('Locations', null=True,blank=True)



class Customer(Document):
	name = StringField(max_length=50,null=True,blank=True)
	useremail = EmailField(max_length=50,null=True,blank=True)
	phone_number = IntField()
	password = StringField(max_length=500,null=True,blank=True)
	address = ReferenceField('Locations', null=True,blank=True)
