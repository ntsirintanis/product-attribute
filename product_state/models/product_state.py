# Copyright 2020 Therp B.V. (<https://therp.nl>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class ProductState(models.Model):
    _name = "product.state"
    
    name = fields.Char(
        required=True,
        translate=True)
    code = fields.Char(
        required=True)
