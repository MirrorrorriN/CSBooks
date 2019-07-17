# -*- coding:utf-8 -*-

from elasticsearch_dsl import DocType,Nested,Date,Boolean,analyzer,Completion,Text,Keyword,Integer
from elasticsearch_dsl.connections import connections

# 新建连接
connections.create_connection(hosts="127.0.0.1")

class ArticleType(DocType):
    # 文章类型
    title = Text(analyzer="ik_max_word")
    create_date = Date()

    url = Keyword()
    url_object_id = Keyword()

    front_image_url = Keyword()
    front_image_path = Keyword()

    praise_nums = Integer()
    comment_nums = Integer()
    fav_nums = Integer()

    tags = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")

    class Meta:
        # 数据库名称和表名称
        index = "books"
        doc_type = "douban"

if __name__ == '__main__':
    ArticleType.init()