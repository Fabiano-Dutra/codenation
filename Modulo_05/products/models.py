'''
    Modelo do app de Produtos.
'''

from django.db import models
from django.db.models import Q, QuerySet
# Create your models here.


# Criação de manager de produtos
class ProductManager(models.Manager):
    '''
        Realiza a pesquisa nos produtos cujo nome contenha 'text'
    '''
    #Filtro para pesquisar pelo texto usando a função with_text.
    def with_text(self, text: str) -> QuerySet:
        queryset = self.get_queryset().filter(name__contains=text)
        return queryset

    # Filtro para pegar os produtos caros acima de R$ 500,
    # função expensive_produts.
    def expensive_products(self) -> QuerySet:
        '''
            Realiza a lista dos produtos cujo preço seja maior do que R$ 500
        '''
        return self.get_queryset().filter(price__gte=500)

    # Filtro para pegar os produtos baratos abaixo de R$100,
    # função cheap_toys.
    def cheap_toys(self) -> QuerySet:
        '''
            Retorna a lista dos brinquedos mais baratos.
        '''
        return self.get_queryset().filter(
            category__name='Brinquedos',
            price__lte=100
        )

    # Filtro com operador 'ou'.
    def toys_or_expensive_items(self) -> QuerySet:
        '''
           Retorna a lista dos brinquedos mais caros.
        '''
        # O 'Q' funciona com operador 'ou'.
        query_filter = Q(category__name = 'Brinquedos') | Q(price__gte=500)
        queryset = self.get_queryset().filter(query_filter)
        print(queryset.query)
        return queryset

    # Função para testar o uso de documentação nas funções acima.
    def test_function(self):
        a = self.with_text('')
        b = self.expensive_products()
        c = self.cheap_toys()
        d = self.toys_or_expensive_items()




# Esta classe tem de ficar acima para funcionar seu relacionamento com a classe Product que está abaixo.
# Uma categoria pode ter vários produtos 1 x n.
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
    '''
        Model contendo todos os campos necessários para cadastrar produtos no ecomm.
    '''
    # Abaixo instancia do manager de produtos.
    # Extendendo o objects ao incluir mais comportamentos dentro dele, no caso o manager.
    objects = ProductManager()
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


# Função para API de vendas(orders)
class Order(models.Model):
    name = models.CharField('Nome do cliente', max_length=100)
    payment = models.CharField('Meio de pagamento', max_length=50)
    products = models.ManyToManyField(Product)

    @property
    def total_amount(self):
        # Vai pegar todos os valores das vendas, somar e retornar este resultado.
        return sum(product.price for product in self.products.all())

    # Função string para ficar mais fácil a visualização.
    def __str__(self):
        # Retornando o nome de quem está comprando e o total de seu pedido.
        return f'{self.name} - {self.total_amount}'