from django.contrib.staticfiles.apps import StaticFilesConfig


class MyStaticFilesConfig(StaticFilesConfig):
    ignore_patterns = ['CVS', '.*', '*~', 'bootstrap-datetimepicker-standalone.css']
