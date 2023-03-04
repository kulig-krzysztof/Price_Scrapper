# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector


class PricesPipeline:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'aijo'
        )

        self.cur = self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS prices(
            id int NOT NULL auto_increment,
            company varchar(100),
            name varchar(255),
            price varchar(100),
            PRIMARY KEY (id)
        )
        """)
    def process_item(self, item, spider):

        self.cur.execute("insert into prices (company, name, price) values (%s, %s, %s)", ( item["company"][0], item["name"][0], item["price"]))

        self.conn.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()