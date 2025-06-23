from django.db import models


# Create your models here.
class Contract(models.Model):  
    contract_title = models.CharField('Titulo do Contrato', max_length=200, blank=True, null=True)
    annotation = models.TextField('Descricao', max_length=200)
    contract_date = models.DateField('Data do Contrato', auto_now=False, auto_now_add=False)   
    is_active = models.BooleanField('Ativo', default=False)
    term = models.DateField('Prazo do Contrato', auto_now=False, auto_now_add=False)
    photo = models.ImageField('Foto', upload_to='photos')
    doc = models.FileField('Documentos', upload_to='docs')   
    #body_contracts = models.ManyToManyField('bodycontracts.BodyContract') 
    #negotiation = models.ForeignKey('negotiations.Negotiation', on_delete=models.CASCADE)
    contract_types = models.ForeignKey('contracttypes.ContractType', on_delete=models.CASCADE)
     
    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering =['id']
    
    def __str__(self):
        return  self.contract_title


  
    # def __str__(self):
    #     return  f"{self.contract_title} - {self.contract_type}"
# class Attachment(models.Model):
    
#     contract = models.ForeignKey('contracts.Contract', on_delete=models.CASCADE, related_name='anexos')
#     file_name = models.CharField(max_length=255)
#     file = models.ImageField(upload_to='attachment_contract/') 

#     class Meta:
#         verbose_name = 'Anexo'
#         verbose_name_plural = 'Anexos'
#         ordering =['id']
    
#     def __str__(self):
#         return self.contract

