
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountAnalyticLinePlan(models.Model):
    _inherit = 'account.analytic.line.plan'

    resource_plan_id = fields.Many2one(
        comodel_name='analytic.resource.plan.line',
        string='Resource Plan Line',
        copy=False,
        ondelete='cascade'
    )
