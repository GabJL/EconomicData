from database import *
from sqlalchemy.orm import sessionmaker


def get_amount_locations(session):
    return session.query(Location).count()


def get_series_without_data(session):
    series = session.query(Serie).filter()
    result = []
    for s in series:
        codes = int(session.query(Code).filter(Code.serie_id == s.id).count())
        if codes == 0:
            result.append(s.name)
    return result


def get_series_without_data_for_all_locations(session, number):
    series = session.query(Serie).filter()
    result = []
    for s in series:
        codes = int(session.query(Code).filter(Code.serie_id == s.id).count())
        if codes > 0 and codes < number:
            result.append(s.name)
    return result


def get_adequate_series(session, number):
    series = session.query(Serie).filter()
    result = []
    for s in series:
        codes = int(session.query(Code).filter(Code.serie_id == s.id).count())
        if codes == number:
            result.append(s)
    return result



def print_list(text, l):
    if not l:
        print(f"{text}: None")
    else:
        print(f"{text}:")
        for s in l:
            print(f"\t{s}")

if __name__ == '__main__':
    engine = createDB()
    Session = sessionmaker(bind=engine)
    session = Session()

    nlocations = get_amount_locations(session)

    res = get_series_without_data(session)
    print_list("Series without data", res)
    res = get_series_without_data_for_all_locations(session, nlocations)
    print_list("Series without data for all the locations", res)

    series =get_adequate_series(session, nlocations)
    print_list("Considered series", [n.name for n in series])