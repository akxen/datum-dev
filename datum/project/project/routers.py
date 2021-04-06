"""Database router"""


class CustomRouter:
    def db_for_read(self, model, **hints):
        """Reads go to reports database, all other models go to default"""

        if model._meta.app_label == 'reports':
            return 'data'

        return None

    def db_for_write(self, model, **hints):
        """Only writing to default database"""

        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the same database
        """

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Reports database is read-only"""

        # Reports database should be read-only
        if (db == 'data') or (app_label == 'reports'):
            return False

        return True
