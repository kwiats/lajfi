import React from 'react';
import { View, StyleSheet, TouchableOpacity, Text } from 'react-native';
import { StackNavigationProp } from '@react-navigation/stack';
import { RouteProp } from '@react-navigation/native';
import { Ionicons } from '@expo/vector-icons';
import FloatingActionButton from "~/components/FloatingActionButton"; // Import ikonek

type RootStackParamList = {
  Home: undefined;
  TaskList: undefined;
  EventList: undefined;
};

type HomeScreenNavigationProp = StackNavigationProp<RootStackParamList, 'Home'>;
type HomeScreenRouteProp = RouteProp<RootStackParamList, 'Home'>;

type Props = {
  navigation: HomeScreenNavigationProp;
  route: HomeScreenRouteProp;
};

const HomeScreen: React.FC<Props> = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <FloatingActionButton />
      <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('TaskList')}>
        <Ionicons name="list-outline" size={20} color="#fff" style={styles.icon} />
        <Text style={styles.buttonText}>ToDo Lista</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('EventList')}>
        <Ionicons name="calendar-outline" size={20} color="#fff" style={styles.icon} />
        <Text style={styles.buttonText}>Eventy</Text>
      </TouchableOpacity>
      {/* Dodaj inne przyciski według potrzeby */}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f0f0f0',
    padding: 20,
  },
  button: {
    flexDirection: 'row', // Ustawienie kierunku układu wierszowego dla ikonek i tekstu
    backgroundColor: '#444',
    paddingVertical: 15,
    paddingHorizontal: 30,
    borderRadius: 10,
    marginVertical: 10,
    alignItems: 'center',
    width: '80%',
  },
  icon: {
    marginRight: 10,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
});

export default HomeScreen;
