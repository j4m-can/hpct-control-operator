#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""Control operator for cluster.
"""

import logging

from ops.main import main

from hpctops.charm.service import ServiceCharm

logger = logging.getLogger(__name__)


class HpctControlCharm(ServiceCharm):
    """Control operator."""

    def __init__(self, *args):
        super().__init__(*args)

        self.framework.observe(self.on.add_compute_action, self._on_add_compute_action)
        self.framework.observe(self.on.add_group_action, self._on_add_group_action)
        self.framework.observe(self.on.add_user_action, self._on_add_user_action)

        self.framework.observe(
            self.on.control_ldap_server_action, self._on_control_ldap_server_action
        )
        self.framework.observe(
            self.on.control_slurm_server_action, self._on_control_slurm_server_action
        )

        self.framework.observe(self.on.remove_compute_action, self._on_remove_compute_action)
        self.framework.observe(self.on.remove_group_action, self._on_remove_group_action)
        self.framework.observe(self.on.remove_user_action, self._on_remove_user_action)

    def params_doc(self, params):
        l = []
        for k, v in params.items():
            l.append(f"{k:>15}: {v}")
        return "\n".join(l)

    def _on_add_compute_action(self, event):
        logging.debug(f"add-compute")
        event.log(self.params_doc(event.params))

    def _on_add_group_action(self, event):
        logging.debug(f"add-group")
        event.log(self.params_doc(event.params))

    def _on_add_user_action(self, event):
        logging.debug(f"add-user")
        event.log(self.params_doc(event.params))

    def _on_control_ldap_server_action(self, event):
        logging.debug(f"control-ldap-server")
        event.log(self.params_doc(event.params))

    def _on_control_slurm_server_action(self, event):
        logging.debug(f"control-slurm-server")
        event.log(self.params_doc(event.params))

    def _on_remove_compute_action(self, event):
        logging.debug(f"remove-compute")
        event.log(self.params_doc(event.params))

    def _on_remove_group_action(self, event):
        logging.debug(f"remove-group")
        event.log(self.params_doc(event.params))

    def _on_remove_user_action(self, event):
        logging.debug(f"remove-user")
        event.log(self.params_doc(event.params))


if __name__ == "__main__":
    main(HpctControlCharm)
