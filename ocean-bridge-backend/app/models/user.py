from datetime import datetime
from typing import Optional
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from pydantic import BaseModel, UUID4, Field
from db.database import Base

#SQL Alchemy models
class Authentication(Base):
    __tablename__ = 'authentication'
    __table_args__ = {'schema': 'OceanBridge.authapi'}

    entity_id = Column(UNIQUEIDENTIFIER, primary_key=True)
    contact_id = Column(UNIQUEIDENTIFIER)
    username = Column(String(255))
    user_secret_server_salt = Column(String(255))
    plaintext_password = Column(String(255))
    hashed_password = Column(String(255))
    is_active = Column(Boolean)
    password_updated_on = Column(DateTime)
    ottp_secret_key = Column(String(255))
    failed_login_attempts_since_last_login = Column(TINYINT)
    account_status_choice = Column(UNIQUEIDENTIFIER, nullable=True)
    two_factor_authentication_enabled = Column(Boolean)
    password_recovery_choice = Column(UNIQUEIDENTIFIER, nullable=True)
    second_factor_authentication_choice = Column(UNIQUEIDENTIFIER, nullable=True)
    account_lock_expiry = Column(DateTime)
    last_password_reset = Column(DateTime)
    force_password_change = Column(Boolean)
    user_is_super_admin = Column(Boolean)
    updated_at = Column(DateTime, nullable=False, onupdate=func.now())

    # Relationships
    authentication_tokens = relationship("AuthenticationToken", back_populates="authentication")
    recovery_mfa = relationship("AuthenticationRecoveryMFA", back_populates="authentication")

    def __repr__(self):
        return f"<Authentication(entity_id={self.entity_id})>"
    
class AuthenticationToken(Base):
    __tablename__ = 'authentication_token'
    __table_args__ = {'schema': 'OceanBridge.authapi'}

    authentication_token_id = Column(UNIQUEIDENTIFIER, primary_key=True)
    entity_id = Column(UNIQUEIDENTIFIER, ForeignKey('OceanBridge.authapi.authentication.entity_id'))
    ip_address = Column(String(15))
    browser = Column(String(50))
    os = Column(String(50))
    device_id = Column(String(50))
    is_active = Column(Boolean)
    access_token = Column(String(255))
    refresh_token = Column(String(255))
    access_token_expired_at = Column(TIMESTAMP(timezone=True), nullable=False)
    refresh_token_expired_at = Column(TIMESTAMP(timezone=True), nullable=False)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())
    last_login_date = Column(TIMESTAMP(timezone=True), nullable=False)

    # Relationships
    authentication = relationship("Authentication", back_populates="authentication_tokens")

    def __repr__(self):
        return f"<AuthenticationToken(authentication_token_id={self.authentication_token_id}, entity_id={self.entity_id}, ip_address={self.ip_address})>"
    
class AuthenticationRecoveryMFA(Base):
    __tablename__ = 'authentication_recovery_mfa'
    __table_args__ = {'schema': 'OceanBridge.authapi'}

    recovery_id = Column(UNIQUEIDENTIFIER, primary_key=True)
    entity_id = Column(UNIQUEIDENTIFIER, ForeignKey('OceanBridge.authapi.authentication.entity_id'))
    recovery_type_choice = Column(UNIQUEIDENTIFIER)
    recovery_key = Column(String(255))
    recovery_value = Column(String(255))

    # Relationships
    authentication = relationship("Authentication", back_populates="recovery_mfa")

    def __repr__(self):
        return f"<AuthenticationRecoveryMFA(recovery_id={self.recovery_id}, entity_id={self.entity_id}, recovery_key={self.recovery_key})>"
    
    
# Pydantic models
class AuthenticationBase(BaseModel):
    entity_id: UUID4 
    contact_id: UUID4
    username: str | None = None
    user_secret_server_salt: str | None = None
    plaintext_password: str | None = None
    hashed_password: str | None = None
    is_active: bool
    password_updated_on: datetime | None = None
    ottp_secret_key: str | None = None
    failed_login_attempts_since_last_login: int | None = None
    account_status_choice: UUID4 | None = None
    two_factor_authentication_enabled: bool
    password_recovery_choice: UUID4 | None = None
    second_factor_authentication_choice: UUID4 | None = None
    account_lock_expiry: datetime | None = None
    last_password_reset: datetime | None = None
    force_password_change: bool
    user_is_super_admin: bool
    updated_at: datetime | None = None

    class ConfigDict:
        from_attributes = True

class AuthenticationCreate(AuthenticationBase):
    pass

class AuthenticationUpdate(BaseModel):
    contact_id: UUID4
    username: str
    user_secret_server_salt: str
    plaintext_password: str
    hashed_password: str
    is_active: bool
    password_updated_on: datetime
    ottp_secret_key: str
    failed_login_attempts_since_last_login: int
    account_status_choice: UUID4
    two_factor_authentication_enabled: bool
    password_recovery_choice: UUID4
    second_factor_authentication_choice: UUID4
    account_lock_expiry: datetime
    last_password_reset: datetime
    force_password_change: bool 
    user_is_super_admin: bool
    updated_at: datetime

class AuthenticationTokenBase(BaseModel):
    authentication_token_id: UUID4
    entity_id: UUID4
    ip_address: str 
    browser: str
    os: str 
    device_id: str 
    is_active: bool
    access_token: str 
    refresh_token: str 
    access_token_expired_at: datetime 
    refresh_token_expired_at: datetime 
    deleted_at: Optional[datetime]
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    last_login_date: Optional[datetime] 

    class ConfigDict:
        from_attributes = True

class AuthenticationTokenCreate(AuthenticationTokenBase):
    pass

class AuthenticationTokenUpdate(BaseModel):
    entity_id: Optional[UUID4] = None
    ip_address: Optional[str] = None
    browser: Optional[str] = None
    os: Optional[str] = None
    device_id: Optional[str] = None
    is_active: Optional[bool] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    access_token_expired_at: Optional[datetime] = None
    refresh_token_expired_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    last_login_date: Optional[datetime] = None