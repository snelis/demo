from django.db import models


class Color(models.Model):
    color = models.CharField(max_length=64)


class ShoeQuerySet(models.query.QuerySet):
    def color(self, color):
        """
        :rtype: ShoeQuerySet
        """
        return self.filter(color__color=color)

    def size(self, size):
        """
        :rtype: ShoeQuerySet
        """
        return self.filter(size=size)


class ShoeManager(models.Manager):
    def get_query_set(self):
        """
        :rtype: ShoeQuerySet
        """

        qs = ShoeQuerySet(self.model)

        # prefetch
        qs = qs.select_related('color')

        return qs


class Shoe(models.Model):
    size = models.IntegerField()
    color = models.ForeignKey(Color)

    objects = ShoeManager()

    def __repr__(self):
        return '<Shoe({id}:{size}-{color})>'.format(**dict(
            id=self.id,
            size=self.size,
            color=self.color.color
        ))