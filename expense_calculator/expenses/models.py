from django.db import models

# Models are widely used in Python programming, especially in frameworks like Django, where models represent database tables and are used for data manipulation and retrieval.

# In this case, we are creating a model called Expense, which will represent a database table called expenses.


class Expense(model.Model):
    """
    Expsense model
    """

    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"
