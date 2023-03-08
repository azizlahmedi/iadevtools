from django.db import migrations
from neoxam.backport import consts

def expand_timespan(apps, schema_editor):

    Record = apps.get_model('backport', 'Record')
    Commit = apps.get_model('adltrack', 'Commit')
    for record in Record.objects.filter(backported=False):
        from_version = record.from_version
        to_version = record.to_version
        commit = record.commit
        new_path = commit.path.replace(from_version, to_version)
        if Commit.objects.filter(path=new_path,
                                username=commit.username,
                                commit_date__gt=(commit.commit_date - consts.FILTERING_THRESHOLD),
                                commit_date__lt=(commit.commit_date + consts.FILTERING_THRESHOLD)):
            record.backported = True
            record.save(update_fields=('backported',))

class Migration(migrations.Migration):

    dependencies = [
        ('backport', '0002_remove_java_commit'),
    ]

    operations = [
        migrations.RunPython(expand_timespan)
    ]
