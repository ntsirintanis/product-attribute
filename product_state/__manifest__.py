# Copyright 2017 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Product State",
    "summary": """
        Module introducing a state field on product template""",
    "author": "ACSONE SA/NV, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/product-attribute",
    "category": "Product",
    "version": "13.0.1.0.1",
    "license": "AGPL-3",
    "depends": [
        "product",
        "sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/product_views.xml",
        "views/product_state.xml",
    ],
    "application": True,
}
