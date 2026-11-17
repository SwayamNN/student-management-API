
from env.database import engine, Base
from env.models import Student

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")
