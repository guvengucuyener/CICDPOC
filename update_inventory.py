import yaml
import json
import os

# Define File Paths
NETWORK_SERVICES_PATH = "group_vars/NETWORK_SERVICES/network_services.yml"
CONNECTED_ENDPOINTS_PATH = "group_vars/CONNECTED_ENDPOINTS/connected_endpoints.yml"
INPUT_DATA_PATH = "ui_input.json"

def main():
    # 1. Load the raw input web matrix from the Flask payload
    if not os.path.exists(INPUT_DATA_PATH):
        print(f"Error: {INPUT_DATA_PATH} not found. Skipping file generation.")
        return

    with open(INPUT_DATA_PATH, "r") as f:
        # Flask passes the matrix data down as an array of JSON objects/dictionaries
        # Expected structure matches your keys: vlanId, sviVirtualIpAddress, device, port, Mode, etc.
        try:
            web_rows = json.load(f)
        except Exception as e:
            # If coming as a raw stringified list, attempt to parse safely
            import ast
            with open(INPUT_DATA_PATH, "r") as f_raw:
                web_rows = ast.literal_eval(f_raw.read())

    # 2. Read Existing AVD Inventory Files
    with open(NETWORK_SERVICES_PATH, "r") as f:
        network_services = yaml.safe_load(f) or {"tenants": []}

    with open(CONNECTED_ENDPOINTS_PATH, "r") as f:
        connected_endpoints = yaml.safe_load(f) or {"servers": []}

    # Locate Tenant1 -> VRF DC mapping
    tenant = next((t for t in network_services.get("tenants", []) if t["name"] == "TENANT1"), None)
    if not tenant:
        print("Error: TENANT1 not found in network_services.yml")
        return
    
    vrf_dc = next((v for v in tenant.get("vrfs", []) if v["name"] == "DC"), None)
    if not vrf_dc:
        print("Error: VRF DC not found under TENANT1")
        return

    # Ensure svis list exists
    if "svis" not in vrf_dc:
        vrf_dc["svis"] = []

    # Locate Server1 for Adapters
    server1 = next((s for s in connected_endpoints.get("servers", []) if s["name"] == "server1"), None)
    if not server1:
        # If server1 doesn't exist, initialize it
        server1 = {"name": "server1", "adapters": []}
        connected_endpoints["servers"].append(server1)

    # 3. Process Each Web Row and inject into structures
    for row in web_rows:
        vlan_id = int(row.get("vlanId"))
        svi_ip = row.get("sviVirtualIpAddress")
        switch_name = row.get("device")
        switch_port = row.get("port")
        l2_mode = row.get("Mode")
        server_name = row.get("servername")

        # --- Update network_services.yml ---
        # Check if SVI ID already exists to prevent duplicate entries
        if not any(svi["id"] == vlan_id for svi in vrf_dc["svis"]):
            new_svi = {
                "id": vlan_id,
                "name": f"vlan{vlan_id}",
                "enabled": True,
                "ip_address_virtual": svi_ip
            }
            vrf_dc["svis"].append(new_svi)
            print(f"Added SVI for VLAN {vlan_id}")

        # --- Update connected_endpoints.yml ---
        # Build the exact layout matching Arista AVD specifications
        new_adapter = {
            "endpoint_ports": [server_name],
            "switch_ports": [switch_port],
            "switches": [switch_name],
            "vlans": vlan_id,
            "mode": l2_mode,
            "spanning_tree_portfast": "edge"
        }
        
        # Prevent adding identical switch interface mappings
        if not any(a["switches"] == [switch_name] and a["switch_ports"] == [switch_port] for a in server1["adapters"]):
            server1["adapters"].append(new_adapter)
            print(f"Added adapter connection on {switch_name} {switch_port}")

    # 4. Write Data cleanly back to files with correct formatting
    with open(NETWORK_SERVICES_PATH, "w") as f:
        yaml.dump(network_services, f, default_flow_style=False, sort_keys=False)

    with open(CONNECTED_ENDPOINTS_PATH, "w") as f:
        yaml.dump(connected_endpoints, f, default_flow_style=False, sort_keys=False)

    print("Inventory files updated successfully.")

if __name__ == "__main__":
    main()
