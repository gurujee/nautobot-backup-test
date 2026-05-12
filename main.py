"""
Main orchestration entry point for Demo2.
"""

from orchestrator.clients.nautobot_client import get_devices
from orchestrator.clients.nornir_client import run_command
from orchestrator.loaders.inventory_loader import load_target_devices
from orchestrator.managers.backup_manager import save_backup
from orchestrator.managers.git_manager import git_commit_backup_changes

target_devices = load_target_devices(
    "inventory/target_devices.yml"
)

devices = get_devices(target_devices)

results = run_command(
    devices=devices,
    command="show running-config",
    textfsm=False,
)

for device_name, result in results.items():
    if result["status"] == "success":
        save_backup(
            device_name=device_name,
            config_output=result["output"],
            result_data=result,
    )

git_commit_backup_changes(
    repo_path=".",
    commit_message="Updated device backups",
)

print (results)

print("Backups saved successfully.")

