import React, { useEffect, useRef } from 'react';
import { Network } from 'vis-network';
import { useSelector, useDispatch } from 'react-redux';
import { setNodes, setEdges, setSelectedNode } from '../features/network/networkSlice';
import { nodes, edges } from './NetworkData';

const NetworkGraph = () => {
    const networkRef = useRef(null);
    const dispatch = useDispatch();
    const { nodes: storeNodes, edges: storeEdges, selectedNode } = useSelector(state => state.network);

    useEffect(() => {
        // Sample data
        // const nodes = nodes;
        // const edges = edges;

        dispatch(setNodes(nodes.get()));
        dispatch(setEdges(edges.get()));

        const data = {
            nodes: nodes,
            edges: edges
        };

        const options = {
            layout: {
                hierarchical: {
                    direction: 'LR',
                    sortMethod: 'directed',
                    levelSeparation: 150,
                    nodeSpacing: 100
                }
            },
            nodes: {
                shape: 'dot',
                size: 16,
                font: {
                    size: 14
                }
            },
            edges: {
                width: 1,
                color: {
                    color: '#999999',
                    opacity: 0.5
                },
                smooth: {
                    type: 'curvedCW',
                    roundness: 0.2
                }
            },
            physics: {
                hierarchicalRepulsion: {
                    centralGravity: 0.0,
                    springLength: 100,
                    springConstant: 0.01,
                    nodeDistance: 120,
                    damping: 0.09
                },
                solver: 'hierarchicalRepulsion'
            }
        };

        // Create network
        const network = new Network(networkRef.current, data, options);

        // Add click event handler
        network.on('click', function(params) {
            if (params.nodes.length > 0) {
                const nodeId = params.nodes[0];
                const node = nodes.get(nodeId);
                dispatch(setSelectedNode(node));
            }
        });

        // Cleanup
        return () => {
            network.destroy();
        };
    }, [dispatch]);

    return (
        <div>
            <div 
                ref={networkRef} 
                style={{ 
                    height: '600px', 
                    border: '1px solid lightgray',
                    backgroundColor: '#ffffff'
                }}
            />
            {selectedNode && (
                <div style={{ 
                    padding: '1rem', 
                    marginTop: '1rem', 
                    border: '1px solid #ddd',
                    borderRadius: '4px'
                }}>
                    <h3>Selected Node Information</h3>
                    <p>ID: {selectedNode.id}</p>
                    <p>Label: {selectedNode.label}</p>
                    <p>Level: {selectedNode.level}</p>
                </div>
            )}
        </div>
    );
};

export default NetworkGraph; 