from django.contrib import admin
from exames.models import TiposExames, PedidosExames, SolicitacaoExame


admin.site.register(TiposExames)
admin.site.register(PedidosExames)
admin.site.register(SolicitacaoExame)
