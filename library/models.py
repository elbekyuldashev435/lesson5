from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    data_birth = models.IntegerField()

    class Meta:
        db_table = 'author'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Books(models.Model):
    book_category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.BigIntegerField()
    year = models.IntegerField()
    image = models.ImageField('library/', blank=True, null=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return f"{self.book_category.name} {self.name}"


class BookAuthor(models.Model):
    author_name = models.ForeignKey(to='Author', on_delete=models.CASCADE)
    book_name = models.ForeignKey(to='Books', on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_author'

    def __str__(self):
        return f"{self.author_name}"
