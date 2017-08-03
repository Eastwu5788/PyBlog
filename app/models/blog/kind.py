from django.db import models


class BlogKind(models.Model):

    user_id = models.IntegerField()
    title = models.CharField()
    status = models.IntegerField()
    created_time = models.CharField()
    updated_time = models.CharField()

    @staticmethod
    def query_format_kind(kind_id=0, cache=True):
        obj = BlogKind.objects.get(id=kind_id)
        if not obj:
            return {}
        return BlogKind.format_kind_info(obj)

    @staticmethod
    def format_kind_info(kind):
        result = dict()
        result["kind_id"] = kind.id
        result["title"] = kind.title
        result["created_time"] = kind.created_time
        return result

    class Meta:
        app_label = "b_blog"
        db_table = "blog_kind"