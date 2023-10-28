from fastapi import HTTPException

from backend.src.core.shemas.users import User


def get_user(db, user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
