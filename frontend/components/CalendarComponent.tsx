import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { Calendar } from 'react-native-calendars';
import { Event } from '~/api/types';
import { getEvents } from '~/api/common/services/EventService';

const CalendarComponent: React.FC = () => {
  const [events, setEvents] = useState<Event[]>([]);
  const [selectedDate, setSelectedDate] = useState<string>(new Date().toISOString().split('T')[0]);

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

  const renderEvent = (date: string) => {
    return events
      .filter(event => event.start_time.startsWith(date))
      .map(event => (
        <View key={event.id} style={styles.eventItem}>
          <Text style={styles.title}>{event.title}</Text>
          <Text>{event.description}</Text>
        </View>
      ));
  };

  const markedDates = events.reduce((acc, event) => {
    const date = event.start_time.split('T')[0];
    acc[date] = { marked: true, dotColor: 'blue' };
    return acc;
  }, {});

  return (
    <View style={styles.container}>
      <Calendar
        onDayPress={(day) => setSelectedDate(day.dateString)}
        markedDates={{
          ...markedDates,
          [selectedDate]: { selected: true, marked: true, selectedColor: 'blue' },
        }}
      />
      <View style={styles.eventContainer}>
        {renderEvent(selectedDate)}
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  eventContainer: {
    marginTop: 16,
    paddingHorizontal: 16,
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

export default CalendarComponent;
