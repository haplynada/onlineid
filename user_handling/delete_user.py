'''
Created on Nov 2, 2017
 
@author: Bjarke Larsen
'''
from database_handling.connect import Connect
 
def delete_user(user_id):
    """Deletes all data stored about a user in the database.

        The function connects to the database, the curser execute the query.

        Args:
            user_id: An generated number from the database, which is a primary-key in the databse. It is unique to
                each user and intended to be used for look-up.
            ex: "1"

        Returns:
            None
        """
    with Connect() as db: 
        query = "DELETE FROM information WHERE user_id = %s;"
        db.cur.execute(query, (user_id,))
        db.conn.commit()
        return True