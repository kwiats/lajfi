import React, { useEffect, useState } from 'react';
import { Button, FlatList, StyleSheet, Text, View, TouchableOpacity } from 'react-native';
import { Event } from '~/api/types';
import { createEvent, getEvents } from '~/api/common/services/EventService';
import CalendarComponent from '~/components/CalendarComponent';

const EventList: React.FC = () => {
  const [events, setEvents] = useState<Event[]>([]);

  useEffect(() => {
    fetchEvents();
  }, []);

  const fetchEvents = async () => {
    try {
      const data = await getEvents();
      setEvents(data);
    } catch (error) {
      console.error('Error fetching events', error);
    }
  };

  const handleCreateEvent = async () => {
    try {
      const newEvent = {
        title: 'New Event',
        description: 'Description for new event',
        start_time: '2024-12-31T20:00:00',
        end_time: '2024-12-31T23:59:59',
      };
      await createEvent(newEvent);
      fetchEvents(); // Refresh the event list
    } catch (error) {
      console.error('Error creating event', error);
    }
  };

  return (
    <View style={styles.container}>
      <CalendarComponent />
      <TouchableOpacity style={styles.addButton} onPress={handleCreateEvent}>
        <Text style={styles.addButtonText}>Add Event</Text>
      </TouchableOpacity>
      <FlatList
        data={events}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={styles.eventItem}>
            <Text style={styles.title}>{item.title}</Text>
            <Text>{item.description}</Text>
          </View>
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: '#f8f9fa',
  },
  eventItem: {
    padding: 16,
    marginVertical: 8,
    backgroundColor: '#ffffff',
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#ddd',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
  },
  addButton: {
    backgroundColor: '#007bff',
    paddingVertical: 15,
    paddingHorizontal: 20,
    borderRadius: 8,
    alignItems: 'center',
    marginVertical: 16,
  },
  addButtonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },
});

export default EventList;
