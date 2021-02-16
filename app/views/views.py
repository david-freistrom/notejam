from flask import current_app
from datetime import date

@current_app.template_filter('smart_date')
def smart_date_filter(updated_at):
    delta = date.today() - updated_at.date()
    if delta.days == 0:
        return 'Today at {}'.format(updated_at.strftime("%H:%M"))
    elif delta.days == 1:
        return 'Yesterday at {}'.format(updated_at.strftime("%H:%M"))
    elif 1 > delta.days > 4:
        return '{} days ago'.format(abs(delta.days))
    else:
        return updated_at.date()





