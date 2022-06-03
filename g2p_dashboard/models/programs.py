# Part of Newlogic G2P. See LICENSE file for full copyright and licensing details.

from odoo import _, fields, models


class G2PProgram(models.Model):
    _inherit = "g2p.program"

    dashboard_id = fields.Many2one("dashboard.menu", "Dashboard")

    def open_dashboard(self):
        self.ensure_one()

        if self.dashboard_id:
            action = self.dashboard_id.client_action
            return {
                "type": "ir.actions.client",
                "name": action.name,
                "tag": action.tag,
                "id": action.id,
                # 'context': {'record_id':self.id},
            }

        else:
            message = _("A dashboard must be defined for this program.")
            kind = "danger"

            return {
                "type": "ir.actions.client",
                "tag": "display_notification",
                "params": {
                    "title": _("Program"),
                    "message": message,
                    "sticky": True,
                    "type": kind,
                },
            }
