from django.contrib import admin

from products.models import Product, Category, Order

from django.utils.html import format_html
from django.urls import reverse

# Register your models here.

# Para personalizar a exibição de categoria no admin utiliza-se a classe abaixo.
class CategoryModelAdmin(admin.ModelAdmin):
    def products(self, obj):
        # Variavel href com o caminho para o html de produtos 'admin:APP-NAME_MODEL_changelist'
        href = reverse('admin:products_product_changelist') + f'?category={obj.pk}'
        # Utilizando o atributo products definido em models na classe Product, utilizado com um contador abaixo.
        # E colocando um caminho html com o format_html par chegar nos produtos da categoria:
        return format_html(f'<a href="{href}">{ obj.products.count() }</a>')

    # Alterando o título da coluna categoria na tela admin, dando no título abaixo
    products.short_description = 'Produtos da Categoria'

    # O products dentro dos ('') abaixo refere-se a função acima que terá seu resultado exibido com o list_display.
    list_display = ('name', 'description', 'products')


class ProductModelAdmin(admin.ModelAdmin):
# Esta queryset é desnecessária pois o django já faz a estrutura automaticamente.
#    def queryset(self, request, queryset):
#        category = request.GET.get('category')
#        if category:
#            return queryset.filter(category__pk=category)
#
#        return queryset

    # Usando função para mudar o formato da coluna de preços, esta função irá para list_display no lugar do preço
    def formatted_price(self, obj):
        return f'R$ {obj.price}'

    formatted_price.short_description = 'Preço'

    # Criando uma link para categoria que aparece na lista de produtos do admin.
    def link_category(self, obj):
        href = reverse('admin:products_category_change', args=(obj.category.pk,))
        return format_html(f'<a href="{href}">{obj.category.name}<a/>')

    # Alterando o título da coluna categoria na tela admin, dando no título abaixo:
    link_category.short_description = 'Categoria'

    # O list_display é uma tupla com os campos que se quer mostrar, definindo display para produto
    list_display = ('name', 'formatted_price', 'description', 'link_category')


admin.site.register(Product, ProductModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Order)
