from data.database import get_sessionLocal
from models.models import Programme, Role


def init():
    session = get_sessionLocal()

    try:
        programmes = session.query(Programme).all()
        if len(programmes) == 0:
            prog1 = Programme(id=1, programme_name="IJMBE")
            prog2 = Programme(id=2, programme_name="JUPEB")
            prog3 = Programme(id=3, programme_name="DIPLOMA")

            session.add(prog1)
            session.add(prog2)
            session.add(prog3)
            session.commit()
        
        roles = session.query(Role).all()
        if len(roles) == 0:
            role1 = Role(name="admin")
            role2 = Role(name="staff")
            role3 = Role(name="student")

            session.add_all([role1,role2,role3])
            session.commit()
    finally:
        session.close()
