import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, Button, StyleSheet } from 'react-native';
import { Event } from '../../api/types';
import { getEvents, createEvent } from '../../api/common/services/EventService';

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
      <Button title="Add Event" onPress={handleCreateEvent} />
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
  },
  eventItem: {
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
  },
});

export default EventList;
