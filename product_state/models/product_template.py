# Copyright 2017 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_state_id = fields.Many2one(
        comodel_name="product.state")
    state = fields.Char(
        related="product_state_id.code",
        index=True,
        store=True)
