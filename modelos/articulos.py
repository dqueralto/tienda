from odoo import models, fields, api


class Articulos(models.Model):
    _name = 'tienda.articulos'
    cod = fields.Char('Codigo', required=True)
    nombre = fields.Char('Nombre', required=True)
    marca = fields.Char('Marca', required=False)
    modelo = fields.Char('Modelo', required=False)
    descripcion = fields.Text('Descripción', required=False)
    proveedor = fields.Many2one('tienda.proveedores','Proveedor', required=False)
    preventa = fields.Integer('Precio de venta', required=False)


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
        self.nombre = ""
        self.descripcion = ""
        self.cp = ""
        self.tlf = ""
        self.email = ""
        self.nombre = ""

        #done_recs = self.search([('marca', '=', 'fender')])
        #done_recs.write({'marca': 'Fender'})
        return True
    
