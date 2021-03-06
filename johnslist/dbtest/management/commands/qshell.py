from django.core.management.base import BaseCommand, CommandError
from django.core.management import execute_from_command_line
import code
from django.test import Client

class Command(BaseCommand):
    help = "Imports models and guardian for testing. Also stores a user instance 'u', organization 'o', category 'c', and group 'g' for testing purposes."
    def handle(self, *args, **options):
        from guardian.shortcuts import assign_perm
        from dbtest.models import *
        import unittest
        from django.test import Client
        from notifications.signals import notify
        from notifications.models import Notification
        from django.core.urlresolvers import reverse
        from guardian.shortcuts import get_objects_for_user,assign_perm,remove_perm,get_perms
        from guardian.core import ObjectPermissionChecker

        pu = User.objects.get(id=1)
        cp = User.objects.get(id=2)
        u0 = pu
        u1 = cp
        client = Client()
        o = Organization.objects.get(id=1)
        j = Job.objects.get(id=1)
        jr = JobRequest.objects.get(id=1)
        c = Category.objects.get(id=2)
        g = Group.objects.get(id=1)
        # n = Notification.objects.get(id=1)
        code.interact(local=locals())

