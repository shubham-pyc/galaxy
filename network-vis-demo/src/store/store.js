import { configureStore } from '@reduxjs/toolkit';
import networkReducer from '../features/network/networkSlice';

export const store = configureStore({
  reducer: {
    network: networkReducer,
  },
}); 