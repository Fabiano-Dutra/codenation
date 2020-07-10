from django.db import models
# Create your models here.

# Esta classe tem de ficar acima para funcionar seu relacionamento com a classe Product que está abaixo.
# Uma categoria pode ter vários produtos 1xn.
class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição')

    # Função p/ retornar o nome do produto, se tentar converter p/ uma string, aqui diz o que fazer.
    def __str__(self):
        return f'{self.name} - {self.products.count()}'

    # A classe meta abaixo é para indicar como será escrito o nome em plural de categorias no site admin
    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    # Aqui está um relacionamento com Category: ForeignKey traz o id da Category e deletion.Don_Nothing é para não
    # deletar a category se deletar um product. E relate_name fará aparecer na categoria todos os produtos que tiver.
    category = models.ForeignKey(Category,
                                 on_delete=models.deletion.DO_NOTHING,
                                 # Abaixo é o atributo products representa todos os produtos
                                 # pertencentes a categoria.
                                 related_name='products'
                                 )

    # Função p/ retornar o nome do produto, se tentar converter p/ uma string, aqui diz o que fazer.
    def __str__(self):
        return self.name
