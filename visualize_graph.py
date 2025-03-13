from pyvis.network import Network
import json

# Read the JSON file
with open('network_graph.json', 'r') as f:
    graph_data = json.load(f)

# Create a new network
net = Network(height='750px', width='100%', bgcolor='#ffffff', font_color='#333333')
net.force_atlas_2based()
net.show_buttons(filter_=['physics'])

# Define level colors and y-coordinates
level_config = {
    'STG_': {'level': 1, 'color': '#4e79a7', 'y': -300},  # Blue
    'SAT_': {'level': 2, 'color': '#f28e2b', 'y': -100},  # Orange
    'FACT_': {'level': 3, 'color': '#e15759', 'y': 100},  # Red
    'VW_': {'level': 4, 'color': '#76b7b2', 'y': 300}     # Teal
}

# Add nodes with hierarchical positioning
for node in graph_data['nodes']:
    node_id = node['id']
    prefix = next(prefix for prefix in level_config.keys() if node_id.startswith(prefix))
    config = level_config[prefix]
    
    # Add node with specific configuration
    net.add_node(
        node_id,
        label=node_id,
        color=config['color'],
        level=config['level'],
        y=config['y'],
        physics=True,
        size=20,
        title=f"Level {config['level']}: {node_id}",
        object_id=node['object_id']  # Adding object_id as a value attribute
    )

# Add edges
for link in graph_data['links']:
    source = link['source']
    target = link['target']
    
    # Get the levels of source and target nodes
    source_prefix = next(prefix for prefix in level_config.keys() if source.startswith(prefix))
    target_prefix = next(prefix for prefix in level_config.keys() if target.startswith(prefix))
    
    # Calculate edge color based on the nodes it connects
    source_color = level_config[source_prefix]['color']
    target_color = level_config[target_prefix]['color']
    
    net.add_edge(
        source,
        target,
        color={'color': '#999999', 'opacity': 0.5},
        smooth={'type': 'curvedCW', 'roundness': 0.2}
    )

# Configure physics
net.set_options("""
const options = {
  "physics": {
    "hierarchicalRepulsion": {
      "centralGravity": 0.0,
      "springLength": 100,
      "springConstant": 0.01,
      "nodeDistance": 120,
      "damping": 0.09
    },
    "minVelocity": 0.75,
    "solver": "hierarchicalRepulsion"
  },
  "layout": {
    "hierarchical": {
      "enabled": true,
      "levelSeparation": 150,
      "nodeSpacing": 100,
      "treeSpacing": 200,
      "blockShifting": true,
      "edgeMinimization": true,
      "parentCentralization": true,
      "direction": "UD",
      "sortMethod": "directed"
    }
  }
}
""")

# Save the graph
net.save_graph('network_visualization.html')
print("Graph visualization has been saved to 'network_visualization.html'") 