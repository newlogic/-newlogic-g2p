#
# Copyright (c) 2022 Newlogic.
#
# This file is part of newlogic-g2p-erp.
# See https://github.com/newlogic/newlogic-g2p-erp/ for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from odoo import _, fields, models


class G2PProgram(models.Model):
    _inherit = ["mail.thread", "mail.activity.mixin", "g2p.job.mixin"]
    _name = "g2p.program"
    _description = "Program"
    _order = "id desc"
    _check_company_auto = True

    # TODO: Associate a Wallet to each program using the accounting module
    # TODO: (For later) Associate a Warehouse to each program using the stock module for in-kind programs

    name = fields.Char(required=True, tracking=True)
    company_id = fields.Many2one(
        "res.company", default=lambda self: self.env.company, tracking=True
    )
    target_type = fields.Selection(
        selection=[("group", "Group"), ("individual", "Individual")], default="group"
    )

    # delivery_mechanism = fields.Selection([("mobile", "Mobile"), ("bank_account", "Bank Account"),
    # ("id", "ID Document"), ("biometric", "Biometrics")], default='id')

    # Pre-cycle steps
    # TODO: for those, we should allow to have multiple managers and
    #  the order of the steps should be defined by the user
    eligibility_managers = fields.Many2many(
        "g2p.eligibility.manager", string="Eligibility Managers"
    )  # All will be run
    deduplication_managers = fields.Many2many(
        "g2p.deduplication.manager", string="Deduplication Managers"
    )  # All will be run
    # for each beneficiary, their preferred will be used or the first one that works.
    notification_managers = fields.Many2many(
        "g2p.program.notification.manager", string="Notification Managers"
    )
    program_managers = fields.Many2many(
        "g2p.program.manager", string="Program Managers"
    )
    # Cycle steps
    cycle_managers = fields.Many2many(
        "g2p.cycle.manager", string="Cycle Managers"
    )
    entitlement_managers = fields.Selection([])

    reconciliation_managers = fields.Selection([])

    program_membership_ids = fields.One2many(
        "g2p.program_membership", "program_id", "Program Memberships"
    )
    cycle_ids = fields.One2many("g2p.cycle", "program_id", "Cycles")

    # TODO: JJ - Add a way to link reports/Dashboard about this program.

    # TODO: Implement the method that will call the different managers
    def import_beneficiaries(self):
        # 1. get the beneficiaries using the eligibility_manager.import_eligible_registrants()
        for rec in self:
            if rec.eligibility_managers:
                err_ctr = 0
                for el in rec.eligibility_managers:
                    if not el.manager_ref_id.import_eligible_registrants():
                        err_ctr += 1
                if err_ctr == 0:
                    # Add import to queue job. Show success notification!
                    title = _("ON QUEUE!")
                    message = _(
                        "The import was put on queue. Re-open this form later to refresh the program members."
                    )
                    kind = "success"  # warning, danger, info, success
                elif err_ctr == len(rec.eligibility_managers):
                    # No registrants imported. Show error message!
                    title = _("ERROR!")
                    message = _("There are no registrants imported.")
                    kind = "danger"
                elif err_ctr < len(rec.eligibility_managers):
                    # Not all registrants are imported. Show warning!
                    title = _("WARNING!")
                    message = _(
                        "%s out of %s managers are not imported."
                        % (err_ctr, len(rec.eligibility_managers))
                    )
                    kind = "warning"

            else:
                # No eligibility managers entered. Show error message!
                title = _("ERROR!")
                message = _("There are no eligibility managers defined.")
                kind = "danger"

            return {
                "type": "ir.actions.client",
                "tag": "display_notification",
                "params": {
                    "title": title,
                    "message": message,
                    "sticky": False,
                    "type": kind,
                },
            }

    def verify_eligibility(self):
        # 1. Verify the eligibility of the beneficiaries using eligibility_manager.validate_program_eligibility()
        pass

    def deduplicate_beneficiaries(self):
        # 1. Deduplicate the beneficiaries using deduplication_manager.check_duplicates()
        pass

    def notify_eligible_beneficiaries(self):
        # 1. Notify the beneficiaries using notification_manager.enrolled_in_program()
        pass

    def create_new_cycle(self):
        # 1. Create the next cycle using cycles_manager.new_cycle()
        # 2. Import the beneficiaries from the previous cycle to this one. If it is the first one, import from the
        # program memberships.
        pass
