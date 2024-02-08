from .models import CustomUser
import logging
from datetime import datetime

logger = logging.getLogger( __name__ )


def remove_unverified_users():
    
    print("crojob called")
    logger.info("\n----------------------------------------------------------------")
    logger.info("Cron job called at: %s", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    users = CustomUser.objects.filter(is_verified = False)

    print("List of users removed :\n", users)
    logger.info("List of users removed :")
    logger.info(str(list(users)))
    users.delete()
   