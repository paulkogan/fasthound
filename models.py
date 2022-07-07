from sqlalchemy import Column, DateTime, Text, Integer

# from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.orm import declarative_base


# sqlAlchemy Classes
base_cls = declarative_base()


class EngSelect(base_cls):
    __tablename__ = "energizers"

    # id: Mapped[UUID] = Column(PostgresUUID(as_uuid=True), primary_key=True)
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(Text)
    last_name = Column(Text)
    occupation = Column(Text)
    wiki_page = Column(Text)
    born_state = Column(Text)
    born_town = Column(Text)
    home_state = Column(Text)
    home_town = Column(Text)
    current_town = Column(Text)
    current_state = Column(Text)


class EngCreateInitial(base_cls):
    __tablename__ = "energizers"
    __table_args__ = {"extend_existing": True}

    first_name = Column(Text)
    last_name = Column(Text)
    occupation = Column(Text)
    wiki_page = Column(Text)


class Energizer(base_cls):
    __tablename__ = "energizers"
    __table_args__ = {"extend_existing": True}

    # id: Mapped[UUID] = Column(PostgresUUID(as_uuid=True), primary_key=True)
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(Text)
    last_name = Column(Text)
    occupation = Column(Text)
    wiki_page = Column(Text)
    born_state = Column(Text)
    born_town = Column(Text)
    home_state = Column(Text)
    home_town = Column(Text)
    bio = Column(Text)
    education = Column(Text)
    early_life = Column(Text)
    current_town = Column(Text)
    current_state = Column(Text)
    ethnicity = Column(Text)
    gender = Column(Text)
    plays_with = Column(Text)
    rep_1 = Column(Text)
    rep_2 = Column(Text)
    middle_name = Column(Text)
    home_zipcode = Column(Integer)
    high_school = Column(Text)
    imdb_link = Column(Text)
    social_1 = Column(Text)
    social_2 = Column(Text)
    social_3 = Column(Text)
    birthday = Column(Text)
    solicitor = Column(Text)
    stat_1 = Column(Text)
    stat_2 = Column(Text)
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True))
