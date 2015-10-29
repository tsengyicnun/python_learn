admins = set()
users = {'Smile', 'Tony','Happy','Sherry','Allen','Andy', 'Mars'}
admins.add('ihc')
admins.add('Mars')
admins.add('Tony')


print admins & users
print admins | users
print admins ^ users
print admins - users   
print users - admins   