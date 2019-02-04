from odoo import models, fields, api


class Articulos(models.Model):
    _name = 'tienda.pedidos'
    cod = fields.Char('Codigo', required=True)
    articulo = fields.Many2one('tienda.articulos','Articulo', required=True)
    proveedor = fields.Many2one('tienda.proveedores','Proveedor', required=True)
    cantidad = fields.Integer('Cantidad', required=True)
    precuni = fields.Integer('Precio por unidad', required=True)
    prectotal = fields.Integer('TOTAL: ', required=True)



    def name_get(self):
        res=[]
        for record in self:
            name = record.cod
            res.append((record.id, name))
        return res

    @api.one
    def limpiar(self):
        self.cod = ""
        return True

    @api.multi

    def limpia_todo(self):
        self.cod = ""
        self.articulo = ""
        self.proveedor = ""


        done_recs = self.search([('marca', '=', 'fender')])
        done_recs.write({'marca': 'Fender'})
        return True

