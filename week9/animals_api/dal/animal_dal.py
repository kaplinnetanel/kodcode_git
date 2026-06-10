from database import get_connection
import logging

class Animal_DAL:
    def creat_animal(self, name,animal_typ,age):
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO animals(name, animal_type, age) VALUES(%s, %s, %s)"
        values = (name, animal_typ, age)
        cursor.execute(query, values)
        conn.commit()
        conn.close()
        cursor.close()

    def get_all_animals(self):
        conn = get_connection() 
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM animals")
        rows = cursor.fetchall()
        conn.close()
        cursor.close()
        return rows 

    def get_animal_by_id(self,animal_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary= True)
        cursor.execute("SELECT * FROM animals WHERE id = %s",(animal_id,))
        row = cursor.fetchone()
        conn.close()
        cursor.close()
        return row
    
    def update_animal(self,animal_id,name, animal_type, age):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE animals SET name = %s,animal_type=%s,age=%s WEHRE id = %s",(animal_id,name, animal_type, age))
        conn.commit()
        cursor.close()
        conn.close()
    
    def delete_animal(self,animal_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM animals WHERE id = %s",(animal_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return f"Animal by {animal_id} delete"
    