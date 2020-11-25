import datetime
from peewee import *
from playhouse.db_url import connect
from playhouse.shortcuts import model_to_dict, dict_to_model


database = connect('postgresql://postgres:admin@localhost:5432/weather')
database_proxy = DatabaseProxy()  # Create a proxy for our db.
# Configure our proxy to use the db we specified in config.



class BaseModel(Model):
    class Meta:
        database = database  # Use proxy for our DB.


class Weather(BaseModel):
    """Weather record"""

    date = DateField(primary_key=True)
    day_temperature = TextField()
    night_temperature = TextField()
    day_description = TextField()
    pressure = TextField()
    humidity = TextField()
    wind = TextField()


class DatabaseUpdater:
    def save_data(self, data: dict) -> None:
        """
        Save weather to database

        Args:
            data (dict): {date1: {day_temperature: xx, ...}, date2: {day_temperature: xx, ...}}
        """
        for date, day_info in data.items():
            new_record = {**{'date': date}, **day_info}
            query = Weather.select().where(Weather.date == date)

            if len(query):
                Weather.update(**new_record)
            else:
                Weather.create(**new_record)

    def load_data(self, period_from: str, period_to: str = None) -> list:
        """
        Load weather from database

        Args:
            period_from (str): Start of period for load. Format: 'YYYY-MM-DD'
            period_to (str): Start of period for load. Format: 'YYYY-MM-DD'

        Returns:
            list: [{'date1': datetime.date, etc.}, {date2': datetime.date, etc.}]
        """

        period_from = datetime.datetime.strptime(period_from, '%Y-%m-%d').date()
        if period_to:
            period_to = datetime.datetime.strptime(period_to, '%Y-%m-%d').date()
        else:
            period_to = period_from

        query = Weather.select().where(Weather.date.between(period_from, period_to))

        result = []
        for elem in query:
            elem_dict = {
                'date': elem.date,
                'day_temperature': elem.day_temperature,
                'night_temperature': elem.night_temperature,
                'day_description': elem.day_description,
                'pressure': elem.pressure,
                'humidity': elem.humidity,
                'wind': elem.wind,
            }
            result.append(elem_dict)

        return result


database.create_tables([Weather])
