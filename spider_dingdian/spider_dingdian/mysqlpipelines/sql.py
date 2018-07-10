
import pymysql

from spider_dingdian import settings

conn = pymysql.connect(host=settings.MYSQL_HOSTS, port=settings.MYSQL_PORT,
                user=settings.MYSQL_USER, password=settings.MYSQL_PASSWORD,
                database=settings.MYSQL_DB)
cur = conn.cursor()


class Sql:

    @classmethod
    def insert_xiaoshuo(cls, xs_name,
                        xs_author, category,
                        name_id):
        value = {
            'xs_name': xs_name,
            'xs_author': xs_author,
            'category': category,
            'name_id': name_id
        }
        sql = 'insert into xiaoshuo(xs_name, xs_author, category, name_id) VALUES ' \
              '(%(xs_name)s, %(xs_author)s, %(category)s, %(name_id)s)'

        cur.execute(sql, value)
        conn.commit()

    @classmethod
    def select_name(cls, name_id):
        value = {
            'name_id': name_id
        }
        sql = 'select exists(select 1 from xiaoshuo where name_id=%(name_id)s)'

        cur.execute(sql, value)

        return cur.fetchall()[0]

    @classmethod
    def insert_content(cls, name_id, chapter_name,
                       content, num, chapter_url):
        sql = 'insert into content(name_id, chapter_name, content, num_id, url)' \
              ' VALUES (%(name_id)s, %(chapter_name)s, %(content)s, %(num)s, %(chapter_url)s)'

        values = {
            'name_id': name_id,
            'chapter_name': chapter_name,
            'content': content,
            'num': num,
            'chapter_url': chapter_url
        }
        cur.execute(sql, values)
        conn.commit()

    @classmethod
    def select_chapter(cls, url):
        sql = 'select exists(select 1 from content where chapter_url=%(url)s)'

        value = {
            'url': url
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]