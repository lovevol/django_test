from django.test import TestCase

# Create your tests here.
from app.tasks import task_test

task_test.delay()