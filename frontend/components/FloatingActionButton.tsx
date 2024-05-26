import React from 'react';
import { FloatingAction } from 'react-native-floating-action';
import { useNavigation } from '@react-navigation/native';
import { Ionicons } from '@expo/vector-icons';
const actions = [
  {
    text: 'Dodaj Zadanie',
    icon: <Ionicons name="ios-list" size={20} color="#fff" />,
    name: 'bt_task',
    position: 1,
  },
  {
    text: 'Dodaj Wydarzenie',
    icon: <Ionicons name="ios-calendar" size={20} color="#fff" />,
    name: 'bt_event',
    position: 2,
  },
];

const FloatingActionButton: React.FC = () => {
  const navigation = useNavigation();

  return (
    <FloatingAction
      actions={actions}
      onPressItem={(name) => {
        if (name === 'bt_task') {
          navigation.navigate('AddTask'); // Zastąp odpowiednią nazwą ekranu dodawania zadania
        } else if (name === 'bt_event') {
          navigation.navigate('AddEvent'); // Zastąp odpowiednią nazwą ekranu dodawania wydarzenia
        }
      }}
    />
  );
};

export default FloatingActionButton;
