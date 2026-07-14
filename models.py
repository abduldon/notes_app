from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):
    id = db.column(db.Integer, primary_key=true)
    username = db.column(db.string(80), unique=True, nullable = False)
    email = db.column(db.String(120), unique = True, nullable = False)
    password = db.column(db.string(120, unique = True, nullable = False))

    # Relationship to the Note model
    notes = db.relationship(
        'Note',
        backref='user',
        lazy=True,
        cascade='all, delete'
    )

class Note(db.Model):
    __tablename__ = 'notes'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    discription = db.Column(db.Text, nullable=False)  # Note: Spelled 'discription' on the slide
    
    # Foreign key linking to the User model
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'discription': self.discription,
            'user_id': self.user_id
        }