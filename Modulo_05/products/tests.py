from django.test import TestCase

from Modulo_05.products.models import Product

# Create your tests here.
class ProductStrTestCase(TestCase):
    def test_str_should_return_name(self):
        # Qualquer módulo tem um gerenciador que é acessado através de objects
        # utilizando o gerenciado consegue criar, filtrar, deletar e outras operações
        product = Product.objects.create(
            nome='Teste Produto',
            description='Teste description',
            price=10.5
        )
        self.assertEqual(str(product), 'Teste Produto')

