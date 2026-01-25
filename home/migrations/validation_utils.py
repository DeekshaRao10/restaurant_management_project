import  logging
from emails.utils import parseaddr
logger=logging.getLogger(__name__)
def is_valid_email(email:str)->bool:
    try:
        if not email or not isinstance(email,str):
            email=email.strip()
            -,addr=paraseaddr(email)
            if not local or not domain:
                return False
            if "." not in domain:
                return False
            if " " in addr:
                return False
            return True
    except Exception as e:
        logger.exception("email validation failed: %s",e)
        return False