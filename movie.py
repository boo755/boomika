director = Column(String)
    release_year = Column(Integer)from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the base class
Base = declarative_base()

# Define the Movie class
class Movie(Base):
    _tablename_ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)

# Create an SQLite engine and a session
engine = create_engine('sqlite:///yourdatabase.db')  # Use your database URI
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create Movie instances
movie1 = Movie(title="goat", director="venkatprabhu", release_year=2024, genre="action")
movie2 = Movie(title="leo", director="loki", release_year=2023, genre="action")
movie3 = Movie(title="hridhayam", director="mani", release_year=2022, genre="comedy")

# Add movies to the session and commit
session.add_all([movie1, movie2, movie3])
session.commit()

# Query all movies from the database
movies = session.query(Movie).all()

# Print movie details.
for movie in movies:
    print(movie.title, movie.director, movie.release_year, movie.genre)