from rimbot import database

class User(database.Model):
    __tablename__ = 'users'

    id          = database.Column(database.Integer, primary_key = True)
    username    = database.Column(database.String(128), unique = True, index = True)
    email       = database.Column(database.String(128), unique = True, index = True)
    password    = database.Column(database.String(128))
    plan        = database.Column(database.Integer, database.ForeignKey('plans.id'))

    def __repr__():
        return '<User %r>' % self.username

class Plan(database.Model):
    __tablename__ = 'plans'

    id          = database.Column(database.Integer, primary_key = True)
    name        = database.Column(database.String(128))
    description = database.Column(database.String(512))
    users       = database.relationship('User', backref = 'role')

    def __repr__():
        return '<Plan %r>' % self.name