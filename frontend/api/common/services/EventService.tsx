import api from '../../common/api';
import { Event } from '../../types';

export const getEvents = async (): Promise<Event[]> => {
  try {
    const response = await api.get('/events/');
    return response.data;
  } catch (error) {
    console.error('Error fetching events', error);
    throw error;
  }
};

export const getEvent = async (id: number): Promise<Event> => {
  try {
    const response = await api.get(`/events/${id}/`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching event with id ${id}`, error);
    throw error;
  }
};

export const createEvent = async (eventData: Partial<Event>): Promise<Event> => {
  try {
    const response = await api.post('/events/', eventData);
    return response.data;
  } catch (error) {
    console.error('Error creating event', error);
    throw error;
  }
};

export const updateEvent = async (id: number, eventData: Partial<Event>): Promise<Event> => {
  try {
    const response = await api.put(`/events/${id}/`, eventData);
    return response.data;
  } catch (error) {
    console.error(`Error updating event with id ${id}`, error);
    throw error;
  }
};

export const deleteEvent = async (id: number): Promise<void> => {
  try {
    await api.delete(`/events/${id}/`);
  } catch (error) {
    console.error(`Error deleting event with id ${id}`, error);
    throw error;
  }
};
