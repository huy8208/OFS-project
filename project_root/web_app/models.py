from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

class CustomerManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('Email cannot be empty!')
        if not username:
            raise ValueError('Username cannot be empty!')

        user = self.model(email=self.normalize_email(email),username=username)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_customer = False
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Customer(AbstractBaseUser):
    email = models.EmailField(_('email address'),unique=True)
    username = models.CharField(max_length=100,unique=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects  = CustomerManager()

    def __str__(self):
        """select username to be displayed in admin panel"""
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
    CATEGORY = (
        ('Vegetable','Vegetable'),
        ('Fruit','Fruit'),
        ('Meat','Meat'),('Pantry','Pantry'),('Dairy','Dairy'),('Frozen Foods', 'Frozen Foods'),('Beverages','Beverages')
    )
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(null=True,blank=True,upload_to='uploaded_images/')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        """Check to see if there is an image of product, if it does, return that image, 
        else -> return none to prevent bug."""
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    """The model order has many-to-one relationship with model customer and product.
    One customer can have many orders. One product can have many orders."""
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )

    customer = models.ForeignKey(Customer,blank=True,null=True, on_delete= models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True,null=True)
    # date_created = models.DateTimeField(auto_now_add=True,null=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)
    # product = models.ManyToManyField(Product) #May need to be removed
    status = models.CharField(max_length=200,null=True, choices=STATUS)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        """Calculate and return total price for all product in cart."""
        allOrderedItems = OrderedItem.objects.all()
        total = sum([item.get_total for item in allOrderedItems])
        return total

    @property
    def get_cart_items(self):
        """Calculate and return total price for all product in cart."""
        allOrderedItems = OrderedItem.objects.all()
        total = sum([item.quantity for item in allOrderedItems])
        return total

class OrderedItem(models.Model):
    """An order Item is one item with an order. For example, a shopping cart may consist of many items but is all part of one order.
     Therfore the OrderItem model will be a child of the PRODUCT model AND the ORDER Model."""
    class Meta:
        verbose_name = "Ordered Item"

    product = models.ForeignKey(Product, on_delete= models.SET_NULL, blank = True, null = True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL, blank = True, null = True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True)
       
    @property
    def get_total(self):
        """Calculate and return total price for each product in cart."""
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    # Store shipping address of customer
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, blank = True, null = True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL, blank = True, null = True)
    address = models.CharField(max_length = 200, null = True)
    city = models.CharField(max_length = 200, null = True)
    state = models.CharField(max_length = 200, null = True)
    zipcode = models.CharField(max_length = 200, null = True)
    data_added = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.address


