from odoo import models, fields, api


class Proveedores(models.Model):
    _name = 'tienda.proveedores'
    cif = fields.Char('CIF', required=True)
    nombre = fields.Char('Nombre', required=True)
    direccion = fields.Char('Direccion', required=True)
    provincia = fields.Char('Provincia', required=True)
    cp = fields.Integer('Codigo Postal', required=True)
    tlf = fields.Integer('Telefono', required=True)
    email = fields.Char('Email', required=True)


    def name_get(self):
        res=[]
        for record in self:
            name = record.cif
            res.append((record.id, name))
        return res

    @api.one
    def limpiar(self):
        self.cif = ""
        return True

    @api.multi
    def limpia_todo(self):
        self.cif = ""
        self.direccion = ""
        self.provincia = ""
        self.cp = ""
        self.tlf = ""
        self.email = ""
        self.nombre = ""

        #done_recs = self.search([('marca', '=', 'fender')])
        #done_recs.write({'marca': 'Fender'})
        return True
    
