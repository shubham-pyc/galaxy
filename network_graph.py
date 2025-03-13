import networkx as nx
import json
import random

# Create a new graph
G = nx.Graph()

# Generate node names
prefixes = {
    'STG_': ['customer', 'order', 'product', 'sales', 'inventory', 'supplier', 'employee', 
             'shipment', 'return', 'payment', 'category', 'location', 'promotion', 'review',
             'warehouse', 'price', 'discount', 'transaction', 'account', 'department', 
             'store', 'region', 'campaign', 'brand', 'market'],
    'SAT_': ['daily', 'monthly', 'yearly', 'customer_profile', 'order_details', 'product_metrics',
             'sales_summary', 'inventory_status', 'supplier_performance', 'employee_stats',
             'shipment_tracking', 'return_analysis', 'payment_summary', 'category_performance',
             'location_metrics', 'promotion_effectiveness', 'review_analytics', 'warehouse_status',
             'price_history', 'discount_impact', 'transaction_summary', 'account_status',
             'department_metrics', 'store_performance', 'region_analysis'],
    'FACT_': ['sales', 'orders', 'inventory', 'customers', 'employees', 'shipments', 'returns',
              'payments', 'products', 'suppliers', 'categories', 'locations', 'promotions',
              'reviews', 'warehouses', 'prices', 'discounts', 'transactions', 'accounts',
              'departments', 'stores', 'regions', 'campaigns', 'brands', 'markets'],
    'VW_': ['sales_summary', 'order_analytics', 'inventory_report', 'customer_insights',
            'employee_dashboard', 'shipment_status', 'return_summary', 'payment_analytics',
            'product_performance', 'supplier_overview', 'category_summary', 'location_report',
            'promotion_impact', 'review_summary', 'warehouse_metrics', 'price_analysis',
            'discount_summary', 'transaction_report', 'account_overview', 'department_summary',
            'store_analytics', 'region_performance', 'campaign_metrics', 'brand_summary',
            'market_analysis']
}

# Add nodes to the graph
all_nodes = []
for prefix, suffixes in prefixes.items():
    for suffix in suffixes:
        node_name = f"{prefix}{suffix}"
        # Generate a unique random name
        random_name = f"T001_{node_name}"
            
        # Add node with both the ID and the random name
        G.add_node(node_name, object_id=random_name)
        all_nodes.append(node_name)

# Add random edges between nodes
# Each node will have 2-5 connections
for node in all_nodes:
    num_connections = random.randint(2, 5)
    possible_targets = [n for n in all_nodes if n != node and not G.has_edge(node, n)]
    if possible_targets:
        targets = random.sample(possible_targets, min(num_connections, len(possible_targets)))
        for target in targets:
            G.add_edge(node, target)

# Convert the graph to a dictionary format using NetworkX's built-in method
graph_data = nx.node_link_data(G)

# Save to JSON file
with open('network_graph.json', 'w') as f:
    json.dump(graph_data, f, indent=2)

print("Network graph has been created with:")
print(f"- Number of nodes: {G.number_of_nodes()}")
print(f"- Number of edges: {G.number_of_edges()}")
print("The graph has been saved to 'network_graph.json'") 