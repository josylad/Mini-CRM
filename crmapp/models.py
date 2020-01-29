from django.db import models


# Create your models here.
class Companies(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    pub_date = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to = 'company_pics/', blank=True, default='company_pics/default.jpg')
    website = models.URLField(null=True)

    
    def save_company(self):
        self.save()
    
    def delete_company(self):
        self.delete()
        
    @classmethod
    def get_allcompany(cls):
        company = cls.objects.all()
        return company
    
    @classmethod
    def search_company(cls, search_term):
        company = cls.objects.filter(name__icontains=search_term)
        return company
    
    
    @classmethod
    def get_companies(request, id):
        try:
            company = company.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return company
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Company'
        verbose_name_plural = 'Companies'
        
        
        
class Employee(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    company = models.ForeignKey(Companies,on_delete=models.CASCADE, blank=True)

    def save_employee(self):
        self.save()

    def delete_employee(self):
        self.delete()
    
    def __str__(self):
        return f"{self.firstname}, {self.lastname}, {self.email}"
    
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
            