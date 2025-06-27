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
    body_contracts = models.ManyToManyField('bodycontracts.BodyContract', verbose_name="itens contrato") 
    contract_types = models.ForeignKey('contracttypes.ContractType', on_delete=models.CASCADE)
     
    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering =['id']
    
    def __str__(self):
        return  self.contract_title