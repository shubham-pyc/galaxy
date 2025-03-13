import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  nodes: [],
  edges: [],
  selectedNode: null,
  loading: false,
  error: null
};

export const networkSlice = createSlice({
  name: 'network',
  initialState,
  reducers: {
    setNodes: (state, action) => {
      state.nodes = action.payload;
    },
    setEdges: (state, action) => {
      state.edges = action.payload;
    },
    setSelectedNode: (state, action) => {
      state.selectedNode = action.payload;
    },
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
    setError: (state, action) => {
      state.error = action.payload;
    }
  }
});

export const { setNodes, setEdges, setSelectedNode, setLoading, setError } = networkSlice.actions;

// Selectors
export const selectNodes = (state) => state.network.nodes;
export const selectEdges = (state) => state.network.edges;
export const selectSelectedNode = (state) => state.network.selectedNode;
export const selectLoading = (state) => state.network.loading;
export const selectError = (state) => state.network.error;

export default networkSlice.reducer; 