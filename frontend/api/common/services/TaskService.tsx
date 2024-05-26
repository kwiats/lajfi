import api from '../../common/api';
import { Task } from '../../types';

export const getTasks = async (): Promise<Task[]> => {
  try {
    const response = await api.get('/tasks/');
    return response.data;
  } catch (error) {
    console.error('Error fetching tasks', error);
    throw error;
  }
};

export const getTask = async (id: number): Promise<Task> => {
  try {
    const response = await api.get(`/tasks/${id}/`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching task with id ${id}`, error);
    throw error;
  }
};

export const createTask = async (taskData: Partial<Task>): Promise<Task> => {
  try {
    const response = await api.post('/tasks/', taskData);
    return response.data;
  } catch (error) {
    console.error('Error creating task', error);
    throw error;
  }
};

export const updateTask = async (id: number, taskData: Partial<Task>): Promise<Task> => {
  try {
    const response = await api.put(`/tasks/${id}/`, taskData);
    return response.data;
  } catch (error) {
    console.error(`Error updating task with id ${id}`, error);
    throw error;
  }
};

export const deleteTask = async (id: number): Promise<void> => {
  try {
    await api.delete(`/tasks/${id}/`);
  } catch (error) {
    console.error(`Error deleting task with id ${id}`, error);
    throw error;
  }
};
