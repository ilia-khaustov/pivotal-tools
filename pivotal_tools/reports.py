import datetime


class PivotalReportGenerator(object):

    def __init__(self, pivotal_client):
        self.client = pivotal_client

    def weekly_dev(self, weeks_ago=0):
        report = '\n'
        
        me = self.client.me()
        
        today = datetime.datetime.now() - datetime.timedelta(weeks=weeks_ago)
        
        monday = today - datetime.timedelta(days=today.weekday())
        monday = monday.replace(hour=8, minute=0, second=0)

        friday = today + datetime.timedelta(days=(4-today.weekday()))
        friday = friday.replace(hour=20, minute=0, second=0)

        all_stories = self.client.get(
            'stories',
            updated_after=monday.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            updated_before=friday.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            fields="url,name,owner_ids"
        )
        report += 'Tasks owned by {}, updated after {} and before {}\n\n'.format(
            me['name'],
            monday.strftime("%Y-%m-%d %H:%M"),
            friday.strftime("%Y-%m-%d %H:%M"),
        )

        owned_stories = filter(lambda s: me['id'] in s['owner_ids'], all_stories)
        for s in owned_stories:
            report += s['url'] + '\n'
            report += s['name'] + '\n'
            report += '\n'

        return report[:-1]
