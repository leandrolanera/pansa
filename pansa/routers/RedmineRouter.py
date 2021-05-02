class RedmineRouter(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on redmine models to 'redminedb'"
        if model._meta.app_label == 'gerente':
            return 'redminedb'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on redmine models to 'redminedb'"
        if model._meta.app_label == 'gerente':
            return 'redminedb'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in redmine app"
        if obj1._meta.app_label == 'gerente' and obj2._meta.app_label == 'gerente':
            return True
        # Allow if neither is redmine app
        elif 'gerente' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'redminedb' or model._meta.app_label == "gerente":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True