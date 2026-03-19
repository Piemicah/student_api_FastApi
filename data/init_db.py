from data.database import get_sessionLocal
from models.models import Programme


def init():
    session = get_sessionLocal()

    try:
        result = session.query(Programme).all()
        if len(result) == 0:
            prog1 = Programme(id=1, programme_name="IJMBE")
            prog2 = Programme(id=2, programme_name="JUPEB")
            prog3 = Programme(id=3, programme_name="DIPLOMA")

            session.add(prog1)
            session.add(prog2)
            session.add(prog3)
            session.commit()
    finally:
        session.close()
