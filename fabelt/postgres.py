from fabric.api import cd, sudo, task

from fabelt import apt


@task()
def install():
    apt.install('postgresql')
    apt.install('libpq-dev')


@task()
def create_database(name, owner=None):
    if owner:
        cmd = 'createdb {name} --owner {owner}'.format(name=name, owner=owner)
    else:
        cmd = 'createdb {name}'.format(name=name)

    with cd('~postgres'):
        sudo(cmd, user='postgres')


@task()
def drop_database(name):
    with cd('~postgres'):
        sudo('dropdb {name}'.format(name=name), user='postgres')


@task()
def create_user(username):
	with cd('~postgres'):
		sudo('createuser {username} -P'.format(username=username),
			 user='postgres')


@task()
def drop_user(username):
	with cd('~postgres'):
		sudo('dropuser {username}'.format(username=username),
			 user='postgres')
