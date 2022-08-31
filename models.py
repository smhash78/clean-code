class User(AbstractUser):
    name = models.CharField(max_length=100)
    type = models.IntegerField()


class Payment(models.Model):
    is_paid = models.BooleanField(default=False)
    payment_agent = models.CharField(max_length=30)

    def get_payment_agent(self):
        """
        A monkey patch to get payment agent. Now is it store in the special
        field in the database. This method is deprecated and is used for
        backwards compatibility.

        .. deprecated:: r574
        """
        if not self.is_paid:
            return None

        if self.provider1.filter(type=1).count():
            self.payment_agent = User("Provider1")
        elif self.provider2.filter(type=1).count():
            self.payment_agent = User("AO Provider2")
        elif self.provider3.filter(type=1).count():
            self.payment_agent = User("Provider3")
        elif self.provider4.count():
            self.payment_agent = User("Complex Provider 4 Name With Surname")
        else:
            self.payment_agent = User("Provider5 Full Company-Name")

        self.save()
        return self.payment_agent
