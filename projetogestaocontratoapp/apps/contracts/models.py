from django.db import models
from contractypes.models import ContractType

# Create your models here.
class Contract(models.Model):  
    contract_type = models.ForeignKey(ContractType, on_delete=models.CASCADE)
    note = models.TextField('Descricao', max_length=200)
    contract_date = models.DateField('Data do Contrato', auto_now=False, auto_now_add=False)   
    is_active = models.BooleanField('Ativo', default=False)
    term = models.DateField('Prazo do Contrato', auto_now=False, auto_now_add=False)   
    value = models.DecimalField('Valor do Contrato', max_digits=10, decimal_places=2, default=0.00)
    contract_title = models.CharField('Titulo do Contrato', max_length=200, blank=True, null=True)
   
    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering =['id']
    
    def __str__(self):
        return self.contract_title
    

class Attachment(models.Model):
    
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='anexos')
    file_name = models.CharField(max_length=255)
    file = models.ImageField(upload_to='attachment_contract/') 

    class Meta:
        verbose_name = 'Anexo'
        verbose_name_plural = 'Anexos'
        ordering =['id']
    
    def __str__(self):
        return self.contract

