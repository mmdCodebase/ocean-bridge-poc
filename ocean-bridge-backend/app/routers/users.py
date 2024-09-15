from fastapi import APIRouter, Query, Depends, HTTPException, status
from datetime import datetime
from sqlalchemy.orm import Session, class_mapper
from db.database import get_db
from models.user import (
    Authentication,
    AuthenticationCreate,
    AuthenticationUpdate,
    AuthenticationToken,
    AuthenticationTokenCreate,
    AuthenticationTokenUpdate,
    AuthenticationRecoveryMFA
)

router = APIRouter(
    prefix="/authentication",
    tags=["authentication"],
    responses={404: {"description": "Not found"}},
)

@router.get("/user", status_code=status.HTTP_200_OK)
async def get_updated_users(
    updated_start_time: str = Query(..., description="Start time for user updates in ISO 8601 format"), 
    updated_end_time: str = Query(..., description="End time for user updates in ISO 8601 format"), 
    db: Session = Depends(get_db)
):
    """
    Endpoint to fetch updated_users based on provided date range.
    """
    try:
        start_time = datetime.fromisoformat(updated_start_time)
        end_time = datetime.fromisoformat(updated_end_time)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Please use ISO 8601 format.")

    updated_users = db.query(Authentication.entity_id).filter(Authentication.updated_at >= start_time, Authentication.updated_at <= end_time).all()
    return {"Status": "Success", "updated_users": [user.entity_id for user in updated_users]}

def serialize_instance(obj):
    """
    Serialize a SQLAlchemy object to a dictionary.
    """
    serialized = {}
    for column in class_mapper(obj.__class__).columns:
        value = getattr(obj, column.name)
        if isinstance(value, bytes):
            try:
                decoded_value = value.decode('utf-8')
            except UnicodeDecodeError:
                decoded_value = value.decode('latin1')
            serialized[column.name] = decoded_value
        else:
            serialized[column.name] = value
    return serialized

@router.get("/user/{entity_id}", status_code=status.HTTP_200_OK)
async def get_user(entity_id: str, db: Session = Depends(get_db)):
    """
    Endpoint to fetch user data based on provided entity ID, including related data from AuthenticationToken and AuthenticationRecoveryMFA tables.
    """
    user_data = db.query(Authentication).filter(Authentication.entity_id == entity_id).first()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    
    recovery_data = db.query(AuthenticationRecoveryMFA).filter(AuthenticationRecoveryMFA.entity_id == entity_id).all()
    token_data = db.query(AuthenticationToken).filter(AuthenticationToken.entity_id == entity_id).all()
    
    return {
        "Status": "Success",
        "user_data": serialize_instance(user_data),
        "recovery_data": [serialize_instance(recovery) for recovery in recovery_data],
        "auth_tokens": [serialize_instance(token) for token in token_data]
    }
    
@router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_authentication_user(authentication_user_data: AuthenticationCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new authentication record in the database.
    """
    try:
        authentication_user_db = Authentication(**dict(authentication_user_data))
        print("authntication", authentication_user_db)
        db.add(authentication_user_db)
        db.commit()
        db.refresh(authentication_user_db)
        return {"Status": "Success", "authentication_user_id": authentication_user_db.entity_id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create authentication user") from e
    
@router.patch("/user/{entity_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_authentication_user(entity_id: str, authentication_user_data: AuthenticationUpdate, db: Session = Depends(get_db)):
    """
    Endpoint to update authentication_user_data based on provided entity ID.
    """
    try:
        authentication_user_db = db.query(Authentication).filter(Authentication.entity_id == entity_id).first()
        if not authentication_user_db:
            raise HTTPException(status_code=404, detail="authentication_user_db not found")
        print(authentication_user_db)
        update_data = authentication_user_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(authentication_user_db, key, value)
        
        db.commit()
        return {"Status": "Success", "success": True}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to update authentication user") from e

@router.post("/token", status_code=status.HTTP_201_CREATED)
async def create_authentication_token(authentication_token_data: AuthenticationTokenCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new authentication token record in the database.
    """
    try:
        authentication_token_db = AuthenticationToken(**dict(authentication_token_data))
        db.add(authentication_token_db)
        db.commit()
        db.refresh(authentication_token_db)
        return {"Status": "Success", "authentication_token_id": authentication_token_db.authentication_token_id}
    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(status_code=500, detail="Failed to create authentication token") from e

@router.patch("/token/{authentication_token_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_authentication_token(authentication_token_id: str, authentication_token_data: AuthenticationTokenUpdate, db: Session = Depends(get_db)):
    """
    Endpoint to update authentication_token_data based on provided authentication_token ID.
    """
    try:
        authentication_token_db = db.query(AuthenticationToken).filter(AuthenticationToken.authentication_token_id == authentication_token_id).first()
        if not authentication_token_db:
            raise HTTPException(status_code=404, detail="authentication_token_db not found")
        
        update_data = authentication_token_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(authentication_token_db, key, value)
        
        db.commit()
        return {"Status": "Success", "success": True}
    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(status_code=500, detail="Failed to update authentication token") from e


