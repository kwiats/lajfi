import 'react-native-gesture-handler';
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from './app/home/HomeScreen';
import TaskList from './app/task/TaskList';
import EventList from './app/event/EventList';
import AddTaskScreen from "~/app/task/AddTaskScreen";
import AddEventScreen from "~/app/event/AddEventScreen";

const Stack = createStackNavigator();

const App: React.FC = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="lajfi">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="TaskList" component={TaskList} />
        <Stack.Screen name="EventList" component={EventList} />
          <Stack.Screen name="AddTask" component={AddTaskScreen} />
        <Stack.Screen name="AddEvent" component={AddEventScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
