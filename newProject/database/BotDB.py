import psycopg2
from newProject.user.User import UserOB
from newProject.food.FoodClass import Food
from psycopg2.errors import SyntaxError

class Botdb:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="ec2-44-194-117-205.compute-1.amazonaws.com",
            database="dajf4n97l9f9cn",
            user="pkngmkhjfnvmhi",
            password="0a3fac6e67f9f29946adc77db24c903c4a5f25eead251702bb96ff6e0d79b870"
        )

    async def delete_from_base(self, user_id: int):
        query = f"""
        DELETE FROM books WHERE user_id = {user_id}
        """
        await self.write_to_base(query)

    async def get_food(self, name):
        query = f"""
        SELECT * FROM foods_table WHERE id = '{name}' 
        """
        food = await self.read_from_base(query)
        food = list(food[0])
                   # id      name    cost   category  photo   status
        return Food(food[0],food[1],food[2],food[3],food[4],food[5],food[6])
        
    async def is_user_exist(self, user_id):
        query = f"""
        SELECT * FROM mfcus WHERE user_id = {user_id}
        """
        data = await self.read_from_base(query)
        if len(data) == 0:
            return False
        else:
            return True

    async def write_to_base(self, query):
        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()

    async def read_from_base(self, query):
        c = self.connection.cursor()
        c.execute(query)
        return c.fetchall()

    async def update_all_column(self, user_id):
        query = f"""
        UPDATE mfcus SET description = 'None', location = 'None', 
        status = 'None', last_food = 'None' WHERE user_id = {user_id}
        """
        await self.write_to_base(query)

    async def get_user(self, user_id):
        query = f"""
        SELECT * FROM mfcus WHERE user_id = {user_id}
        """
        data = await self.read_from_base(query)
        data = list(data[0])
        return UserOB(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10])

    async def update_column(self, user_id: int,column: str, value: any):
        query = ""
        if type(value) == int:
            query = f"""
            UPDATE mfcus SET {column} = {value} WHERE user_id = {user_id}
            """
        else:
            query = f"""
            UPDATE mfcus SET {column} = '{value}' WHERE user_id = {user_id}
            """

        try:
            await self.write_to_base(query)

        except SyntaxError:
            second_value = str()
            second_value = value
            second_value.replace("'","`")
            query = f"""
            UPDATE mfcus SET {column} = '{second_value}' WHERE user_id = {user_id}                
            """
            await self.write_to_base(query)

    async def update_books(self, user_id: int, condition: str, answer: str, column: str, value: any):
        query = f"""
        UPDATE TABLE books SET {column} = ? WHERE {condition} = '{answer}' and user_id = {user_id}
        """

        await self.write_to_base(query)

    async def insert_user(self, user_id):
        query = f"""
        INSERT INTO mfcus (user_id,step) VALUES ({user_id},1)
        """
        await self.write_to_base(query)

    async def get_user_orders(self,user: UserOB):
        """
        Userning hamma buyutmalari shu metod yordamida books jadvalidan olinadi
        """
        query = f"""
        SELECT * FROM books WHERE user_id = {user.user_id} 
        """
        orders = await self.read_from_base(query)
        if len(orders) == 0: return None
        check_list = dict()
        for i in orders:
            if i[2] in check_list and i[3] != 0:
                count = check_list.get(i[2])
                check_list[i[2]] = count + i[3]
            else:
                check_list[i[2]] = i[3]

        return check_list

    async def add_user_order(self, user: UserOB, food: Food, text: str):
        """
        Userning hamma buyurtmalari shu metod orqali books jadvaliga yoziladi
        """
        query = f"""
        INSERT INTO books (id, user_id, food_name, count_food) 
        VALUES ({user.id},{user.user_id}, '{food.name}', {int(text)})
        """
        await self.write_to_base(query)

    async def delete_from_books(self, user_id: int, food = None):
        """
        Userning buyurtmalari booksdan faqat shu metod orqali o'chiriladi
        """
        query = str()
        if food == None:
            query = f"""
            DELETE FROM books WHERE user_id = {user_id}
            """

        else:
            query = f"""
            DELETE FROM books WHERE user_id = {user_id} and food_name = '{food}'
            """

        await self.write_to_base(query)

    async def add_to_sales(self, user_id: int, order_cost: int):
        query = f"""
        INSERT INTO sales (id, order_cost) VALUES ({user_id},{order_cost})
        """
        # print(query)
        await self.write_to_base(query)

class SCDB:
    def __init__(self):
        self.connection2 = psycopg2.connect(
            host="ec2-44-194-117-205.compute-1.amazonaws.com",
            database="dajf4n97l9f9cn",
            user="pkngmkhjfnvmhi",
            password="0a3fac6e67f9f29946adc77db24c903c4a5f25eead251702bb96ff6e0d79b870"
        )

    async def delete_from_base(self, user_id: int):
        query = f"""
                DELETE FROM books WHERE user_id = {user_id}
                """
        await self.__write_to_base(query)


    async def __write_to_base(self, query):
        cr = self.connection2.cursor()
        cr.execute(query)
        self.connection2.commit()

