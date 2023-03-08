from django.db import migrations

def filter_all_java_commits(apps, schema_editor):

    Record = apps.get_model('backport', 'Record')
    for record in Record.objects.filter(commit__path__endswith='.java'):
        record.backported = True
        record.save(update_fields=('backported',))

class Migration(migrations.Migration):

    dependencies = [
        ('backport', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(filter_all_java_commits)
    ]