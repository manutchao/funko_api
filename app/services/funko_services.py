from app import mongo
from app.models.funko_model import Funko

def get_funkos(page=1, per_page=10):
    """Récupère les Funkos avec pagination."""
    skip = (page - 1) * per_page
    funko_docs = list(mongo.db.funko_pop.find({}, {'_id': 0}).skip(skip).limit(per_page))

    # Convertir chaque document MongoDB en objet Funko
    funkos = [Funko.from_dict(doc).to_dict() for doc in funko_docs]

    print()
    print()
    print(funko_docs)
    print()
    print()
    print()
    total_count = mongo.db.funko_pop.count_documents({})

    return {
        "data": funkos,
        "pagination": {
            "current_page": page,
            "per_page": per_page,
            "total_count": total_count,
            "total_pages": (total_count // per_page) + (1 if total_count % per_page else 0)
        }
    }